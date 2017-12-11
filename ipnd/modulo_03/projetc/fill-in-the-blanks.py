# coding=utf-8
LIVES = 5

# PHRASES e LIST_OF_ANSWERS sao relacionadas pelo indice da lista.
# Ou seja, LIST_OF_ANSWERS[0] contém as respostas de PHRASES[0]
PHRASES = [
    "Essa eh ___1___ a primeira ___2___ frase ___3___ e ___4___",
    "Essa eh a segunda frase",
    "Essa eh a terceira frase",
]

# Par identificador <-> valor que reflete a resposta para cada espaço
LIST_OF_ANSWERS = [
    [["___1___","Resposta"],["___2___","Resposta"],["___3___","Resposta"],
        ["___4___","Resposta"]],
    [["___1___","Resposta"],["___2___","Resposta"],["___3___","Resposta"],
        ["___4___","Resposta"]],
    [["___1___","Resposta"],["___2___","Resposta"],["___3___","Resposta"],
        ["___3___","Resposta"]]
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
def select_phrase(level):
    if (level == 'fácil'):
        return 0
    elif (level == 'médio'):
        return 1
    elif (level == 'difícil'):
        return 2
    # TODO: lancar uma exception caso nome nao suportado
    return None

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
        if la[0] == key and la[1] == answer:
            return True
    return False

# Imprime o resultado do jogo baseado na quantidade de acertos
def result(hits,max_hits):
    if (hits == max_hits):
        return "Você venceu!"
    else:
        return "Você não conseguiu acertar todos os desafios! Revise o conteúdo!"

# Jogo em si, captura as informações do usuário e implementa as regras
def play_game(lives,phrases,list_of_answers):
    lives,hits = init(LIVES)
    level = raw_input("Selecione o nivel de dificuldade: ")
    index = select_phrase(level)
    print phrases[index]
    keys = get_replacement_keys(index, list_of_answers)
    max_hits = len(keys)
    while (lives > 0 and hits < max_hits):
        answer = raw_input("Qual a palavra que substitui "+ keys[hits] + "? " +
        "(tentativas restantes = "+str(lives)+") ")
        if (check_answer(answer, keys[hits], list_of_answers[index]) == False):
            lives -= 1
            print "Tente novamente!"
        else:
            print phrases[index]
            hits += 1
    print result(hits,max_hits)

play_game(LIVES,PHRASES,LIST_OF_ANSWERS)
