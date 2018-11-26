from datetime import datetime
#AnaliseFinac = {'profit':[], 'losses':[], 'future':[]}
def pagamentosConsultas():
    from Nutrin.Consulta.Services.Consulta.listConsulta import listConsultas
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    consultas = listConsultas(True)
    AnaliseFinac = {'profit':[], 'losses':[], 'future':[]}
    mes = datetime.now().month
    ano = datetime.now().year
    #print(consultas)
    for c in consultas:
        status, tipoAtm = readTipoAtendimento(True, c['tipoAtendimento_id'])
        # print('---------------------------consultas')
        # print(c)
        # print('---------------------------tipoAtem')
        # print(tipoAtm)
        if status:                
            #print(tipoAtm)
            valor = tipoAtm.preco
            '2018-02-01'
            anoConsulta = c['horario_id'][-1]
            mesConsulta = c['horario_id'][-1]
            data = anoConsulta[:7]
            if int(anoConsulta[:4]) <= ano and int(mesConsulta[5:7]) < mes:
                print(int(anoConsulta[:4]),int(mesConsulta[5:7]))
                if c['pagamento']:
                    tipo = 'profit'
                else:
                    tipo = 'losses'
            else:
                tipo = 'future'
            print('-------------------------------- var')
            print(tipo, data, valor, AnaliseFinac)
            financeiro = construtor(AnaliseFinac, tipo, data, valor)
    valores = [AnaliseFinac]
    return valores


def construtor(AnaliseFinac,tipo, mes, valor):
    for p, x in AnaliseFinac.items():
        #print(p,x)
        if p==tipo:
            if not x:
                AnaliseFinac[p].append({
                    'mes':mes,
                    'vlrTotal': valor,
                    'qtdConsultas': 1
                })
                return AnaliseFinac
            else:
                for i in x:
                    if i['mes'] == mes:
                        i['vlrTotal'] = i['vlrTotal'] + valor
                        i['qtdConsultas'] += 1
                        return AnaliseFinac
                AnaliseFinac[p].append({
                        'mes':mes,
                        'vlrTotal': valor,
                        'qtdConsultas': 1
                })
    return AnaliseFinac


# validações:
# 1- validar mes
#     profit e losses < atual
#     future >= atual
#     -- finacn[0]['profit'] == profit
#     -- finacn[0]['losses'] == losses
#     -- finacn[0]['future'] == future
# #exemplo profit




# 1.2 - verificar se True or False no profit e losses
# 2- somar a vlrTotal sem repedir data
# 3 - somar qtdConsultas

# modelo
# AnaliseFinac = [{
#             profit: [{
#                     'mes':'11-2018',
#                     'vlrTotal': 600,
#                     'qtdConsultas': 3
#             },
#             {
#                     'mes':'10-2018',
#                     'vlrTotal': 1600,
#                     'qtdConsultas': 7
#             }],
#             losses: [{
#                     'mes':'11-2018',
#                     'vlrTotal': 200,
#                     'qtdConsultas': 1
#             }],
#             future:[{
#                     'mes':'12-2018',
#                     'vlrTotal': 400,
#                     'qtdConsultas': 2
#             }]
# }]
