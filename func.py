def soma (lista_valores): # definindo o parametro da função soma para os valores dentro da lista 
        x = 0 # x representa o resultado que por equanto é 0 
        for item in lista_valores: # Usei o for para percorrer os itens na minha lista
                x += item # adicionando a x um item da lista 
        return x # retorna o valor de x depois

def subtracao (lista_valores): # Def que vai subrtrair os valores 
        x = lista_valores[0] # Usa de uma lista para o usuário adicionar varios valores
        for item in lista_valores[1:]: #[1:]: pega a lista a partir do vetor 1 
                x -= item # Faz com que seja subtraído 1 do item e armazena na variável x
        return x # retona o valor de x

def multiplicacao(lista_valores): # Def de multiplicação
    x = lista_valores[0] # Também usa de uma lista para multiplicar quantos valores o usuário quiser
    for item in lista_valores[1:]: # Começa as operações a partir do vetor 1 
        x *= item # Multiplica os valores de item e armazena eles na variável x
    return x  # Retorna o valor de x

def divisao (valor1, valor2): # Def de divisão
    x = valor1 / valor2 # Os valores definidos anteriormente vão ser divididos um pelo outro 
    return x  # Retorna valor de X 

def menu():
        x = int(input("Escolha a operação desejada por favor: \nDigite 1 para Soma. \nDigite 2 para Substração. \nDigite 3 para Multiplicação. \nDigite 4 para Divisão. \nDigite 5 para potenciação.  \nDigite 6 para Raiz quadrada. \nDigite 7 para Fatorial. \nDigite 8 para cálculo de seno, cosseno e tangente (em graus). \nDigite 9 para Logaritmo (base 10 e base e).\nDigite 0 para Sair. \n--> "))
        return x