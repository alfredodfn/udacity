LIVES = 5

# PHRASES and LIST_OF_ANSWERS sao dependentes pelo indice
PHRASES = [
    "Essa eh ___1___ a primeira ___2___ frase ___3___ ",
    "Essa eh a segunda frase",
    "Essa eh a terceira frase",
]

LIST_OF_ANSWERS = [
    [["___1___","Resposta"],["___2___","Resposta"],["___3___","Resposta"]],
    [["___1___","Resposta"],["___2___","Resposta"],["___3___","Resposta"]],
    [["___1___","Resposta"],["___2___","Resposta"],["___3___","Resposta"]]
]

def banner(lives):
    print "Voce possui " + str(lives) + " tentativas!"
    print "Informe o nivel de dificuldade. Pode ser: baixo, medio ou alto."

# Inicializa o jogo
def init(lives):
    banner(lives)
    lives = lives
    hits = 0
    return lives,hits

# Retorna o indice de uma frase baseado na dificuldade
def select_phrase(level):
    if (level == 'baixo'):
        return 0
    elif (level == 'medio'):
        return 1
    elif (level == 'alto'):
        return 2
    # TODO: lancar uma exception caso nome nao suportado
    return None

# Retorna uma lista com as chaves de
# substituicao (e.g., ___1___) para uma determinada frase
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

def play_game(lives,phrases,list_of_answers):
    lives,hits = init(LIVES)
    level = raw_input("Selecione o nivel de dificuldade: ")
    index = select_phrase(level)
    print phrases[index]
    keys = get_replacement_keys(index, list_of_answers)
    max_hits = len(keys)
    while (lives > 0 and hits < max_hits):
        answer = raw_input("Qual a palavra que substitui "+ keys[hits] + "? ")
        if (check_answer(answer, keys[hits], list_of_answers[index]) == False):
            lives -= 1
        else:
            hits += 1

play_game(LIVES,PHRASES,LIST_OF_ANSWERS)
