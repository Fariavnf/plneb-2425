def gera_html():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>O Presidente dos Presidentes</title>
        <style>
            body {
                background-image: url('pictures/porto.gif');
                background-repeat: repeat;
                color: rgb(0, 0, 0);
                font-family: 'Times New Roman', serif;
                text-align: center;
            }

            header {
                background-color: rgb(0, 61, 165);
                padding: 10px 0;
                font-size: 2em;
                color: rgb(255, 215, 0);
                border: 3px solid rgb(255, 215, 0);
                font-family: 'Comic Sans MS', cursive;
                text-shadow: 2px 2px white;
            }

            .marquee-container {
                background-color: rgb(255, 215, 0);
                padding: 5px 0;
                font-family: 'Comic Sans MS', cursive;
            }

            marquee {
                font-size: 1.5em;
                font-weight: bold;
                color: rgb(0, 61, 165);
            }
            
            span { 
            padding-right: 200px;
            }

            .main-body {
                background-color: rgb(240, 240, 240); 
                border: 3px ridge rgb(128, 128, 128);
                width: 80%;
                margin: 20px auto;
                padding: 20px;
                font-family: 'Times New Roman', serif;
            }

            .content-section {
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: space-between;
                gap: 20px;
                margin-bottom: 20px;
                padding: 10px;
                border-bottom: 2px solid rgb(0, 61, 165);
            }
        
            .content-section img {
                width: 50%; 
                border: 3px inset rgb(0, 61, 165);
            }
        
            .content-text {
                width: 50%;
                text-align: justify;
            }
            
            .audio-controls {
                margin-top: 10px;
            }
            
        </style>
    </head>
    <body>
        <header>
            O Presidente dos Presidentes
        </header>
        <div class="marquee-container">
            <marquee behavior="scroll" direction="left"> 
                <span>Memorial a Jorge Nuno Pinto da Costa, o eterno Presidente </span>
                <span> A homenagem a Jorge Nuno Pinto da Costa nas portas do Estádio do Dragão </span> 
                <span> Uma inspiração eterna. Um legado Imortal </span> 
            </marquee>
        </div>
        <div class="main-body">
        
            <div class="content-section">
                <img src="pictures/Porta3.jpg">
                <h4>Porta 3 - Do TRI ao PENTA</h4>
                <p class="content-text">Neste espaço, são celebrados os três tricampeonatos (1996/97, 2007/2008 e 2012/2013), 
                                        os dois tetracampeonatos (1997/1998 e 2008/2009) e o único pentacampeonato (1998/1999) 
                                        alguma vez conquistado por um clube de futebol em Portugal, todos conseguidos com 
                                        Jorge Nuno Pinto da Costa como líder máximo do clube.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 4 - T'Antas Histórias</h4>
                <p class="content-text">O último título do Estádio das Antas foi festejado a 4 de maio de 2003. É o 19.º 
                                        do palmarés do FC Porto.</p>
                <img src="pictures/Porta4.jpg">
            </div>
            
            <div class="content-section">
                <img src="pictures/Porta6.jpg">
                <h4>Porta 6 - Constituição com nova vida</h4>
                <p class="content-text">O Constituição Park foi inaugurado a 6 de setembro de 2008, mais de seis décadas 
                                        depois de Jorge Nuno Pinto da Costa ter assistido lá ao seu primeiro jogo do FC Porto 
                                        enquanto criança com oito anos.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 7 - Os sete magníficos</h4>
                <p class="content-text">Foram sete os títulos internacionais conquistados pelo FC Porto durante a presidência 
                                        de Jorge Nuno Pinto da Costa. Duas Taças Intercontinentais, uma Taça dos Clubes Campeões 
                                        Europeus, uma Liga dos Campeões, uma Taça UEFA, uma Liga Europa e uma Supertaça Europeia 
                                        compõem um palmarés sem igual em Portugal.</p>
                <img src="pictures/Porta7.jpg">
            </div>
            
            <div class="content-section">
                <img src="pictures/Porta9.jpg">
                <h4>Porta 9 - Um super milagre</h4>
                <p class="content-text">A vitória épica na Supertaça conquistada a 9 de setembro de 1992 serviu de paradigma 
                                        para as 22 celebradas nos 42 anos de presidência de Jorge Nuno Pinto da Costa.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 10 - Contra tudo e contra todos</h4>
                <p class="content-text">A representação da conquista da Taça de Portugal a 10 de junho de 1994 simboliza 
                                        as 16 edições da prova rainha celebradas durante a vigência do histórico dirigente 
                                        azul e branco.</p>
                <img src="pictures/Porta10.jpg">
            </div>
            
            <div class="content-section">
                <img src="pictures/Porta12.jpg">
                <h4>Porta 12 - O início</h4>
                <p class="content-text">A 12 de maio de 1985, Jorge Nuno Pinto da Costa celebrou o primeiro campeonato 
                                        nacional enquanto presidente do FC Porto.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 13 - No topo do Mundo</h4>
                <p class="content-text">A 13 de dezembro de 1987, na neve de Tóquio, o FC Porto sagrou-se Campeão do Mundo 
                                        pela primeira vez.</p>
                <img src="pictures/Porta13.jpg">
            </div>
            
            <div class="content-section">
                <img src="pictures/Porta17.jpg">
                <h4>Porta 17 - O primeiro dia do resto da nossa vida</h4>
                <p class="content-text"> Jorge Nuno Pinto da Costa foi eleito para o primeiro de 15 mandatos no dia 17 
                                        de abril de 1982.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 18 - Dublin pintada a azul</h4>
                <p class="content-text">O sétimo troféu internacional da história azul e branca viajou de Dublin para a 
                                        Invicta a 18 de maio de 2011.</p>
                <img src="pictures/Porta18.jpg">
            </div>
            
             <div class="content-section">
                <img src="pictures/Porta20.jpg">
                <h4>Porta 20 - Em casa é que é bom!</h4>
                <p class="content-text"> O primeiro campeonato conquistado no Estádio do Dragão chegou a 20 de maio de 2007.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 21 - Sevilha eterna</h4>
                <p class="content-text">A primeira Taça UEFA veio de Sevilha para Portugal a 21 de maio de 2003.</p>
                <img src="pictures/Porta21.jpg">
            </div>
            
            <div class="content-section">
                <img src="pictures/Porta23.jpg">
                <h4>Porta 23 - Campeão Supremo</h4>
                <p class="content-text"> O número de campeonatos conquistados enquanto líder máximo da instituição.</p>
            </div>
            
            <div class="content-section">
                <h4>Porta 24 - “Eu luto 24 horas pelo FC Porto”</h4>
                <p class="content-text">“Eu luto 24 horas pelo FC Porto” - uma entrada com frases simbólicas do Presidente 
                                        dos Presidentes.</p>
                <img src="pictures/Porta24.jpg">
            </div>
            
            <div class="content-section">
                <img src="pictures/Porta27.jpg">
                <h4>Porta 27 - Campeão Europeu</h4>
                <p class="content-text"> O FC Porto sagrou-se Campeão Europeu pela primeira vez a 27 de maio de 1987, em Viena.</p>
            </div>
        </div>
        
        <div class="audio-controls">
            <button id="playPauseButton" onclick="togglePlayPause()">▶️</button>
            <input type="range" id="volume" min="0" max="1" step="0.1" onchange="setVolume(this.value)">
        </div>

        <audio id="audio" autoplay loop muted>
            <source src="audio/hino.m4a" type="audio/mp4">
        </audio>

        <script>
        const audio = document.getElementById("audio");
        const playPauseButton = document.getElementById("playPauseButton");
    
        window.addEventListener('click', () => {
            audio.muted = false;
        }, { once: true });
    
        function formatTime(seconds) {
            if (isNaN(seconds)) return "0:00";  // If duration is not loaded, return default
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
        }
    
        function updateButtonText() {
            const currentTime = formatTime(audio.currentTime);
            const totalTime = formatTime(audio.duration);
            playPauseButton.textContent = audio.paused 
                ? `▶️ ${currentTime} / ${totalTime}`
                : `⏸️ ${currentTime} / ${totalTime}`;
        }
    
        function togglePlayPause() {
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
            updateButtonText();
        }
    
        function setVolume(value) {
            audio.volume = value;
        }
        
        audio.addEventListener("loadedmetadata", updateButtonText);
        audio.addEventListener("timeupdate", updateButtonText);
    </script>
    </body>
    </html>
    """
    return html_content


if __name__ == '__main__':
    html_text = gera_html()
    with open("out.html", "w", encoding="utf-8") as html_out:
        html_out.write(html_text)
