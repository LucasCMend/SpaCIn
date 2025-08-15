🚀 SpaCIn - Uma Odisséia Espacial
Este projeto é um jogo de nave no estilo "collectathon", inspirado em clássicos como Space Invaders e Subway Surfers. Desenvolvido como parte da disciplina de Introdução à Programação, o jogo desafia o jogador a sobreviver a uma chuva de asteroides e inimigos, testando seus reflexos e habilidades.

Membros da equipe:

Daniel Acioly <dgla>
Guilherme Valença <gvs2>
Gustavo Leão <gjcln>
João Gabriel Caldas <jgmc>
Lucas Mendonça <lcm>
Luís Felipe Durães <lflld>

Arquitetura do Projeto
O código foi organizado seguindo os princípios da Programação Orientada a Objetos (POO) para garantir que o projeto seja modular, legível e fácil de expandir. A estrutura principal é dividida em classes, cada uma com uma responsabilidade única:

Inimigos.py - Contém a lógica dos inimigos e os tiros que eles disparam. Definindo as funções update, desenhar e init.

Projeto_de_IP.py - Código principal do jogo. Nele contém todas as lógicas necessárias para o jogo rodar, por exemplo: Colisões, tiro dos inimigos, movimentações, remover objetos, geração dos coletáveis, definição dos limites e masks.

asteroides.py - Contém a lógica dos asteroides. Definindo as funções update, desenhar e init.

coletaveis.py - Contém a lógica dos coletáveis das placas e dos galões de combustível. Definindo as funções update, desenhar e init.

dados.py - Imprime na tela a quantidade de placas, de combustível e a fase do usuário.

final.py - Contém a lógica de final de jogo e avanço de fase. Definindo o fim da fase e a música a ser tocada.

fundo.py - Contém a lógica do plano de fundo do jogo e seu movimento de acordo com o avanço do jogador.

game_over.py - Contém a tela de fim de jogo. Definindo o que será mostrado ao fim do jogo e a música.

restart.py - Contém a lógica para permitir o reinício do jogo após o fim do jogo.

settings.py - Contém os dados básicos do jogo.

ship.py - Contém a lógica da nave do jogador e seu movimento de acordo para onde o jogador está se movendo. Definindo as funções update, desenhar, init e mask.

stars.py - Contém a lógica das estrelas que ficam no plano de fundo do jogo e seu movimento de acordo com o avanço do jogador.

story.py - Contém a lógica que unifica a história do jogo com o menu e com o jogo em si.

tela_menu.py - Contém a lógica da tela de menu. Definindo as funções init, draw e run.

pastas - Onde estão colocados os arquivos de imagem e áudio do jogo. 


 Ferramentas e Bibliotecas
Python 3: É uma linguagem de programação versátil, poderosa e com uma sintaxe limpa, ideal para o aprendizado de conceitos fundamentais e para o desenvolvimento rápido de projetos como este.

Pygame: É a biblioteca padrão da indústria para o desenvolvimento de jogos 2D em Python. Foi escolhida por fornecer todas as ferramentas necessárias para a criação do nosso jogo, como manipulação de janelas, renderização de imagens (sprites), detecção de eventos (teclado) e controle de frame rate.

Git e GitHub: Ferramentas essenciais para o controle de versão e o trabalho em equipe. Utilizamos o GitHub para hospedar o projeto e o Git para gerenciar as diferentes versões do código. O uso de branches foi fundamental para que cada membro pudesse trabalhar em uma funcionalidade (ex: um na nave, outro nos asteroides) sem interferir no trabalho dos outros.


 Divisão de Trabalho:
O time definiu as funções separando cada um com uma classe diferente de início. E fomos projetando as necessidades e ajustes pontuais de acordo com a disponibilidade e necessidade de cada.

Felipe - Classe de asteroides
Gustavo - Classe de coletáveis e músicas
João - Classe da nave e do fundo
Lucas - Classe dos inimigos
Daniel - Classe e lógica do menu e geração de imagens
Guilherme - Geração de imagens e lógica de fim de jogo
Todos - Integração no código principal e ajustes
 

 Conceitos usados:
O principal dele foi as lógicas básicas de if, else e laços de repetição (for e while) já que a biblioteca pygame facilita muito o trabalho da equipe. Além disso, a definição de funções foi algo fundamental no projeto pois facilita demais o processo e garante que o código fique o mais limpo possível, atribuindo as funções para as devidas classes.


 Desafios e erros do projeto:
	Principal desafio: O maior desafio foi a definição da ideia, já que tivemos muitas ideias diferentes. E mesmo após definir a ideia central, o time queria ficar sempre aumentando o escopo do projeto para ter o melhor jogo possível. Mas fizemos uma reunião presencial no começo do projeto para colocar o time no mesmo compasso e iniciar o projeto de forma coesa.
	Principal erro: Uso correto do github e das branches. Tivemos dificuldade de aplicar boas práticas de programação com o uso de branches de forma correta, até pela falta de familiaridade de uso do github. Fizemos de forma separada os códigos e sempre aplicávamos de forma única na main branch.
	Principal lição aprendida: Que conseguimos trabalhar bem em equipe e executar um bom projeto apesar da falta de familiaridade inicial com as tecnologias e bibliotecas usadas.
 
 Galeria:

 
