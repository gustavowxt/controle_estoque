"""
***Programa de cadastro e controle de estoque de uma empresa***

Funções:
*Cadastrar produtos que entrarão no estoque
*Alterar produtos cadastrados no estoque
*Excluir produtos cadastrados no estoque
*Consultar produtos cadastrados no estoque
*Registrar entrada de produtos no estoque
*Registrar saída de produtos no estoque
*Saldo de estoque unitário no estoque
*Análise total de estoque

Obs: Este programa é apenas protótipo.
"""


print("SEJA BEM VINDO AO PROGRAMA DE CONTROLE DE ESTOQUE\n")


#-Variáveis necessárias-#

variavel_escolha = 0
exibir_produto_codigo = 0
menu_principal = 0
menu_cadastrar_produto = 0
menu_controle_produto = 0
quantidade_produto_antiga = 0
quantidade_produto_entrada = 0
quantidade_produto_saida = 0
valor_venda_produto_antiga = 0
lucro_obtido_total = 0


#-Funções-#

    #Conseguir printar dados
def printar_dados():
    printar = "------------------------\n\n"
    print("\n------------------------")
    print("Cód.:", codigo_produto_lista[exibir_produto_codigo])
    print("Nome:", nome_produto_lista[exibir_produto_codigo])
    print("Quantidade:", quantidade_produto_lista[exibir_produto_codigo])
    print("Modelo: ", modelo_produto_lista[exibir_produto_codigo])
    print("Fabricante: ", fabricante_produto_lista[exibir_produto_codigo])
    print("Valor de custo:", valor_custo_produto_lista[exibir_produto_codigo])
    print("Valor de venda:", valor_venda_produto_lista[exibir_produto_codigo])
    return printar

    #Função para nenhum produto cadastrado
def nenhum_produto_cadastrado():
    if nome_produto_lista == []:
        print_para_n_none = print ("Nenhum produto cadastrado")
    return print_para_n_none
    
    

#-Listas de produto-#
nome_produto_lista = []

codigo_produto_lista = []

quantidade_produto_lista = []
quantidade_produto_antiga_lista = []
quantidade_produto_saida_lista = []
quantidade_produto_entrada_lista = []

modelo_produto_lista = []

fabricante_produto_lista = []

valor_custo_produto_lista = []
valor_custo_produto_antiga_lista = []

valor_venda_produto_lista = []
valor_venda_produto_antiga_lista = []





    
#laço de repetição do menu
while True:
    print("------------------------")
    menu_principal = (input("1. Cadastrar produto\n2. Consultar produto\n3. Controle de estoque\n4. Sair\n-->"))
    print("\n------------------------")



#   #Menu de cadastro #condições para a escolha do menu do usuário #1
    if(menu_principal == "1"):
        while True:
            menu_cadastrar_produto = (input("1. Cadastrar novo produto\n2. Alterar produto\n3. Remover produto\n4. Retornar ao Menu Inicial\n-->"))
            print("\n")

            
