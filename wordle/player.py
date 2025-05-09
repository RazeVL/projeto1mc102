
# Nome completo do primeiro membro: Roger Honorato
# RA do primeiro membro: 247617
# Nome completo do segundo membro: [Segundo membro da equipe]
# RA do segundo membro: [Segundo membro da equipe]

"""
Implemente aqui o seu código para adivinhar a palavra.

Seu principal objetivo é implementar a função `player`, que deve retornar uma palavra (string) como seu próximo palpite.
Caso sua função não retorne uma string, a automatização não irá ocorrer tanto em game.py quanto em tournament.py.
Caso sua função retorne a string vazia, você poderá jogar manualmente (teclado).

Observações:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
- A função recebe duas listas como argumento:
    - guess_hist: lista de palavras que foram chutadas anteriormente
    - res_hist: lista de respostas dos chutes anteriores
- A função deve retornar uma string como palpite

Lembretes:
- Segue a coloração possíveis dos caracteres:
    - Correto: verde ("GREEN")
    - Presente mas na posição errada: amarelo ("YELLOW")
    - Ausente: vermelho ("RED")

Para mais informações, reveja o README.md
"""

import random
from utils import load_words, ALL_COLORS, load_words

words = load_words()   # Carrega a lista de palavras
placeholder = words.copy()

for i in words:  # remove todas as palavras com tamanho invalido
    if len(i) != 5:
        placeholder.remove(i)
words = placeholder.copy()


def filtro(eliminadas):  # filtra a lista de palavras possíveis, removendo todas as que tem letras eliminadas
    try:
        if type("".join(correta)) == str:   # verifica se a palavra ja foi descoberta, e se sim, retorna ela.
            return ("".join(correta))
    except TypeError:
        for palavras in words:
            for char in palavras:
                if char in eliminadas:
                    placeholder.remove(palavras)
                    break
    return placeholder


resp_chr = []  # Letras que estão na palavra correta
eliminadas = []  # Letras que não estão na palavra correta
correta = ["", "", "", "", ""]  # resposta correta, com as letras em ordem


def player(guess_hist, res_hist):
    if guess_hist != [] and res_hist != []:
        ultima_tentativa = guess_hist[-1]
        correção = res_hist[-1]
        # relaciona as letras com a resposta
        a = [
            [ultima_tentativa[0], correção[0]],
            [ultima_tentativa[1], correção[1]],
            [ultima_tentativa[2], correção[2]],
            [ultima_tentativa[3], correção[3]],
            [ultima_tentativa[4], correção[4]],
            ]
        for sublist in a:
            letra = sublist[0]

            match sublist[1]:   # verifica qual a resposta
                case "GREEN":
                    if letra not in resp_chr:
                        resp_chr.append(letra)
                    # adiciona o caractere na posição correta
                    correta.pop(a.index(sublist))
                    correta.insert(a.index(sublist), letra)

                case "RED":
                    if letra not in eliminadas:
                        eliminadas.append(letra)

                case "YELLOW":
                    if letra not in resp_chr:
                        resp_chr.append(letra)

        global words
        words = filtro(eliminadas)
        guess = random.choice(words)
        print(f"{correta}\n{resp_chr}\n{eliminadas}")
        return guess

    else:
        return "aureo"  # palavra de início, provavelmente não pode enviar assim
