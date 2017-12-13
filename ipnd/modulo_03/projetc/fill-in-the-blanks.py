# coding=utf-8

# Estrutura de dados do jogo
data = {
    'facil': {
        'phrase': "A ___1___ (World Wide Web) é uma coleção de documentos " + \
         "___2___ (HyperText Markup Language), o principal tipo de documento " + \
         "que nela pode ser contido. Entretanto, diversos outros tipos de " + \
         "arquivos são suportados: ___3___, vídeos, músicas, textos planos, " + \
         "entre outros. A comunicação entre esses documentos é realizada " + \
         "por meio de ___4___.",
        'answers': ['WWW','HTML','imagens','hyperlinks'],
        'lives': 5
    },
    'medio': {
        'phrase': "A Web é composta pelo ___1___ (você, seu computador e " + \
         "um navegador), a ___2___ e os ___3___es que armazenam os documentos " + \
         "HTML. O ___1___, através do ___4___, interage com o ___3___ por meio " + \
         "do protocolo HTTP (Hypertext Transfer Protocol), requisitando os " + \
         "documentos HTML e demais tipos associados.",
        'answers': ['cliente','Internet','servidor','navegador'],
        'lives': 2
    },
    'dificil': {
        'phrase': "O ___1___ modifica o HTML alterando diretamente o elemento " + \
        "ou através de ___2___es. Os ___2___es são os nomes utilizados para " + \
        "filtrar os elementos atribuídos a uma ___3___ ou atributo de " + \
        "___4___ (ID).",
        'answers': ['CSS','seletor','classe','identificação'],
        'lives': 1
    }
}

"""Imprime o Banner inicial"""
def banner(level,data):
    print "Você possui " + str(data[level]['lives']) + " tentativa(s)!"

"""Seleciona o nivel das perguntas a serem feitas ao usuario"""
def select_level(data):
    while True:
        level = raw_input("Selecione o nivel de dificuldade (facil, medio ou dificil): ")
        if level in data:
            return level
        print "Nível \"" + level + "\" não suportado! Tente novamente."

"""Inicializa o jogo com as vidas (tentativas máximas), os numeros de acertos
o nivel, o numero maximo de acertos necessarios e a frase escolhida"""
def init_game(data):
    level = select_level(data)
    banner(level,data)
    lives = data[level]['lives']
    hits = 0
    max_hits = len(data[level]['answers'])
    phrase = data[level]['phrase']
    return lives,hits,max_hits,level,phrase

"""Imprime o resultado do jogo dada a quantidade de acertos"""
def result(hits,max_hits):
    if (hits == max_hits):
        return "Você venceu!"
    else:
        return "Você não conseguiu acertar todos os desafios! Revise o conteúdo!"

""" Implementa as regras e o fluxo do jogo """
def play_game(data):
    lives,hits,max_hits,level,phrase = init_game(data)
    while (lives > 0 and hits < max_hits):
        print phrase
        answer = raw_input("Qual a palavra que substitui ___"+ str(hits+1) + "___? " +
        "(tentativas restantes = "+str(lives)+") ")
        if (answer.lower() == data[level]['answers'][hits].lower()):
            print "\nCorreto!\n"
            phrase = phrase.replace("___"+str(hits + 1)+"___", data[level]['answers'][hits])
            hits += 1
        else:
            print "\nResposta incorreta!\n"
            lives -= 1
    print result(hits,max_hits)

play_game(data)