#   #   #Menu para cadastrar um novo produto #1.1
            if (menu_cadastrar_produto == "1"):
                
                while True:

                    if (len(nome_produto_lista)) == 10000:
                        print("---------------------------------------")
                        print("Capacidade máxima de produtos excedida!")
                        print("---------------------------------------")
                        break
                    
                    while True:
                        #Cadastrar nome do produto
                        print("-------------------------")
                        nome_produto_digitado = input("Digite o nome do produto: ")

                        #Se o usuário digitar nome vazio
                        if(nome_produto_digitado == ""):
                            print("\n--------------")
                            print("Nome inválido!")
                            print("--------------\n")

                        #Se produto ja estiver condito na lista
                        elif (nome_produto_digitado in nome_produto_lista):
                            print("\n------------------------------------")
                            print("Nome ja cadastrado, tente novamente!")
                            print("------------------------------------\n")

                        #Verificar se há somente letras
                        else:
                            for i in range(len(nome_produto_digitado)):
                                         
                                if (ord(nome_produto_digitado[i])) in range(65,91) or (ord(nome_produto_digitado[i])) in range(97,123) or ord(nome_produto_digitado[i]) == 45 or ord(nome_produto_digitado[i]) == 231 or ord(nome_produto_digitado[i]) == 32:
                                    continue

                                else:                                   
                                    print("\n-----------------------------------------------")
                                    print("Nome do produto só pode conter letras ou hífens")
                                    print("-----------------------------------------------\n")
                                    break

                        #condição para avançar pra proxima etapa
                            if (ord(nome_produto_digitado[i])) in range(65,91) or (ord(nome_produto_digitado[i])) in range(97,123) or ord(nome_produto_digitado[i]) == 45 or ord(nome_produto_digitado[i]) == 231 or ord(nome_produto_digitado[i]) == 32:
                                break
                                                            
                                     
                    #Adicionar nome do produto na lista
                    nome_produto_lista.append(nome_produto_digitado)
                        
                
                    #Cadastrar quantidade de um produto a uma lista.
                    while True:
                        quantidade_produto_digitado = (input("Digite a quantidade do produto: "))

                        #Se o usuário digitar nome vazio
                        if(quantidade_produto_digitado == ""):
                            print("\n-------------------")
                            print("Quantidade inválida!")
                            print("-------------------\n")

                        
                        #Verificar se há somente numeros
                        else:
                            for i in range(len(quantidade_produto_digitado)):
                                         
                                if (ord(quantidade_produto_digitado[i])) in range(48,58):
                                    continue

                                else:                                   
                                    print("\n--------------------------------------------")
                                    print("Quantidade do produto só pode conter números")
                                    print("--------------------------------------------\n")
                                    break
                            

                            #condição para avançar pra proxima etapa
                            if (ord(quantidade_produto_digitado[i])) in range(48,58):

                                int(quantidade_produto_digitado)
                                break

                    #Adicionar quantidade a lista             
                    quantidade_produto_lista.append(quantidade_produto_digitado)
                            
                    quantidade_produto_antiga = quantidade_produto_digitado
                    quantidade_produto_antiga_lista.append(quantidade_produto_antiga)

                            
                    #Acicionar o modelo do produto a uma lista
                    while True:
                        modelo_produto_digitado = (input("Digite o modelo do produto: "))

                        if(modelo_produto_digitado == ""):
                            print("\n----------------")
                            print("Modelo inválido!")
                            print("----------------\n")
                        else:
                            modelo_produto_lista.append(modelo_produto_digitado)
                            break

                    #Acicionar o modelo do produto a uma lista
                    while True:
                        fabricante_produto_digitado = (input("Digite o fabricante do produto: "))

                        if(fabricante_produto_digitado == ""):
                            print("\n--------------------")
                            print("Fabricante inválido!")
                            print("--------------------\n")
                        else:
                            fabricante_produto_lista.append(fabricante_produto_digitado)
                            break
                    

                    #Adicionar o valor de custo de um produto a uma lista.                        
                    while True:
                        valor_custo_produto_digitado = (input("Digite o valor de custo do produto: "))

                        #Se o usuário digitar nome vazio
                        if(valor_custo_produto_digitado == ""):
                            print("\n---------------")
                            print("Valor inválido!")
                            print("---------------\n")
    

                        
                        #Verificar se há somente numeros
                        else:
                            for i in range(len(valor_custo_produto_digitado)):
                                         
                                if (ord(valor_custo_produto_digitado[i])) in range(48,58) or (ord(valor_custo_produto_digitado[i])) == 46:
                                    continue
                                else:
                                    print("\n---------------")
                                    print("valor inválido!")
                                    print("---------------\n")
                                    break
                          

                            #condição para avançar pra proxima etapa
                            if (ord(valor_custo_produto_digitado[i])) in range(48,58):

                                float(valor_custo_produto_digitado)
                                break
                            
                            if (ord(valor_custo_produto_digitado[i])) in range(46,47):

                                float(valor_custo_produto_digitado)
                                break
                          
                            
                    valor_custo_produto_lista.append(valor_custo_produto_digitado)
                    
                    valor_custo_produto_antiga = valor_custo_produto_digitado
                    valor_custo_produto_antiga_lista.append(valor_custo_produto_antiga)
                    

                    #Adicionar o valor de venda de um produto a uma lista.
                    while True:
                        valor_venda_produto_digitado = (input("Digite o valor de venda do produto: "))

                        #Se o usuário digitar nome vazio
                        if(valor_venda_produto_digitado == ""):
                            print("\n---------------")
                            print("Valor inválido!")
                            print("---------------\n")

                        
                        #Verificar se há somente numeros
                        else:
                            for i in range(len(valor_venda_produto_digitado)):
                                         
                                if (ord(valor_venda_produto_digitado[i])) in range(48,58) or (ord(valor_venda_produto_digitado[i])) == 46:
                                    continue
                                else:
                                    print("\n---------------")
                                    print("valor inválido!")
                                    print("---------------\n")
                                    break
                          

                            #condição para avançar pra proxima etapa
                            if (ord(valor_venda_produto_digitado[i])) in range(48,58):

                                float(valor_venda_produto_digitado)
                                break
                            
                            if (ord(valor_venda_produto_digitado[i])) in range(46,47):

                                float(valor_venda_produto_digitado)
                                break
                            
                    valor_venda_produto_lista.append(valor_venda_produto_digitado)
                    
                    valor_venda_produto_antiga = valor_venda_produto_digitado
                    valor_venda_produto_antiga_lista.append(valor_venda_produto_antiga)
                    

                    #Adicionar o código do produto em uma lista
                    codigo_produto_lista.append((len(codigo_produto_lista)))


                    #Menssagem de exito
                    print("\n-------------------------------")
                    print("Produto cadastrado com sucesso!")
                    print("-------------------------------\n")

                    break

