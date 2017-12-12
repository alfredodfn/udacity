# coding=utf-8

LIVES = 5

LEVEL_LIST = ['fácil','médio','difícil']

# PHRASES e LIST_OF_ANSWERS sao relacionadas pelo indice da lista.
# Ou seja, LIST_OF_ANSWERS[0] contém as respostas de PHRASES[0]
PHRASES = [
    "A ___1___ (World Wide Web) é uma coleção de documentos ___2___ " +
    "(HyperText Markup Language), o principal tipo de documento que nela pode " +
    "ser contido. Entretanto, diversos outros tipos de arquivos são suportados: " +
    "___3___, vídeos, músicas, textos planos, entre outros. A comunicação entre " +
    "esses documentos é realizada por meio de ___4___.",

    "A Web é composta pelo ___1___ (você, seu computador e um navegador), a ___2___ e os ___3___es que armazenam os documentos HTML. O ___1___, através do ___4___, interage com o ___3___ por meio do protocolo HTTP (Hypertext Transfer Protocol), requisitando os documentos HTML e demais tipos associados.",

    "O ___1___ modifica o HTML alterando diretamente o elemento ou através de ___2___es. Os ___2___es são os nomes utilizados para filtrar os elementos atribuídos a uma ___3___ ou atributo de ___4___ (ID)."
]

# Par identificador <-> valor que reflete a resposta para cada espaço
LIST_OF_ANSWERS = [
    [["___1___","WWW"],["___2___","HTML"],["___3___","imagens"],
        ["___4___","hyperlinks"]],
    [["___1___","cliente"],["___2___","Internet"],["___3___","servidor"],
        ["___4___","navegador"]],
    [["___1___","CSS"],["___2___","seletor"],["___3___","classe"],
        ["___4___","identificação"]]
]

# Imprime o Banner inicial
def banner(lives):
    print "Você possui " + str(lives) + " tentativa(s)!"
    print "Informe o nivel de dificuldade. Pode ser: fácil, médio ou difícil."

# Inicializa o jogo com as vidas (tentativas máximas) e os numeros de acertos
def init(lives):
    banner(lives)
    lives = lives
    hits = 0
    return lives,hits

# Retorna o indice de uma frase baseado na dificuldade
def select_phrase_index(level, level_list):
    return level_list.index(level)

# Retorna uma lista com todas as chaves de substituicao (e.g., ___1___)
# encontradas para uma determinada frase
def get_replacement_keys(index, list_of_answers):
    keys = []
    i = 0
    while ( i < len(list_of_answers[index])):
        keys.append(list_of_answers[index][i][0])
        i += 1
    return keys

# Verifica se a resposta esta presente na lista de respostas de uma
# determinada pergunta
def check_answer(answer, key, list_of_answer):
    for la in list_of_answer:
        if la[0] == key and la[1].lower() == answer.lower():
            return True
    return False

# substitui a palavra key por answer em phrase
def replace_answer(answer,key,phrase):
    return phrase.replace(key,answer)

# Imprime o resultado do jogo baseado na quantidade de acertos
def result(hits,max_hits):
    if (hits == max_hits):
        return "Você venceu!"
    else:
        return "Você não conseguiu acertar todos os desafios! Revise o conteúdo!"

# Jogo em si, captura as informações do usuário e implementa as regras
def play_game(lives,phrases,list_of_answers,level_list):
    lives,hits = init(LIVES)
    level = ""
    while level not in level_list:
        level = raw_input("Selecione o nivel de dificuldade: ")
    index = select_phrase_index(level,level_list)
    phrase = phrases[index]
    print phrase
    keys = get_replacement_keys(index, list_of_answers)
    max_hits = len(keys)
    while (lives > 0 and hits < max_hits):
        answer = raw_input("Qual a palavra que substitui "+ keys[hits] + "? " +
        "(tentativas restantes = "+str(lives)+") ")
        if (check_answer(answer, keys[hits], list_of_answers[index]) == False):
            lives -= 1
            print "Tente novamente!"
        else:
            phrase = replace_answer(answer,keys[hits],phrase)
            print phrase
            hits += 1
    print result(hits,max_hits)

play_game(LIVES,PHRASES,LIST_OF_ANSWERS,LEVEL_LIST)
