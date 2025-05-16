# Nome completo do primeiro membro: Roger Honorato
# RA do primeiro membro: 247617
# Nome completo do segundo membro: Leonardo Paillo da Silva
# RA do segundo membro: 198218

import random
from utils import load_words, ALL_COLORS


lista_palavras = load_words()
palavras_filtradas = lista_palavras.copy()

for i in lista_palavras:  # filtra as palavras com tamanho invalido
    if len(i) != 5:
        palavras_filtradas.remove(i)
lista_palavras = palavras_filtradas.copy()


def filtro_red():  # remove as palavras que tem letras eliminadas
    placeholder = lista_palavras.copy()
    for palavra in placeholder:
        for letra in eliminadas:
            if letra in palavra:
                lista_palavras.remove(palavra)
                break
    return lista_palavras


def filtro_yellow(letra, posicao):
    placeholder = lista_palavras.copy()
    for palavra in placeholder:

        if letra not in palavra:  # remove palavras que não possuem a letra
            lista_palavras.remove(palavra)

        else:  # remove palavras onde a letra amarela está na mesma posição
            if palavra[posicao] == letra:
                lista_palavras.remove(palavra)

    return lista_palavras


def filtro_green(letra, posicao): #segue a lógica oposta do filtro amarelo
    placeholder = lista_palavras.copy()

    for palavra in placeholder:

        if letra not in palavra: 
            lista_palavras.remove(palavra)

        elif palavra[posicao] != letra:
            lista_palavras.remove(palavra)

    return lista_palavras


amarelas = []  # letras que estão na palavra correta
correta = ["", "", "", "", ""]  # resposta correta, com as letras em ordem
eliminadas = []  # letras eliminadas


def player(guess_hist, res_hist):
    global lista_palavras

    if guess_hist != [] and res_hist != []:
        ultima_tentativa = guess_hist[-1]
        correção = res_hist[-1]

        # relaciona as letras com a resposta
        jogada = [
            [ultima_tentativa[0], correção[0]],
            [ultima_tentativa[1], correção[1]],
            [ultima_tentativa[2], correção[2]],
            [ultima_tentativa[3], correção[3]],
            [ultima_tentativa[4], correção[4]],
            ]

        for sublist in jogada:
            letra = sublist[0]

            match sublist[1]:  # roda os filtros de palavras (menos o vermelho)

                case "GREEN":
                    correta.pop(jogada.index(sublist))
                    correta.insert(jogada.index(sublist), letra)
                    lista_palavras = filtro_green(letra.upper(), jogada.index(sublist))

                case "RED":
                    if letra not in eliminadas:
                        eliminadas.append(letra)

                case "YELLOW":
                    if letra not in amarelas:
                        amarelas.append(letra)

                    lista_palavras = filtro_yellow(letra.upper(), jogada.index(sublist))

        if len("".join(correta)) != 5:
            placeholder = eliminadas.copy()

            for letra in placeholder:
                if letra in correta:
                    eliminadas.remove(letra)

                elif letra in amarelas:
                    eliminadas.remove(letra)

            lista_palavras = filtro_red()  # roda depois para não se opor aos outros filtros
            guess = random.choice(lista_palavras)

        else:
            guess = "".join(correta)

    else: #caso do primeiro guess, com palavras 'ideais'
        if 'TRACE' in lista_palavras:
            guess = 'trace'

        elif 'CLASE' in lista_palavras:
            guess = 'clase'

        elif 'METAL' in lista_palavras:
            guess = 'metal'

        elif 'ELICA' in lista_palavras:
            guess = 'elica'

    return guess