#   #   #Menu para alterar um produto #1.2
            elif (menu_cadastrar_produto == "2"): 

                #Quando não há nenhum produto cadastrado               
                if (nome_produto_lista == []):
                    print("\n-------------------------")
                    print("Nenhum produto cadastrado")
                    print("-------------------------\n")

                

                #Listar produtos cadastrados
                else:                    
                    while True:
                        print("Lista de produtos cadastrados")
                        for i in range(len(codigo_produto_lista)):            
                            print(codigo_produto_lista[i]," --- ",nome_produto_lista[i])
                        print("\n\n")

                        
                        exibir_produto_codigo = int(input("Digite o código do produto: "))
                       
                                 
                        #Se o usuário digitar valor vazio 
                        if (exibir_produto_codigo == ""):
                            print("\n-----------------------------------------")
                            print ("Valor vazio! Por favor digite novamente!")
                            print("-----------------------------------------\n")

                                                    
                        #Se o que foi digitado não estiver contido na lista 
                        elif (exibir_produto_codigo not in codigo_produto_lista):
                            print("\n-----------------------------------------")
                            print ("Valor invalido ou produto não cadastrado!")
                            print("-----------------------------------------\n")                  
                                                   
                        #Printar dados especificos do produto
                        else:
                            print(printar_dados())
                            print("Deseja alterar os dados exibidos?")
                            variavel_escolha = (input("1. Sim\n2. Não\n-->"))

                            while True:

#   #   #   #Condição de seguraça para alterar o produto #1.2.1
                                if (variavel_escolha == "1"): 

                                    #Excluir o indice especifico do produto digitado
                                    nome_produto_lista.pop(exibir_produto_codigo)                
                                    quantidade_produto_lista.pop(exibir_produto_codigo)
                                    modelo_produto_lista.pop(exibir_produto_codigo)
                                    fabricante_produto_lista.pop(exibir_produto_codigo)
                                    valor_custo_produto_lista.pop(exibir_produto_codigo)
                                    valor_venda_produto_lista.pop(exibir_produto_codigo)
                                    codigo_produto_lista.pop(exibir_produto_codigo)
                                    
                                    #Alterar nome do produto na lista
                                    while True:
                                        #Cadastrar nome do produto
                                        print("-------------------------")
                                        nome_produto_digitado = input("Digite o nome do produto: ")

                                        #Se o usuário digitar nome vazio
                                        if(nome_produto_digitado == ""):
                                            print("\n--------------")
                                            print("Nome inválido!")
                                            print("--------------\n")

                                        #Se produto ja estiver condito na lista
                                        elif (nome_produto_digitado in nome_produto_lista):
                                            print("\n------------------------------------")
                                            print("Nome ja cadastrado, tente novamente!")
                                            print("------------------------------------\n")

                                        #Verificar se há somente letras
                                        else:
                                            for i in range(len(nome_produto_digitado)):
                                                         
                                                if (ord(nome_produto_digitado[i])) in range(65,91) or (ord(nome_produto_digitado[i])) in range(97,123) or ord(nome_produto_digitado[i]) == 45 or ord(nome_produto_digitado[i]) == 231:
                                                    continue

                                                else:                                   
                                                    print("\n--------------------------------------------")
                                                    print("Nome do produto só pode conter letras hífens")
                                                    print("--------------------------------------------\n")
                                                    break

                                        #condição para avançar pra proxima etapa
                                            if (ord(nome_produto_digitado[i])) in range(65,91) or (ord(nome_produto_digitado[i])) in range(97,123) or ord(nome_produto_digitado[i]) == 45 or ord(nome_produto_digitado[i]) == 231:
                                                break
                                                                            
                                                     
                                    #Adicionar nome do produto na lista
                                    nome_produto_lista.insert(exibir_produto_codigo,nome_produto_digitado)
                                        
                                
                                    #Cadastrar quantidade de um produto a uma lista.
                                    while True:
                                        quantidade_produto_digitado = (input("Digite a quantidade do produto: "))

                                        #Se o usuário digitar nome vazio
                                        if(quantidade_produto_digitado == ""):
                                            print("\n-------------------")
                                            print("Quantidade inválida!")
                                            print("-------------------\n")

                                        
                                        #Verificar se há somente numeros
                                        else:
                                            for i in range(len(quantidade_produto_digitado)):
                                                         
                                                if (ord(quantidade_produto_digitado[i])) in range(48,58):
                                                    continue

                                                else:                                   
                                                    print("\n--------------------------------------------")
                                                    print("Quantidade do produto só pode conter números")
                                                    print("--------------------------------------------\n")
                                                    break
                                            

                                            #condição para avançar pra proxima etapa
                                            if (ord(quantidade_produto_digitado[i])) in range(48,58):

                                                int(quantidade_produto_digitado)
                                                break

                                    #Adicionar quantidade a lista             
                                    quantidade_produto_lista.insert(exibir_produto_codigo,quantidade_produto_digitado)
                                            
                                    quantidade_produto_antiga = quantidade_produto_digitado
                                    quantidade_produto_antiga_lista.insert(exibir_produto_codigo,quantidade_produto_antiga)

                                            
                                    #Acicionar o modelo do produto a uma lista
                                    
                                    modelo_produto_digitado = (input("Digite o modelo do produto: "))
                                    modelo_produto_lista.insert(exibir_produto_codigo,modelo_produto_digitado)

                                    #Acicionar o modelo do produto a uma lista
                                    
                                    fabricante_produto_digitado = (input("Digite o fabricante do produto: "))
                                    fabricante_produto_lista.insert(exibir_produto_codigo,fabricante_produto_digitado)
                                    

                                    #Adicionar o valor de custo de um produto a uma lista.                        
                                    while True:
                                        valor_custo_produto_digitado = (input("Digite o valor de custo do produto: "))

                                        #Se o usuário digitar nome vazio
                                        if(valor_custo_produto_digitado == ""):
                                            print("\n---------------")
                                            print("Valor inválido!")
                                            print("---------------\n")
                    

                                        
                                        #Verificar se há somente numeros
                                        else:
                                            for i in range(len(valor_custo_produto_digitado)):
                                                         
                                                if (ord(valor_custo_produto_digitado[i])) in range(48,58) or (ord(valor_custo_produto_digitado[i])) == 46:
                                                    continue
                                                else:
                                                    print("\n---------------")
                                                    print("valor inválido!")
                                                    print("---------------\n")
                                                    break
                                          

                                            #condição para avançar pra proxima etapa
                                            if (ord(valor_custo_produto_digitado[i])) in range(48,58):

                                                float(valor_custo_produto_digitado)
                                                break
                                            
                                            if (ord(valor_custo_produto_digitado[i])) in range(46,47):

                                                float(valor_custo_produto_digitado)
                                                break
                                          
                                            
                                    valor_custo_produto_lista.insert(exibir_produto_codigo,valor_custo_produto_digitado)
                                    
                                    valor_custo_produto_antiga = valor_custo_produto_digitado
                                    valor_custo_produto_antiga_lista.insert(exibir_produto_codigo,valor_custo_produto_antiga)
                                    

                                    #Adicionar o valor de venda de um produto a uma lista.
                                    while True:
                                        valor_venda_produto_digitado = (input("Digite o valor de venda do produto: "))

                                        #Se o usuário digitar nome vazio
                                        if(valor_venda_produto_digitado == ""):
                                            print("\n---------------")
                                            print("Valor inválido!")
                                            print("---------------\n")

                                        
                                        #Verificar se há somente numeros
                                        else:
                                            for i in range(len(valor_venda_produto_digitado)):
                                                         
                                                if (ord(valor_venda_produto_digitado[i])) in range(48,58) or (ord(valor_venda_produto_digitado[i])) == 46:
                                                    continue
                                                else:
                                                    print("\n---------------")
                                                    print("valor inválido!")
                                                    print("---------------\n")
                                                    break
                                          

                                            #condição para avançar pra proxima etapa
                                            if (ord(valor_venda_produto_digitado[i])) in range(48,58):

                                                float(valor_venda_produto_digitado)
                                                break
                                            
                                            if (ord(valor_venda_produto_digitado[i])) in range(46,47):

                                                float(valor_venda_produto_digitado)
                                                break
                                            
                                    valor_venda_produto_lista.insert(exibir_produto_codigo,valor_venda_produto_digitado)
                                    
                                    valor_venda_produto_antiga = valor_venda_produto_digitado
                                    valor_venda_produto_antiga_lista.insert(exibir_produto_codigo, valor_venda_produto_antiga)
                                    

                                    #Adicionar o código do produto em uma lista
                                    codigo_produto_lista.insert(exibir_produto_codigo,exibir_produto_codigo)


                                    #Menssagem de exito
                                    print("\n-------------------------------")
                                    print("Produto alterado com sucesso!")
                                    print("-------------------------------\n")

                                    break
                                break
                            break
                            


