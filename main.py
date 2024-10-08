from model import*

clinica = Clinica_Sorrisos("Clinica Sorrisos", "586887.999/02", "(84) 996107967", "katarina_sorrisos@gmail.com", 963415)
opcao_menu = 1

while opcao_menu != 0:
    print(f"Seja bem vindo a {clinica.nome} ")
    print("""
    1...............Acessar como Paciente
    2...............Acessar como Funcionário
    3...............Acessar como proprietário
    0...............Sair""")
    opcao_menu = int(input("Digite a opção desejada"))

#CRUD pacientes
    if opcao_menu == 1:
        while opcao_menu != 6:
            print("""
            1.............Cadastrar
            2.............Editar Cadastro
            3.............Remover Cadastro
            4.............Reativar cadastro
            5.............Exibir dados 
            6.............Voltar para página inicial""")
            opcao_menu = int(input("Digite a opção desejada: " ))

            if opcao_menu == 1:
                nome = input("Digite seu nome: ")
                cpf = input("Digite seu cpf: ")
                telefone = input("Digite seu telefone: ")
                rua = input("Digite sua rua: ")
                numero = input("Digite o numero da sua residência: ")
                bairro = input("Digite seu bairro: ")
                cidade = input("Digite sua cidade: ")
                estado = input("Digite seu estado: ")
                indicacao = input("Informe como ficou sabendo da nossa clinica")
                login = input("Digite seu login para acesso: ")
                senha = input("Digite sua senha de acesso: ")
                endereco = Endereco(numero, rua, bairro, cidade, estado)
                paciente = Paciente(nome, cpf, telefone, indicacao, login, senha)
                paciente.adicionar_endereco(endereco)

                try:
                    clinica.adicionar_pacientes(paciente)
                    print("Cadastrado com sucesso!")

                except(PacienteExistente):
                    print("Já possuimos usuário cadastrado com esse login, tente novamente!")

            if opcao_menu == 2:
                login_busca = input("Digite o login para busca: ")
                senha_busca = input("Digite a sua senha: ")
                print("Por favor, informe os novos dados \n")
                nome = input("Digite seu nome: ")
                cpf = input("Digite seu cpf: ")
                telefone = input("Digite seu telefone: ")
                rua = input("Digite sua rua: ")
                numero = input("Digite o numero da sua residência: ")
                bairro = input("Digite seu bairro: ")
                cidade = input("Digite sua cidade: ")
                estado = input("Digite seu estado: ")
                indicacao = input("Informe como ficou sabendo da nossa clinica")
                login = input("Digite seu login para acesso: ")
                senha = input("Digite sua senha de acesso: ")
                endereco = Endereco(numero, rua, bairro, cidade, estado)
                paciente = Paciente(nome, cpf, telefone, indicacao,login, senha)
                paciente.adicionar_endereco(endereco)
                verif = clinica.editar_paciente(login_busca, senha_busca, paciente)
                if verif == True:
                    print("Dados atualizados com sucesso! ")

                else:
                    print("Algo deu errado, tente novamente!")

            if opcao_menu == 3:
                login_busca = input("Digite o login para busca")
                senha_busca = input("Digite a senha: ")
                verif = clinica.excluir_paciente(login_busca, senha_busca)
                if verif == True:
                    print("Paciente excluído!")
                else:
                    print("ops...Algo deu errado, tente novamente")

            if opcao_menu == 4:
                login_busca = input("Digite o login para busca")
                senha_busca = input("Digite a senha: ")
                verif = clinica.reativar_paciente(login_busca, senha_busca)
                if verif == True:
                    print("Paciente reativado com sucesso! ")
                else:
                    print("tente novamente!")

            if opcao_menu == 5:
                login_busca = input("Digite o login para busca")
                senha_busca = input("Digite a senha: ")
                exibir = clinica.exibir_paciente(login_busca, senha_busca)
                print(exibir)

            if opcao_menu > 5:
                print("Essa opção não é válida, tente novamente.")

