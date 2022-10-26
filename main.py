"Importando as funções criadas em outros arquivos e a tabela ascii em formato maiúsculo para utilizar na decodificação"
from encripta import codifica
from descripta import decodifica
from string import ascii_uppercase

"criando uma lista com nome alfabeto para utilizar as letras do alfabeto em maiúsculo"
alfabeto = list(ascii_uppercase)
mensagem = "O HALLOWEEN ACONTECE TODO ANO NO DIA TRINTA E UM DE OUTRUBRO E GERALMENTE AS PESSOAS VAO DE FANTASIAS DE TERROR PARA PEDIR DOCES EM CASAS DE ESTRANHO SEMPRE FALANDO SOBRE DOCES OU TRAVESSURAS"
chave = 7
"determinei a mensagem acima e o número de casas a frente como 7 casas a frente para fazer a cifra "

codifica(mensagem, chave)

decodifica(mensagem, chave)
"chamei as funções para fazer a codificação e decodificação"

if __name__ == "__main__":
	codigo = codifica(mensagem, chave)
	print("Mensagem:", mensagem)
	print("Cifra de César:", codigo)
	print("Cifra decodificada:", decodifica(codigo, chave))

"utilizei um if para melhor suporte de finalizar o código, com os prints para mostrar as funções funcinando no sistema."