#   #   #Remover produto cadastrado  #1.3
            elif (menu_cadastrar_produto == "3"):

                #Quando não há nenhum produto cadastrado 
                if (nome_produto_lista == []):
                    print("\n-------------------------")
                    print("Nenhum produto cadastrado")
                    print("-------------------------\n")

                #Listar produtos cadastrados
                else:
                    while True:

                        #For que printar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(codigo_produto_lista)):            
                            print(codigo_produto_lista[i]," --- ",nome_produto_lista[i])
                        print("\n\n")
                    
                        exibir_produto_codigo = int(input("Digite o código do produto: "))

                        #Valor não contido dentro da lista de codigos
                        if exibir_produto_codigo not in codigo_produto_lista:
                            print("\n-----------------------------------------")
                            print("Valor invalido ou produto não cadastrado")
                            print("-----------------------------------------\n")                           
                        
                        else:
                            #Printar dados especificos do produto
                            print(printar_dados())
                            print("Deseja excluir os dados exibidos?")
                            variavel_escolha = (input("1. Sim\n2. Não\n-->"))

                            

                            #Condição de seguraça para excluir o produto #1.3.1
                            if(variavel_escolha == "1"):

                                #Excluir o indice especifico do produto digitado
                                nome_produto_lista.pop(exibir_produto_codigo)                
                                quantidade_produto_lista.pop(exibir_produto_codigo)
                                modelo_produto_lista.pop(exibir_produto_codigo)
                                fabricante_produto_lista.pop(exibir_produto_codigo)
                                valor_custo_produto_lista.pop(exibir_produto_codigo)
                                valor_venda_produto_lista.pop(exibir_produto_codigo)
                                codigo_produto_lista.pop(exibir_produto_codigo)
                                
                                
                                
                                #Menssagem de exito
                                print("\n-----------------------------")
                                print("Produto excluido com sucesso!")
                                print("-----------------------------\n")
                                break

                            #Não excluir o produto
                            elif(variavel_escolha == "2"):
                                print("-----------------------------\n")
                                break

                            #Se o usuário digitar valor vazio
                            elif(variavel_escolha == ""):
                                print("\n-----------------------------------------")
                                print ("Valor invalido ou produto não cadastrado")
                                print("-----------------------------------------\n")                                

                            #Se o usuário digitar caracter invalidos
                            else:
                                print("\n-----------------------------------------")
                                print ("Valor invalido ou produto não cadastrado")
                                print("-----------------------------------------\n")
                    break
                
                            
#   #   #Retornar ao menu principal #1.4
            elif (menu_cadastrar_produto == "4"):
                menu_cadastrar_produto = 0
                break

#   #   #Condição caso o usuario digite um numero errado
            else:
                print("\n------------------------")
                print("O número ou caracter digitado é inválido.")
                print("Por favor, tente novamente.")
                print("------------------------\n")
            
            

