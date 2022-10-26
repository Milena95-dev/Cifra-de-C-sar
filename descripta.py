from string import ascii_uppercase
from encripta import codifica
"importa as string uppercase novamente e puxa a função codifica da encripta para utilizar"
alfabeto = list(ascii_uppercase)

def decodifica(mensagem, chave):
    """Recebe uma string com a mensagem codificada e a chave de decodificação e retorna uma mensagem decodificada"""
    return codifica(mensagem, len(alfabeto)-chave)
"a função decodifica retorna a mensagem ao normal somente, mas retransforma a mensagem codificada para normal novamente."
