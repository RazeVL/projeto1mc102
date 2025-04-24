# Nome completo do primeiro membro: [Aluno que fez a entrega]
# RA do primeiro membro: [Aluno que fez a entrega]
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

WORDS = load_words()   # Carrega a lista de palavras

def player(guess_hist, res_hist):
    

    if 
    else




    global WORDS
    guess = random.choice(WORDS) 
    
    return guess 