#   #Consultar um produto #2    
    elif(menu_principal == "2"):
        while True:
            if (nome_produto_lista == []):
                print("\n-------------------------")
                print("Nenhum produto cadastrado")
                print("-------------------------\n")
                    
            else:
                while True:
                    
                    print("Lista de produtos cadastrados")
                    for i in range(len(codigo_produto_lista)):            
                        print(codigo_produto_lista[i]," --- ",nome_produto_lista[i])
                    print("\n\n")

                    exibir_produto_codigo = int(input("Digite o código do produto: "))

                    if (exibir_produto_codigo not in codigo_produto_lista):
                        print("\n-----------------------------------------")
                        print("Valor invalido ou produto não cadastrado")
                        print("-----------------------------------------\n")

                    else:
                        
                        print(printar_dados())
                    break
                        
            break

                        




#   #Controlar estoque #3
    elif(menu_principal == "3"):
        while True:
            print("--------------------------------")
            menu_controle_produto = input("1. Registrar entrada de produtos\n2. Registrar saída de produtos\n3. Saldo de estoque unitário\n4. Análise total de estoque\n5. Voltar ao menu principal\n-->")

#   #   #   #Registrar entrada de produtos #3.1
            if (menu_controle_produto == "1"):
                if (nome_produto_lista == []):
                    print("\n-------------------------")
                    print("Nenhum produto cadastrado")
                    print("-------------------------\n")

                #Listar produtos cadastrados
                else:
                    while True:

                        #For que printar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(codigo_produto_lista)):            
                            print(codigo_produto_lista[i]," --- ",nome_produto_lista[i])
                        print("\n\n")
                    
                        exibir_produto_codigo = int(input("Digite o código do produto: "))

                        #Valor não contido dentro da lista de codigos
                        if exibir_produto_codigo not in codigo_produto_lista:
                            print("\n-----------------------------------------")
                            print("Valor invalido ou produto não cadastrado")
                            print("-----------------------------------------\n")                           
                        
                        else:
                            #Printar dados especificos do produto
                            print(printar_dados())
                            print("Deseja alterar a quantidade de produto exibido?")
                            variavel_escolha = (input("1. Sim\n2. Não\n-->"))

                            

                            #Condição de seguraça para excluir o produto
                            if(variavel_escolha == "1"):

                                #Alterar oa quantia do produto digitado                                                
                                quantidade_adicionada = int(input("Digite a quantidade que deseja registrar: "))
                                quantidade_nova = int(quantidade_produto_lista[exibir_produto_codigo]) + quantidade_adicionada
                                
                                quantidade_produto_lista.pop(exibir_produto_codigo)
                                quantidade_produto_lista.insert(exibir_produto_codigo, quantidade_nova)

                                quantidade_produto_entrada += quantidade_adicionada 
                                quantidade_produto_entrada_lista.insert(exibir_produto_codigo, quantidade_produto_entrada)

                                
                                #Menssagem de exito
                                print("\n----------------------------------")
                                print("Quantidade registrada com sucesso!")
                                print("----------------------------------\n")
                                break

                            #Não excluir o produto
                            elif(variavel_escolha == "2"):
                                print("-----------------------------\n")
                                break

                            #Se o usuário digitar valor vazio
                            elif(variavel_escolha == ""):
                                print("\n-----------------------------------------")
                                print("Valor invalido ou produto não cadastrado")
                                print("-----------------------------------------\n")                                

                            #Se o usuário digitar caracter invalidos
                            else:
                                print("\n-----------------------------------------")
                                print ("Valor invalido ou produto não cadastrado")
                                print("-----------------------------------------\n")
                    break
                
                
