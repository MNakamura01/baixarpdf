#importando bibliotecas
import requests
import json

#definindo URL do arquivo PDF
URL = "https://diariodonordeste.verdesmares.com.br/filedelivery/policy:1.3064797:1616637665/Tabela%20Ba%CC%81sica%20da%20Se%CC%81rie%20A%202021.pdf"

#definindo header da request
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

#definindo atribustos gerais da request
site = requests.get(URL, headers=headers)

diretorio = input('Deseja salvar o pdf em um diretório específico?')
#realizando requisição e criando / atualizando o arquivo na pasta selecionada
if diretorio != '':
    try:
        with open(f'{diretorio}/tabela.pdf', 'wb') as f:
            f.write(site.content)
            print("Arquivo PDF criado com sucesso!")
    except:
        print("Arquivo PDF não foi criado!")
else:
    try:
        with open('tabela.pdf', 'wb') as f:
            f.write(site.content)
            print("Arquivo PDF criado com sucesso!")
    except:
        print("Arquivo PDF não foi criado!")

#print de confirmação no console

if site.status_code == 200:
    print("Requisição concluída com sucesso!")
    print(site.elapsed)

    # site.history retorna o histórico do site

    print(site.history)
    print(site.encoding)
elif site.status_code == 404:
    print("URL não encontrada")
elif site.status_code == 500:
    print("Parametros inválidos")
else:
    print("Erro")
    