class Endereco:
    def __init__(self, numero, rua, bairro, cidade, estado):
        self.numero = numero
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


    def __str__(self):
        return f"Número: {self.numero} \n Rua: {self.rua} \n Bairro: {self.bairro} \n Cidade: {self.cidade} \n Estado: {self.estado}"

class Paciente:
    def __init__(self, nome, cpf, telefone,  indicacao, login, senha):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.indicacao = indicacao
        self.login = login
        self.senha = senha
        self.endereco = []

    def adicionar_endereco(self, endereco):
        self.endereco.append(endereco)

    def __str__(self):
        return f"Nome: {self.nome} \n Cpf: {self.cpf} \n Telefone: {self.telefone} \n Indicação: {self.indicacao} \n "
    #só vai exibir os dados do paciente

class Funcionario:
    def __init__(self, nome, cpf, telefone, salario, funcao, login, senha):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.salario = salario
        self.funcao = funcao
        self.login = login
        self.senha = senha
        self.endereco = []

    def adicionar_endereco(self, endereco):
        self.endereco.append(endereco)

    def __str__(self):
        return f"Nome: {self.nome} \n Cpf: {self.cpf} \n Telefone: {self.telefone} \n Salario: {self.salario} \n Função: {self.funcao} \n "
    #só vai exibir os dados do funcionário

class Clinica_Sorrisos:
    def __init__(self, nome, cnpj, telefone, email, senha):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.endereco = []
        self.funcionarios = []
        self.pacientes = []
        self.funcionarios_excluidos = []
        self.pacientes_excluidos = []



    def __str__(self):
        return f"Nome: {self.nome} \n Telefone para contato: {self.telefone} \n email: {self.email} \n "

    #adicionar endereço da loja
    def adicionar_endereco(self, endereco):
        self.endereco.append(endereco)

    #adicionar funcionarios
    def adicionar_funcionarios(self, funcionario):
        if self.verificar_cadastroF(funcionario):
            raise FuncionarioExistente
        self.funcionarios.append(funcionario)
        return True

    #adicionar pacientes
    def adicionar_pacientes(self, paciente):
        if self.verificar_cadastroP(paciente):
            raise PacienteExistente
        self.pacientes.append(paciente)
        return True

    #excluir funcionarios
    def excluir_funcionario(self,login, senha):
        for funcionario in self.funcionarios:
            if login == funcionario.login and senha == funcionario.senha:
                self.funcionarios.remove(funcionario)
                self.funcionarios_excluidos.append(funcionario)
                return True

        return False

    #excluir pacientes
    def excluir_paciente(self, login, senha):
        for paciente in self.pacientes:
            if login == paciente.login and senha == paciente.senha:
                self.pacientes.remove(paciente)
                self.pacientes_excluidos.append(paciente)
                return True

        return False

    #procurar e exibir funcionario
    def exibir_funcionario(self, login, senha):
        for funcionario in self.funcionarios:
            if login == funcionario.login and senha == funcionario.senha:
                return funcionario

    #procurar e exibir paciente
    def exibir_paciente(self, login, senha):
        for paciente in self.pacientes:
            if login == paciente.login and senha == paciente.senha:
                return paciente


    #exibir funcionarios ativos
    def get_funcionarios(self):
        lista_retorno = []
        for funcionario in self.funcionarios:
            lista_retorno.append(funcionario)
        return lista_retorno

    #exibir funcionários excluídos
    def get_funcionariosExcluidos(self):
        lista_retorno = []
        for funcionario in self.funcionarios_excluidos:
            lista_retorno.append(funcionario)
        return lista_retorno

    #exibir pacientes ativos
    def get_pacientes(self):
        lista_retorno = []
        for paciente in self.pacientes:
            lista_retorno.append(paciente)
        return lista_retorno

    #exibir pacientes excluídos
    def get_pacientesExcluidos(self):
        lista_retorno = []
        for paciente in self.pacientes_excluidos:
            lista_retorno.append(paciente)
        return lista_retorno

    #editar funcionario
    def editar_funcionario(self,login_busca, senha_busca, funcionario_atualizado):
        for funcionario in self.funcionarios:
            if funcionario.login == login_busca and funcionario.senha == senha_busca:
                funcionario.nome = funcionario_atualizado.nome
                funcionario.cpf = funcionario_atualizado.cpf
                funcionario.telefone = funcionario_atualizado.telefone
                funcionario.endereco = funcionario_atualizado.endereco
                funcionario.login = funcionario_atualizado.login
                funcionario.senha = funcionario_atualizado.senha
                funcionario.funcao = funcionario_atualizado.funcao
                funcionario.salario = funcionario_atualizado.salario
                return True
            return False

    #editar paciente
    def editar_paciente(self,login_busca, senha_busca, paciente_atualizado):
        for paciente in self.pacientes:
            if paciente.login == login_busca and paciente.senha == senha_busca:
                paciente.nome = paciente_atualizado.nome
                paciente.cpf = paciente_atualizado.cpf
                paciente.telefone = paciente_atualizado.telefone
                paciente.endereco = paciente_atualizado.endereco
                paciente.login = paciente_atualizado.login
                paciente.senha = paciente_atualizado.senha
                paciente.indicacao = paciente_atualizado.indicacao
                return True
            return False

    #verificar login e senha funcionarios
    def verificar_cadastroF(self, funcionarioNovo):
        for funcionario in self.funcionarios:
            if funcionarioNovo.login == funcionario.login or funcionarioNovo.senha == funcionario.senha:
                return True
            return False


    #verificar login e senha paciente
    def verificar_cadastroP(self, pacienteNovo):
        for paciente in self.pacientes:
            if pacienteNovo.login == paciente.login or pacienteNovo.senha == paciente.senha:
                return True
            return False

    #obs: pode existir funcionario e paciente com o mesmo login, pois os dois possuem atributos diferentes


    #reativar funcionarios inativos
    def reativar_funcionarios(self, login, senha):
        for funcionario in self.funcionarios_excluidos:
            if login == funcionario.login and senha == funcionario.senha:
                self.funcionarios_excluidos.remove(funcionario)
                self.funcionarios.append(funcionario)
                return True

            return False

    #reativar pacientes inativos
    def reativar_paciente(self, login, senha):
        for paciente in self.pacientes_excluidos:
            if login == paciente.login and senha == paciente.senha:
                self.pacientes_excluidos.remove(paciente)
                self.pacientes.append(paciente)
                return True

            return False

    def autorizacao(self, senha):
        if senha == self.senha:
            return True

        return False


class PacienteExistente(Exception):
    pass

class FuncionarioExistente(Exception):
    pass