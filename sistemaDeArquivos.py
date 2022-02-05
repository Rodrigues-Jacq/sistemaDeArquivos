import os

def criaDir():
    nomeDir = input("Informe o nome do diretório: ")
    if(os.path.exists(nomeDir)):
        print("Diretório informado já existe!")
    else:
        os.mkdir(nomeDir)

def criaArq():
    nomeArquivo = input("Informe o nome do Arquivo: ")
    if(os.path.exists(nomeArquivo)):
        print("Nome do arquivo informado já existe")
    else:
        os.mknod(nomeArquivo)
        print("Arquivo criado com sucesso!\n")

def renomeiaDir():
    nomeDir = input("Informe o nome do diretório que queira renomear: ")
    if(os.path.exists(nomeDir)):
        nomeNovo = input("Informe o novo nome para o diretório: ")
        os.rename(nomeDir, nomeNovo)
    else:
        print("Diretório informado não existe!")

def renomeiaArq():
    nomeArquivo = input("Informe o nome do arquivo que queira renomear: ")
    if(os.path.exists(nomeArquivo)):
        nomeNovo = input("Informe o novo nome para o arquivo: ")
        os.rename(nomeArquivo, nomeNovo)
    else:
        print("Arquivo informado não existe!")

print("Sistema de Arquivos\nInforme o que deseja realizar\n")
print("1- Criar diretório\n2- Criar arquivo\n3- Renomear diretório\n4- Renomear arquivo\n")
escolha = int(input("Escolha: "))

if(escolha == 1):
    criaDir()
elif(escolha == 2):
    criaArq()
elif(escolha == 3):
    renomeiaDir()
elif(escolha == 4):
    renomeiaArq()
else:
    print("Encerrado!")