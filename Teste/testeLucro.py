import requests as Req

url_basica = 'http://127.0.0.1:5000'


def testeLucro():
    url = url_basica + '/lucros'
    dados = Req.api.get(url).json()
    return dados

def main():
    print(testeLucro())

main()