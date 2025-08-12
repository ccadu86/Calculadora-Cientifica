import math # Biblioteca que importa as funçoes de calculos cientificos da calculadora científica
import os
from func import soma, subtracao, multiplicacao, divisao, menu

lista_valores = [] # Para fazer a função "soma" decidi usar uma lista para que o usuário possa somar mais de um valor, por enquanto vazia
Valor = None # Variável que armazenará futuramente os valores inseridos 
valor1 = None # Definir uma variável para inserir 1 valor, já que certas operações tem no max 2 valores a serem inseridos 
Valor2 = None # Definir outro valor
        
print("CALCULADORA CIENTÍFICA")
print()

escolha = menu()

while escolha == 1:
        os.system("cls")
        print("Você escolheu Soma")
        Valor = float(input("Insira um valor: "))
               
        lista_valores.append(Valor)
        sair_continuar = int(input("Selecione 4 para sair ou 1 para continuar: "))
        if sair_continuar == 1:
              print(Valor)
        if sair_continuar == 4:
            os.system("cls")
            print(soma(lista_valores))
            print()
            escolha = menu()


while escolha == 2:
        os.system("cls")
        print("Você escolheu Subratração")
        Valor = float(input("Insira um valor: "))
        lista_valores.append(Valor)
        sair_continuar = int(input("Selecione 4 para sair ou 1 para continuar: "))
        if sair_continuar == 1:
              print(Valor)
        if sair_continuar == 4:
            os.system("cls")
            print(subtracao(lista_valores))
            print()
            escolha = menu()


while escolha == 3: 
        os.system("cls")
        print("Você escolheu multiplicacao")
        Valor = float(input("Insira um valor: "))
        lista_valores.append(Valor)
        sair_continuar = int(input("Selecione 4 para sair ou 1 para continuar: "))
        if sair_continuar == 1:
              print(Valor)
        if sair_continuar == 4:
            os.system("cls")
            print(multiplicacao(lista_valores))
            print()
            escolha = menu()

while escolha == 4:
        os.system("cls")
        print("Você escolheu Divisão")
        valor1 = float(input("Insira o primeiro valor"))
        Valor2 = float(input("Insira o segundo valor"))
        if valor1 == 0 or Valor2 == 0:
               print("Error")
               break
        else:
                print(divisao(valor1,Valor2))
                escolha = menu()

while escolha == 5:
        os.system("cls")
        print("Você escolheu Potenciação")
        potência = float(input("Insira o valor: "))
        expoente = float(input("Insira o expoente: "))
        print(math.pow(potência, expoente)) # Função importada anteriormene que realizará cálculos de potência
        escolha = menu()


while escolha == 6:
        os.system("cls")
        print("Você escolheu Raiz quadrada")
        raiz = float(input("Insira o valor: "))
        if raiz < 0:
               print("ERROR")
        else:
                print(math.sqrt(raiz)) # Função importada anteriormente para realizar cálculos de raíz quadrada
        escolha = menu()

while escolha == 7: 
        os.system("cls")
        print("Você escolheu Fatorial")
        fatorial = int(input("Insira o valor: "))
        if fatorial < 0:
               os.system("cls")
               print("ERROR")
        else:
                os.system("cls")
                print(math.factorial(fatorial)) # Função importada anteriormente (bibblioteca math) para realizar contas de fatorial
        escolha = menu()

while escolha == 8: # Aqui escolhi da opção para usuários fazer operações separadas de cosseno, seno e tangente, ou os 3 ao mesmo tempo, usando as funções ja dadas pela biblioteca math
        os.system("cls")
        print("Você escolheu de cálculo de seno, cosseno e tangente (em graus)")
        Operação = input("Qual operação você deseja realizar?, (escreva Todas, caso queira todas.): ").capitalize()
        if Operação == "Seno":
               print("Seno de um número.")
               seno = float(input("Insira o valor: "))
               rad = math.radians(seno) # converte de radianos para graus
               print(math.sin(seno)) # da o valor do Seno
               escolha = menu()


        if Operação == "Cosseno":
               print("Cosseno de um número.")
               cosseno = float(input("Insira o valor: "))
               rad = math.radians(cosseno) # converte de radianos para graus
               print(math.cos(cosseno)) # da o valor de cosseno
               escolha = menu()


        if Operação == "Tangente":
               print("Tangente de um número.")
               tangente = float(input("Insira o valor: "))
               rad = math.radians(tangente) # converte de radianos para graus
               print(math.tan(tangente)) # da o valor de tangente
               escolha = menu()

         
        if Operação == "Todas":
               print("Seno, cosseno, Tangente de um número.")
               valor = float(input("Insira o valor: "))
               rad = math.radians(valor) # converte de radianos para graus
               print(f"Seno: {math.sin(valor)}") # da o valor do Seno
               print(f"Cosseno: {math.cos(valor)}")# da o valor de cosseno
               print(f"Tangente: {math.tan(valor)}") # da o valor de tangente

               escolha = menu()

while escolha == 9:
        os.system
        print("Você escolheu Logaritimo")
        valor = float(input("Digite um número: "))
        print(f"Logaritmo base 10: {math.log10(valor)}") # função dada da biblioteca math para fazer contas de logaritimo com base 10
        print(f"Logaritmo natural (base e): {math.log(valor)}") # função que faz contas com base e
        escolha = menu()

if escolha == 0:
        os.system("cls")
        print("Você saiu da calculadora ciêntifica!")
        print("Saindo...")
        os.system("Pause")