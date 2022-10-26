"transformará a string em maiúsculo do ASCII para ser melhor de trabalhar a cifra de César"
from string import ascii_uppercase

alfabeto = list(ascii_uppercase)

def codifica(mensagem, chave):
    """Receberá uma string com a mensagem e uma chave de codificação e retornará uma mensagem com a cifra"""
    cifra = ""
    for letra in mensagem:
        indice = ord(letra)-65
        cifra+= alfabeto[(indice+chave) % len(alfabeto)] if letra in alfabeto else letra
    return cifra

"Cifra por enquanto zerada apenas para chamar a função, um for para pegar cada letra no texto em si, indice com função de ordenar retornando um número inteiro como referência"
"para transformar em letra pelo UNICODE, e concatenando a variável cifra com a lista alfabeto (utilizando o indice e adicionando a chave (que será o total de casas a mais) "
"ao cálculo, e ainda retornando o resto de uma divisão entre dois números, finalizando com uma condicional para caso a letra não conste na ascii retornar como ela mesma.  "