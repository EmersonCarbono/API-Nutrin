from Nutrin.Consulta.Services.TipoEstado.readTipoEstado import readEstadoById
from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readAtendimentoById
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoById
from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPacienteById
from Nutrin.Controle.converter_data import binaryToString

def readConsulta(f=False,lucro=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    consultas = Consulta.query.all()
    if consultas != None:
        if f:
            if lucro:
                consulas_dic = []
                for c in consultas:
                    horario = readOcupadoById(c.horario_id)
                    consulas_dic.append({
                        'id': c.id,
                        'tipoAtendimento_id': c.tipoAtendimento_id,
                        'horario_id': horario,
                        'pagamento': c.pagamento
                    })

                return True, consulas_dic
            return True, consultas
        consulas_dic = []
        for c in consultas:
            tipoEstado = readEstadoById(c.tipoEstado_id)
            tipoAtendimento = readAtendimentoById(c.tipoAtendimento_id)
            horario = readOcupadoById(c.horario_id)
            paciente = pesquisarPacienteById(c.paciente_id)
            dieta = binaryToString(c.dieta)
            consulas_dic.append({
                'id': c.id,
                'paciente_id': paciente,
                'tipoAtendimento_id': tipoAtendimento.nome,
                'horario_id': horario,
                'tipoEstado_id':tipoEstado.nome,
                'antropometria_id': c.antropometria_id,
                'dieta': dieta,
                'pagamento': c.pagamento
            })
        return True, consulas_dic
    return False, 'Nenhuma Consulta cadastrada'

def readConsultaId(id_consulta, f=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    #consultas = Consulta.query().filter(id==id_consulta)
    consultas = Consulta.query.get(id_consulta)
    print(consultas)
    if consultas != None:
        if f:
            return True, consultas
        consultas_dic = []   
        tipoEstado = readEstadoById(consultas.tipoEstado_id)
        tipoAtendimento = readAtendimentoById(consultas.tipoAtendimento_id)
        horario = readOcupadoById(consultas.horario_id)
        paciente = pesquisarPacienteById(consultas.paciente_id)
        dieta = binaryToString(consultas.dieta)
        consultas_dic.append({
            'id': consultas.id,
            'paciente_id': paciente,
            'tipoAtendimento_id': tipoAtendimento.nome,
            'horario_id': horario,
            'tipoEstado_id': tipoEstado.nome,
            'antropometria_id': consultas.antropometria_id,
            'dieta': dieta,
            'pagamento': consultas.pagamento
        })
        return True, consultas_dic
    return False, 'Nenhuma consulta com este id'

