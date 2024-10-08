from model import*
clinica = Clinica_Sorrisos("katarina clinica", 15265, 3563, "ssftydg", 55)
enderecoL = Endereco(11, "a", "b", "c", "d")
enderecoP =  Endereco(12, "e", "f", "g", "h")
enderecoF =  Endereco(13, "l", "k", "j", "i")

clinica.adicionar_endereco(enderecoL)
print(clinica)
paciente = Paciente("vi", 123, 44, "abc", "vi", 123 )
paciente.adicionar_endereco(enderecoP)

funcionario = Funcionario("jose", 4355, 45253, 3.000, "prof", "jose", 456)
funcionario.adicionar_endereco(enderecoF)

clinica.adicionar_funcionarios(funcionario)
clinica.adicionar_pacientes(paciente)

func2 = Funcionario("maria", 222, 555, 6.000, "prof", "jose", 456)
func2.adicionar_endereco(enderecoF)
pac2 = Paciente("katrina", 777, 888, "insta", "kat", 333)
pac2.adicionar_endereco(enderecoP)

funcionarios = clinica.get_funcionarios()
for func in funcionarios:
    print(func)

try:
    verif = clinica.adicionar_funcionarios(func2)
except(FuncionarioExistente):
    print("h")