#CRUD funcionários
    if opcao_menu == 2:
        while opcao_menu != 6:
            print("""
            1.............Cadastrar
            2.............Editar Cadastro
            3.............Remover Cadastro
            4.............Reativar cadastro
            5.............Exibir dados 
            6.............Voltar para página inicial""")
            opcao_menu = int(input("Digite a opção desejada: "))

            if opcao_menu == 1:
                nome = input("Digite seu nome: ")
                cpf = input("Digite seu cpf: ")
                telefone = input("Digite seu telefone: ")
                rua = input("Digite sua rua: ")
                numero = input("Digite o numero da sua residência: ")
                bairro = input("Digite seu bairro: ")
                cidade = input("Digite sua cidade: ")
                estado = input("Digite seu estado: ")
                salario = float(input("Digite seu salário"))
                funcao = input("Informe sua funcao ")
                login = input("Digite seu login para acesso: ")
                senha = input("Digite sua senha de acesso: ")
                endereco = Endereco(numero, rua, bairro, cidade, estado)
                funcionario = Funcionario(nome, cpf, telefone, salario, funcao, login, senha)
                funcionario.adicionar_endereco(endereco)

                try:
                    clinica.adicionar_funcionarios(funcionario)
                    print("Cadastrado com sucesso!")

                except(FuncionarioExistente):
                    print("Já possuimos usuário cadastrado com esse login, tente novamente!")

            if opcao_menu == 2:
                login_busca = input("Digite o login para busca: ")
                senha_busca = input("Digite a sua senha: ")
                print("Por favor, informe os novos dados \n")
                nome = input("Digite seu nome: ")
                cpf = input("Digite seu cpf: ")
                telefone = input("Digite seu telefone: ")
                rua = input("Digite sua rua: ")
                numero = input("Digite o numero da sua residência: ")
                bairro = input("Digite seu bairro: ")
                cidade = input("Digite sua cidade: ")
                estado = input("Digite seu estado: ")
                salario = float(input("Digite seu salário: "))
                funcao = input("Informe sua função na clínica")
                login = input("Digite seu login para acesso: ")
                senha = input("Digite sua senha de acesso: ")
                endereco = Endereco(numero, rua, bairro, cidade, estado)
                funcionario = Funcionario(nome, cpf, telefone,salario, funcao, login, senha)
                funcionario.adicionar_endereco(endereco)
                verif = clinica.editar_funcionario(login_busca, senha_busca, funcionario)
                if verif == True:
                    print("Dados atualizados com sucesso! ")

                else:
                    print("Algo deu errado, tente novamente!")

            if opcao_menu == 3:
                login_busca = input("Digite o login para busca")
                senha_busca = input("Digite a senha: ")
                verif = clinica.excluir_funcionario(login_busca, senha_busca)
                if verif == True:
                    print("Funcionário excluído!")
                else:
                    print("ops...Algo deu errado, tente novamente")

            if opcao_menu == 4:
                login_busca = input("Digite o login para busca")
                senha_busca = input("Digite a senha: ")
                verif = clinica.reativar_funcionarios(login_busca, senha_busca)
                if verif == True:
                    print("Funcionário reativado com sucesso! ")
                else:
                    print("tente novamente!")

            if opcao_menu == 5:
                login_busca = input("Digite o login para busca")
                senha_busca = input("Digite a senha: ")
                exibir = clinica.exibir_funcionario(login_busca, senha_busca)
                print(exibir)

            if opcao_menu > 5:
                print("Essa opção não é válida, tente novamente.")

#exclusivo apenas para o dono da clínica
    if opcao_menu == 3:
        senha = int(input("Digite a senha da sua clínica"))
        verif = clinica.autorizacao(senha)
        if verif == True:
            while opcao_menu != 5:
                print("""
                1..........exibir pacientes ativos
                2..........exibir funcionarios ativos
                3..........exibir pacientes excluidos
                4..........exibir funcionarios excluidos
                5.........voltar para págia inicial
                """)
                opcao_menu = input("Digite a opção desejada ")

                if opcao_menu == 1:
                    pacientes = clinica.get_pacientes()
                    for paciente in pacientes:
                        print(paciente)

                if opcao_menu == 2:
                    funcionarios = clinica.get_funcionarios()
                    for funcionario in funcionarios:
                        print(funcionario)

                if opcao_menu == 3:
                    pac_excluidos = clinica.get_pacientesExcluidos()
                    for paciente in pac_excluidos:
                        print(paciente)

                if opcao_menu == 4:
                    func_excluidos = clinica.get_funcionariosExcluidos()
                    for func in func_excluidos:
                        print(func)



        else:
            print("Você não tem autorização para entrar!")