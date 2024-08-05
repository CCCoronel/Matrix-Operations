#Escreva seu polígono em Imagem.txt, cada linha é referente a um ponto no plano sendo que

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import json
import math
import os

def PontosDaImagem(NDP):
    i = 1
    matriz = []
    while (i <= NDP):
        x = (float(input('Digite o elemento X do primeiro ponto: ')))
        y = (float(input('Digite o elemento Y do primeiro ponto: ')))
        matriz.append((x,y))
        i += 1
    return matriz

def Options(Imagem):
    #Esta função apresenta as opções de manipulação da imagem, e depois de escolher sua alternativa é redirecionado para a função desejada
    limpatela()
    print("\n[0] Translação\n[1] Contração ou Expansão\n[2] Cizalhamento\n[3] Rotação \n[4] Reflexão\n[5] Criar novo polígono\n[6] Encerrar Programa")
    Escolha = int(input("\nEscolha uma das opções de manipulação: "))
    
    match Escolha:
        case 0:
            Translacao(Imagem)
        case 1:
            ContExp(Imagem)
        case 2:
            Cizalhamento(Imagem)
        case 3:
            Rotacao(Imagem)
        case 4:
            Reflexao(Imagem)
        case 5:
            Imagem = NovoPoligo()
            limpatela()
            Options(Imagem)
        case 6:
            return 0    
 
def limpatela():
    #Função que limpa tela
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def NovoPoligo():
    #Lê o numero de pontos da imagem sugerida0
    NumeroDePontos = int(input('Digite o numero de pontos da sua imagem: '))
    while NumeroDePontos <= 1:
        limpatela()
        print('Digite um numero maior que um')
        NumeroDePontos = int(input('Digite o numero de pontos da sua imagem: '))
    Imagem = PontosDaImagem(NumeroDePontos)
    
    with open('imagem.json','w') as f:
        json.dump(Imagem, f)   

    return Imagem

def Translacao(Imagem):
    #Leitura do vetor que será aplicado na Imagem1
    vetX = int(input('Digite o elemento X do vetor de translação: '))
    vetY = int(input('Digite o elemento Y do vetor de translação: '))
    VetorDeTranslacao = (vetX, vetY)
    Imagem2 = []
    for (i,j) in Imagem:
        x = i + vetX
        y = j + vetY
        Imagem2.append((x,y))
   
   #Criamos aqui nossa figura com os subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    # Primeiro subplot: Imagem
    #Definimos array1 como nossa lista de pontos no gráfico, ele cria uma lista de tuplas e ordena pra serem utilziadas como pontos
    array1 = np.array(Imagem)
    #Formamos a nossa shape (que no caso será sempre poligonos para esse trabalho) e também definimos suas propriedades (como cor e preenchimento de cor)
    shape1 = Polygon(array1, color="DarkBlue", fill=True)
    ax[0].add_patch(shape1)
    ax[0].set_xlim(-50, 50)
    ax[0].set_ylim(-50, 50)
    ax[0].set_aspect('equal', adjustable='box')
    
    # Segundo subplot: Imagem Translocada
    # Aqui definimos a estrutura da imagem 2, da mesma forma que foi feita a Imagem 1
    array2 = np.array(Imagem2)
    shape2 = Polygon(array2, color = "DarkRed", fill=True)
    #Adicionamos a nossa forma no ax da coluna 2 e definimos o limite da box para (-50, 50)
    ax[1].add_patch(shape2)
    ax[1].set_xlim(-50, 50)
    ax[1].set_ylim(-50, 50)
    ax[1].set_aspect('equal', adjustable='box')
    plt.show()
    Options(Imagem)

def ContExp(Imagem):
    limpatela()
    
    print('Explicação do funcionamento da função: você irá digitar um número maior do que zero, se este numero\nfor maior do que 1 a imagem será expandida, se for entre 0 e 1 a imagem será contraida.')
    k = None
    sacanagemcount = 0
    
    #Leitor do valor K
    while (k <= 0):
        k = float(input('Digite um numero maior do que zero: '))
        if (k <=0) and (sacanagemcount != 2):
            limpatela()
            print('Por favor, um numero maior do que zero')
        sacanagemcount += 1
        if sacanagemcount == 3:
            limpatela()
            print('Você ta de sacanagem comigo não ta?')

    Imagem2 = []
    
    # Looping que monta a Imagem2
    for (x, y) in Imagem:
        novo_x = k * x
        novo_y = k * y
        Imagem2.append((novo_x, novo_y))
    
    #Definimos array1 como nossa lista de pontos no gráfico, ele cria uma lista de tuplas e ordena pra serem utilziadas como pontos
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Primeiro subplot: Imagem
    #Definimos array1 como nossa lista de pontos no gráfico
    array1 = np.array(Imagem)
    #Formamos a nossa shape (que no caso será sempre poligonos para esse trabalho) e também definimos suas propriedades (como cor e preenchimento de cor)
    shape1 = Polygon(array1, color="DarkBlue", fill=True)
    ax[0].add_patch(shape1)
    ax[0].set_xlim(-50, 50)
    ax[0].set_ylim(-50, 50)
    ax[0].set_aspect('equal', adjustable='box')

    # Segundo subplot: Imagem Expandida ou Encolhida
    array2 = np.array(Imagem2)
    shape2 = Polygon(array2, color = "DarkRed", fill=True)
    ax[1].add_patch(shape2)
    ax[1].set_xlim(-50, 50)
    ax[1].set_ylim(-50, 50)
    ax[1].set_aspect('equal', adjustable='box')
    plt.show()
    Options(Imagem)