#   #   #   #Registrar saída de produtos #3.2

            elif (menu_controle_produto == "2"):
                if (nome_produto_lista == []):
                    print("\n-------------------------")
                    print("Nenhum produto cadastrado")
                    print("-------------------------\n")

                #Listar produtos cadastrados
                else:
                    while True:

                        #For que printar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(codigo_produto_lista)):            
                            print(codigo_produto_lista[i]," --- ",nome_produto_lista[i])
                        print("\n\n")
                    
                        exibir_produto_codigo = int(input("Digite o código do produto: "))

                        #Valor não contido dentro da lista de codigos
                        if exibir_produto_codigo not in codigo_produto_lista:
                            print("\n-----------------------------------------")
                            print("Valor invalido ou produto não cadastrado")
                            print("-----------------------------------------\n")                           
                        
                        else:
                            #Printar dados especificos do produto
                            print(printar_dados())
                            print("Deseja alterar a quantidade de produto exibido?")
                            variavel_escolha = (input("1. Sim\n2. Não\n-->"))

                            

                            #Condição de seguraça para excluir o produto
                            if(variavel_escolha == "1"):

                                #Alterar a quantia do produto digitado
                                print("\n---------------------------------------")
                                quantidade_removida = int(input("Digite a quantidade que deseja remover: "))
                                      
                                quantidade_nova = int(quantidade_produto_lista[exibir_produto_codigo]) - quantidade_removida
                                
                                quantidade_produto_lista.pop(exibir_produto_codigo)
                                quantidade_produto_lista.insert(exibir_produto_codigo, quantidade_nova)

                                quantidade_produto_saida += quantidade_removida 
                                quantidade_produto_saida_lista.insert(exibir_produto_codigo, quantidade_produto_saida)

                                                                
                                #Menssagem de exito
                                if(variavel_escolha == "1"):
                                    print("\n---------------------------------------")
                                    print("Baixa de produto concluida com sucesso!")
                                    print("---------------------------------------\n")
                                    break

                            #Não excluir o produto
                            elif(variavel_escolha == "2"):
                                print("-----------------------------\n")
                                break

                            #Se o usuário digitar valor vazio
                            elif(variavel_escolha == ""):
                                print("\n-----------------------------------------")
                                print("Valor invalido ou produto não cadastrado")
                                print("-----------------------------------------\n")                                

                            #Se o usuário digitar caracter invalidos
                            else:
                                print("\n-----------------------------------------")
                                print ("Valor invalido ou produto não cadastrado")
                                print("-----------------------------------------\n")
                    break
#   #   #   #Saldo de estoque unitário #3.3
            elif (menu_controle_produto == "3"):
                if (nome_produto_lista == []):
                    print("\n-------------------------")
                    print("Nenhum produto cadastrado")
                    print("-------------------------\n")

                #Listar produtos cadastrados
                else:
                    while True:

                        #For que printar os produtos
                        print("Lista de produtos cadastrados")
                        for i in range(len(codigo_produto_lista)):            
                            print(codigo_produto_lista[i]," --- ",nome_produto_lista[i])
                        print("\n\n")
                    
                        exibir_produto_codigo = int(input("Digite o código do produto: "))

                        #Valor não contido dentro da lista de codigos
                        if exibir_produto_codigo not in codigo_produto_lista:
                            print("\n-----------------------------------------")
                            print("Valor invalido ou produto não cadastrado")
                            print("-----------------------------------------\n")                           
                        
                        else:
                            #Printar dados especificos do produto
                                                      
                            print("\n------------------------")
                            print("Cód.:", codigo_produto_lista[exibir_produto_codigo])
                            print("Nome:", nome_produto_lista[exibir_produto_codigo])
                            print("Quantidade inicial: ", quantidade_produto_antiga_lista[exibir_produto_codigo])
                            print("Quantidade atual: ", quantidade_produto_lista[exibir_produto_codigo])
                            print("------------------------\n")
                            
                                                         
                            break                        
                    
#   #   #   #Análise total de estoque #3.4
            elif (menu_controle_produto == "4"):

                if (nome_produto_lista == []):
                    print("\n-------------------------")
                    print("Nenhum produto cadastrado")
                    print("-------------------------\n")

                else:
                    #For que printar os produtos
                    print("\n-------------------------------------")
                    print("Lista de produtos cadastrados")
                    for i in range(len(codigo_produto_lista)):            
                        print(codigo_produto_lista[i]," --- ",nome_produto_lista[i], " --- Quant. disponível: ",quantidade_produto_lista[i])
                    print("-------------------------------------\n")
            

                   


#   #   #   #Retornar ao menu principal #3.6
            elif(menu_controle_produto == "5"):
                break

            #Condição caso o usuario digite um numero errado
            else:
                print("\n-----------------------------------------")
                print("O número ou caracter digitado é inválido.")
                print("Por favor, tente novamente.")
                print("-----------------------------------------\n")
                
        



    
#   #condição do while, se o menu for diferente de 4 ele continua, caso contrario ele encerra e manda uma mensagem    
    elif(menu_principal == "4"):
        print("Obrigado por usar nosso programa!")
        break

#   #Condição caso o usuario digite um numero errado
    else:
        print("\n-----------------------------------------")
        print("O número ou caracter digitado é inválido.")
        print("Por favor, tente novamente.")
        print("-----------------------------------------\n")

