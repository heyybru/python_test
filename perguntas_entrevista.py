'''
1. Escreva uma função chamadareverse_string que:
- toma uma palavra como argumento;
- inverte usando reversed() e ''.join();
- retorna a palavra invertida.
'''

# Função que inverte uma string
def reverse_string(word):
    return ''.join(reversed(word))


# Teste. Verificação da função reverse_string
def test_reverse_string():
    input_str = "TripleTen"

    # Realize a operação inversa
    reversed_str = reverse_string(input_str)

    # Verifique se a string invertida corresponde ao resultado esperado
    assert reversed_str == "neTelpirT"

    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)


"""
2. Escreva a função que verifica se uma palavra é um palíndromo 
- Defina uma função de teste;
- Defina uma string de entrada atribuindo a ela o palíndromo conhecido “osso”;
- Chame a função is_palindrome com input_str como argumento. Armazene o resultado na variável result;
- Adicione uma asserção para verificar se o resultado da função identifica corretamente a entrada como um palíndromo;
- Adicione uma instrução print que confirme que o teste foi bem-sucedido, deixando claro que a string de entrada foi corretamente identificada como um palíndromo.
"""

# Função para verificar palíndromo
def is_palindrome(word):
    # Inverta a string usando reversed() e join().
    reversed_str = ''.join(reversed(word))
    return word == reversed_str


# Teste. Verificação da função is_palindrome
def test_is_palindrome():
    # Defina a string de entrada
    input_str = "osso"

    # Execute a verificação do palíndromo
    result = is_palindrome(input_str)

    # Verifique se o resultado é True (verdadeiro) para um palíndromo
    assert result == True

    print("Teste aprovado! '" + input_str + "' é um palíndromo.")

# 3. Escreva uma função que calcule o fatorial de um número

# Importe o módulo matemático para acessar funções matemáticas
import math


def compute_factorial(number):
    # Calcule o fatorial de "number" usando a função fatorial interna do Python no módulo math.
    return math.factorial(number)


# Teste. Verificação da função compute_factorial
def test_compute_factorial():
    # Defina o número de entrada
    input_number = 5

    # Realize o cálculo fatorial
    result = compute_factorial(input_number)

    # Verifique se o resultado é igual ao valor fatorial esperado
    assert result == 120

    print("Teste aprovado! O fatorial de " + str(input_number) + " é " + str(result))