def Cizalhamento(Imagem):
    print('Um cizalhamento é a contorção da imagem, e pode ser realizado de maneira vertical ou horizontal \n [0] Vertical \n [1] Horizontal \n')
    Opcao = float(input('Escolha uma opção: '))
    Imagem2 = []
    k = None
    

    if Opcao == 0 or Opcao == 1:
        if Opcao == 0:
            matriz = [[1, 0],['k',1]]
        else:
            matriz = [[1,'k'],[0,1]]
        print(f'O Cizalhamento é feito multiplicando os pontos pela matriz {matriz}')
        k = float(input('Digite o valor de K: '))
        if Opcao == 0:
            for (x,y) in Imagem:
                Imagem2.append((x, (k*x +y)))
        print (Imagem2)
        if Opcao == 1:
            for (x,y) in Imagem:
                Imagem2.append(((k*y+x), y))
        print (Imagem2)
    else:
        limpatela()
        print('Escolha uma oção válida')
        Cizalhamento(Imagem)

     #Novamente criando os subplots (Para criar a mesma imagem eu vou usar o mesmo código sempre)
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Primeiro subplot: Imagem
    #Definimos array1 como nossa lista de pontos no gráfico, ele cria uma lista de tuplas e ordena pra serem utilziadas como pontos
    array1 = np.array(Imagem)
    #Formamos a nossa shape (que no caso será sempre poligonos para esse trabalho) e também definimos suas propriedades (como cor e preenchimento de cor)
    shape1 = Polygon(array1, color="DarkBlue", fill=True)
    ax[0].add_patch(shape1)
    ax[0].set_xlim(-50, 50)
    ax[0].set_ylim(-50, 50)
    ax[0].set_aspect('equal', adjustable='box')

    # Segundo subplot: Imagem Expandida ou Encolhida
    array2 = np.array(Imagem2)
    shape2 = Polygon(array2, color = "DarkRed", fill=True)
    ax[1].add_patch(shape2)
    ax[1].set_xlim(-50, 50)
    ax[1].set_ylim(-50, 50)
    ax[1].set_aspect('equal', adjustable='box')
    plt.show()
    Options(Imagem)

def Rotacao(Imagem):
    #Nessa função do trabalho, utilizaremos a biblioteca math pra calculos de Seno e Cosseno
    Angulo = math.radians(float(input('Digite um ângulo: ')))
    holderMatrix = [[math.cos(Angulo), -math.sin(Angulo)],[math.sin(Angulo), math.cos(Angulo)]]
    
    Imagem2 = []
    for (x, y) in Imagem:
        novo_x = x * holderMatrix[0][0] + y * holderMatrix[0][1]
        novo_y = x * holderMatrix[1][0] + y * holderMatrix[1][1]
        Imagem2.append((novo_x, novo_y))

    # Criamos aqui nossa figura com os subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Primeiro subplot: Imagem original
    array1 = np.array(Imagem)
    shape1 = Polygon(array1, color="DarkBlue", fill=True)
    ax[0].add_patch(shape1)
    ax[0].set_xlim(-50, 50)
    ax[0].set_ylim(-50, 50)
    ax[0].set_aspect('equal', adjustable='box')

    # Segundo subplot: Imagem rotacionada
    array2 = np.array(Imagem2)
    shape2 = Polygon(array2, color="DarkRed", fill=True)
    ax[1].add_patch(shape2)
    ax[1].set_xlim(-50, 50)
    ax[1].set_ylim(-50, 50)
    ax[1].set_aspect('equal', adjustable='box')

    plt.show()
    Options(Imagem)

def Reflexao(Imagem):
    B = 5
    print("Para refletir a imagem, selecione uma das opções abaixo\n[0] Reflexão no eixo X\n[1] Reflexão no eixo Y\n[2] Reflexão em relação ao eixo y = x\n[3] Reflexão em relação ao eixo y = -x\n[4] Reflexão em relação a origem")
    while (B < 0 or B > 4):
        B = int(input("Escolha uma opção: "))
        if (B < 0 or B > 4):
            limpatela()
            print ("Digite uma oção válida")
            Reflexao(Imagem)

    match B:
        case 0:
            B = [[1, 0],[0,-1]]
        case 1:
            B = [[-1, 0],[0,1]]
        case 2:
            B = [[0, 1],[1,0]]
        case 3:
            B = [[0, -1],[-1,0]]
        case 4:
            B = [[-1, 0],[0,-1]]
        
    Imagem2 = []
    
    for (x,y) in Imagem:
        novo_x = x * B[0][0] + y * B[0][1]
        novo_y = x * B[1][0] + y * B[1][1]
        Imagem2.append((novo_x, novo_y))

    # Criamos aqui nossa figura com os subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Primeiro subplot: Imagem original
    array1 = np.array(Imagem)
    shape1 = Polygon(array1, color="DarkBlue", fill=True)
    ax[0].add_patch(shape1)
    ax[0].set_xlim(-50, 50)
    ax[0].set_ylim(-50, 50)
    ax[0].set_aspect('equal', adjustable='box')

    # Segundo subplot: Imagem rotacionada
    array2 = np.array(Imagem2)
    shape2 = Polygon(array2, color="DarkRed", fill=True)
    ax[1].add_patch(shape2)
    ax[1].set_xlim(-50, 50)
    ax[1].set_ylim(-50, 50)
    ax[1].set_aspect('equal', adjustable='box')

    plt.show()
    Options(Imagem)

def ColetarImagemPorArquivo():
    with open('imagem.json','r') as f:
        Imagem = json.load(f) 
    
    return Imagem

def main():
    #Primeiro é necessário criar uma imagem base, utilizaremos poligonos para realização deste trabalho
    Imagem = NovoPoligo()
    Options(Imagem)
    Imagem = ColetarImagemPorArquivo()
    #Chamada da função Options
    
if __name__ == '__main__':
    main()
