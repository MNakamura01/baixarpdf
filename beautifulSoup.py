from bs4 import BeautifulSoup
import requests
import json

token_login = requests.post(
    'https://accounts.google.com/_/signin/challenge?hl=pt&TL=AM3QAYa2AMnGX_smcwFNKvmGjWNLDCjyCOLiHcBHCaFq9KGyHNd1zu8qhgCoE6go&_reqid=280219&rt=j',
    data = {
        "username": 'ULTRA RJ',
        "password": 'ULTRA RJ',
        "grant_type": 'password',
        "empresaId": 1,
        "filialId": 1
    }
)
access_token = token_login.json()['access_token']
headers = {'Content-Type': 'application/json','Authorization': f'Bearer {access_token}'}

extrair_relatorio = requests.post(
    'http://8aff0ad50fea.sn.mynetname.net:8181/PortalABTLBack/api/v1/helpesReports/export',
    data = json.dumps({
        "filtro": {
            "anoFim": 2022,
            "anoIni": 2022,
            "filialId": "1",
            "flagAtivo": False,
            "mesFim": 5,
            "mesIni": 1,
            "periodoAte": "052022",
            "periodoDe": "012022",
            "porto": "ARATU/BA",
            "portoId": "2",
            "usuario": "ULTRA RJ"
        },
        "sisFormularioId": 332034
    }),
    headers= headers
)
print(extrair_relatorio)

with open('relatório.xls', 'wb') as f:
    f.write(extrair_relatorio.content)

#import ipdb;ipdb.set_trace()