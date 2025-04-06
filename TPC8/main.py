import requests
from bs4 import BeautifulSoup
import json

LINK = 'https://www.atlasdasaude.pt/doencasAaZ'
LINK2 = 'https://www.atlasdasaude.pt'



def find_letters_href():

    html_doc = requests.get(LINK)
    html_content = html_doc.text
    soup = BeautifulSoup(html_content, 'html.parser')

    hrefs = []

    for div in soup.find_all('div', class_='views-summary views-summary-unformatted'):
        a_tag = div.find('a')
        if a_tag:
            hrefs.append(a_tag['href'])

    return hrefs


def get_dic(hrefs):

    dic = {}

    for href in hrefs:

        html_doc = requests.get(LINK2+href)
        html_content = html_doc.text

        soup = BeautifulSoup(html_content, 'html.parser')


        for div_row in soup.find_all('div', class_='views-row'):

            termo_link = div_row.find('a')['href']
            termo = div_row.div.h3.a.text
            resumo_div = div_row.find('div', class_='views-field-body')
            resumo = resumo_div.div.text

            info = doenca_info(LINK2+termo_link)

            dic[termo] = {'resumo': resumo, 'URL': termo_link}

            for k,v in info.items():
                dic[termo][k] = v


    return dic


def doenca_info(url):

    html_doc = requests.get(url)
    html_content = html_doc.text

    soup = BeautifulSoup(html_content, 'html.parser')

    info = {'description' : {'Text' : ''}}
    key = 'description'

    for div_info in soup.find_all('div', class_='field-name-body'):

        for elem in div_info.div.div:

            if elem.name == 'h2':
                key = elem.text.strip('\f')
                info[key] = {}

            elif elem.name == 'p':
                if info[key].get('Text') is None:
                    info[key]['Text'] = ''
                else:
                    info[key]['Text'] += f'{elem.text}\n'

            elif elem.name == 'div':
                if info[key].get('Text') is None:
                    info[key]['Text'] = ''
                else:
                    info[key]['Text'] += f'{elem.text}\n'

            elif elem.name == 'ul' and info[key]:
                for li in elem.find_all('li'):
                    if info[key].get('List') is None:
                        info[key]['List'] = [li.text]
                    else:
                        info[key]['List'].append(li.text)

            elif elem.name == 'h3':
                if info[key].get('List') is None:
                    info[key]['List'] = [elem.a.get('href')]
                else:
                    info[key].get('List').append(elem.a.get('href'))


    div_content = soup.find('div', class_="node-doencas")
    div_nota = div_content.find('div', class_="field-name-field-nota")
    if div_nota:
        nota = div_nota.find("div", class_= "field-item even").text
        info["Nota"] = nota

    return info


if __name__ == '__main__':


    hrefs = find_letters_href()


    dic = get_dic(hrefs)

    f_out = open("termos.json", "w", encoding="utf-8")
    json.dump(dic, f_out, indent=4, ensure_ascii=False)
    f_out.close()













        

















