import requests
from bs4 import BeautifulSoup
import json
import logging
import re

LINK = 'https://revista.spmi.pt/index.php/rpmi/issue/archive'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='scrappy_content.log',
    encoding='utf-8',
    filemode='a'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

def find_issue():
    base_url = LINK
    issues = {}
    page = 1
    total_count = 0
    
    while True:
        if page == 1:
            current_url = base_url
        else:
            current_url = f"{base_url}/{page}"
        
        print(f"Fetching page {page}: {current_url}")
        response = requests.get(current_url)
        
        if response.status_code != 200:
            print(f"Page {page} not found. Status code: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        list_items = soup.select('ul.issues_archive > li')
        
        if not list_items:
            print(f"No more issues found on page {page}")
            break
        
        for item in enumerate(list_items):
            i = total_count + item[0]
            item = item[1]
            

            issue_summary = item.select_one('div.obj_issue_summary')
            if not issue_summary:
                continue
                

            title_link = issue_summary.select_one('a.title')
            
            if title_link:

                name = title_link.text.strip()
                url = title_link.get('href')
                
                series_div = issue_summary.select_one('div.series')
                if series_div:
                    name += " - " + series_div.text.strip()
                
                issues[i] = {"name": name, "URL": url}
        

        total_count += len(list_items)
        page += 1
    

    with open('issues.json', 'w', encoding='utf-8') as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)
    
    print(f"Found {total_count} issues across {page-1} pages")


def find_issue_pubs():
    with open('issues.json', 'r', encoding='utf-8') as f:
        issues = json.load(f)

    total_pubs = 0
    
    for issue_id, issue_data in issues.items():
        issue_url = issue_data['URL']
        
        print(f"Processing issue {issue_id}: {issue_url}")
        response = requests.get(issue_url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve issue page. Status code: {response.status_code}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        pubs = []
        
        article_titles = soup.select('h3.title')
        
        for title_elem in article_titles:
            link = title_elem.select_one('a')
            
            if link:
                article_id = link.get('id', '')
                article_url = link.get('href', '')
                

                subtitle_span = link.select_one('span.subtitle')
                title_pt = ""
                if subtitle_span:
                    title_pt = subtitle_span.text.strip()
                    # Remove the span from the link to get just the main title
                    subtitle_span.extract()
                

                article_title = link.text.strip()
                

                pub_info = {
                    "title": article_title,
                    "title-pt": title_pt,
                    "URL": article_url,
                    "article_id": article_id
                }
                
                pubs.append(pub_info)
        
        issue_data['publications'] = pubs
        total_pubs += len(pubs)
        
        print(f"Found {len(pubs)} publications in this issue\n")
    
    with open('issues_with_pubs.json', 'w', encoding='utf-8') as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)
    
    print(f"Total publications found: {total_pubs}")
    return issues


def find_pub_content():
    with open('issues_with_pubs.json', 'r', encoding='utf-8') as f:
        issues = json.load(f)

    for issue_id, issue_data in issues.items():
        pubs = issue_data['publications']

        for pub in pubs:
            article_url = pub['URL']
            article_id = pub['article_id']

            logging.info(f"Processing publication {article_id}: {article_url}")
            response = requests.get(article_url)

            if response.status_code != 200:
                logging.error(f"Failed to retrieve publication page. Status code: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            ### AUTHORS ###
            authors_div = soup.select_one('section.item.authors')

            if authors_div:
                authors = soup.select('ul.authors > li')
                pub['authors'] = []

                for author in authors:
                    author_data = {}

                    name_span = author.select_one('span.name')
                    if name_span:
                        author_data['name'] = name_span.text.strip()
                    

                    affil_span = author.select_one('span.affiliation')
                    if affil_span:
                        author_data['affiliation'] = affil_span.text.strip()
                    

                    orcid_span = author.select_one('span.orcid')
                    if orcid_span and orcid_span.find('a'):
                        author_data['orcid'] = orcid_span.find('a')['href']
                    
                    pub['authors'].append(author_data)
                
                logging.info(f"Found {len(pub['authors'])} authors for publication {article_id}")

            ### DOI ###
            doi_div = soup.select_one('section.item.doi')
            if doi_div:
                doi_link = doi_div.select_one('a')
                if doi_link:
                    pub['doi'] = doi_link.get('href', '')
                    logging.info(f"Found DOI for publication {article_id}: {pub['doi']}")

            ### KEYWORDS ###
            keywords_section = soup.select_one('section.item.keywords')
            if keywords_section:
                keywords_span = keywords_section.select_one('span.value')
                if keywords_span:
                    clean_keywords = keywords_span.text.strip()
                    pub['keywords'] = re.sub(r'\s+', ' ', clean_keywords)
                    logging.info(f"Found keywords for publication {article_id}: {pub['keywords']}")    

            ### ABSTRACT ###
            abstract_section = soup.select_one('section.item.abstract')
            if abstract_section:
                paragraphs = abstract_section.select('p')
                if paragraphs:
                    pub['abstract'] = {}
                    has_sections = False
                    
                    for p in paragraphs:
                        strong_tag = p.select_one('strong')
                        if strong_tag:
                            section_name = strong_tag.text.strip().rstrip(':')
                            
                            strong_tag.extract()
                            
                            content = p.text.strip()

                            pub['abstract'][section_name] = content
                            has_sections = True
                        else:
                            content = p.text.strip()
                            if content:
                                if "General" not in pub['abstract']:
                                    pub['abstract']["General"] = content
                                else:
                                    pub['abstract']["General"] += " ".join(content)
                    
                    if not has_sections and len(pub['abstract']) == 1 and "General" in pub['abstract']:
                        abstract_content = pub['abstract']["General"]
                        pub['abstract'] = {"Abstract": abstract_content}
                    
                    logging.info(f"Found abstract with {len(pub['abstract'])} sections for publication {article_id}")

    with open('issues_pubs_content.json', 'w', encoding='utf-8') as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)

    logging.info(f"Finished processing authors for all publications")




if __name__ == "__main__":
    #find_issue()
    #find_issue_pubs()
    find_pub_content()



