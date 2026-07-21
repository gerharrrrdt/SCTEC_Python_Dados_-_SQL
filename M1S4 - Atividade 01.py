### DADOS CADASTRADOS
# USUÁRIOS
usuario_00 = "00"
senha_usuario_00 = 1234

# ESCOLAS
matriz = 0
filial_01 = 1
filial_02 = 2
filial_03 = 3

### DADOS DE ENTRADA
escola_atual = None
usuario_atual = None
senha_atual = None
horario_atual = None
menu = None
status = 0
registros = ["--:--",
             "--:--",
             "--:--",
             "--:--"]

### FUNÇÕES
def validarStatus(status_atual):
    global status
    validacao = status_atual
    if(validacao == 0):
        registros[0] = str(input("\nInformar horário de entrada: "))
        status += 1
    elif(validacao == 1):
        print("\nIncluir horário de almoço?")
        almoco = str(input("[S] Sim\n[N] Não\nOpção desejada: "))
        if(almoco == "S"):
            registros[1] = str(input("\nInformar horário de almoço: "))
            status += 1
        else:
            registros[1] = "Não realizado horário de almoço"
            registros[3] = str(input("\nInformar horário de saída: "))
            status = 4
            return
    elif(validacao == 2):
        registros[2] = str(input("\nInformar horário de retorno de almoço: "))
    elif(validacao == 3):
        registros[3] = str(input("\nInformar horário de saída: "))
    else:
        print(50*"=")
        print("NÃO É POSSÍVEL ADICIONAR MAIS REGISTROS!")
        print(50*"=")
        return
    return

def mostrarRegistros(registro_atual):
    print(f"\nEntrada: {registro_atual[0]}\nAlmoço: {registro_atual[1]}\nRetorno Almoço: {registro_atual[2]}\nSaída: {registro_atual[3]}")
    return
        
### PROCESSAMENTO
print(50*"=")
print(14*" " + "GPE - GESTÃO DE PONTOS" + 14*" ")
print("[0] Escola Matriz\n[1] Filial 1\n[2] Filial 2\n[3] Filial 3")
escola_atual = int(input("\nInforme o local de registro: "))
while(escola_atual > 3):
    print("\nLocal não cadastrado, tente novamente!")
    escola_atual = int(input("\nInforme o local de registro: "))

if(escola_atual == 0):
    print(50*"=")
    print(22*" " + "MATRIZ" + 22*" ")
elif(escola_atual == 1):
    print(50*"=")
    print(21*" " + "FILIAL 1" + 21*" ")
elif(escola_atual == 2):
    print(50*"=")
    print(21*" " + "FILIAL 2" + 21*" ")
else:
    print(50*"=")
    print(21*" " + "FILIAL 3" + 21*" ")
    
usuario_atual = str(input("Usuário: "))
while(usuario_atual != usuario_00):
    print("\nUsuário não cadastrado, tente novamente!")
    usuario_atual = str(input("\nUsuário: "))

senha_atual = int(input("Senha: "))
while(senha_atual != senha_usuario_00):
    print("\nSenha incorreta, tente novamente!")
    senha_atual = int(input("\nSenha: "))

menu = (input("\n[A] Adicionar novo registro\n[M] Mostrar registros\n[S] Sair\nInforme a opção desejada: "))
while(menu != "S"):
    if(menu == "A"):
        validarStatus(status)
        menu = (input("\n[A] Adicionar novo registro\n[M] Mostrar registros\n[S] Sair\nInforme a opção desejada: "))
    elif(menu == "M"):
        mostrarRegistros(registros)
        menu = (input("\n[A] Adicionar novo registro\n[M] Mostrar registros\n[S] Sair\nInforme a opção desejada: "))
    else:
        print("\nOpção inválida, tente novamente!")
        menu = (input("\n[A] Adicionar novo registro\n[M] Mostrar registros\n[S] Sair\nInforme a opção desejada: "))
        
        #teste
        
        soma = 1+1