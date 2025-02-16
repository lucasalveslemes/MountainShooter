# ============================================
# Definição da classe 'Funcionario'
# ============================================

class Funcionario:
    """
    Classe que representa um funcionário.

    Quando criamos um novo funcionário, precisamos fornecer:
    - Um número de registro (ID)
    - Nome
    - Cargo
    - Salário
    """

    def __init__(self, in_RegID: int, in_nome: str, in_cargo: str, in_salario: int):
        """Construtor da classe, que define os atributos do funcionário."""
        self.RegId: int = in_RegID  # ID do funcionário
        self.nome: str = in_nome  # Nome do funcionário
        self.cargo: str = in_cargo  # Cargo do funcionário
        self.salario: int = in_salario  # Salário do funcionário

    def mostraReg(self):
        """Exibe os dados do funcionário na tela."""
        print("\n=============================")
        print(f"Registro #{self.RegId}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario:.2f}")
        print("=============================\n")


# ============================================
# Início do programa principal
# ============================================

# Criamos uma lista para armazenar os funcionários cadastrados.
registro = []  # Começamos com uma lista vazia

# Criamos uma variável para armazenar o próximo ID disponível
Reg_ID = 0  # Começamos do ID 1

while True:
    # Exibimos o menu de opções para o usuário
    opcao = input(
        "\nSelecione uma ação:"
        "\n1 - Adicionar funcionário"
        "\n2 - Mostrar os registros existentes"
        "\n3 - Sair"
        "\n>>> "
    )

    if opcao == '1':
        # Adiciona um novo funcionário
        Reg_ID += 1  # Atualiza o contador de IDs

        # Solicita os dados do novo funcionário
        nomeReg = input("Inserir o nome do funcionário: >> ")
        cargoReg = input("Inserir o cargo do funcionário: >> ")

        # Repetimos até o usuário inserir um valor válido para o salário
        while True:
            try:
                salarioReg = float(input("Inserir o salário do funcionário: >> "))
                break  # Se o salário for válido, saímos do loop
            except ValueError:
                print("Por favor, insira apenas números para o salário.")

        # Criamos um novo funcionário com os dados informados
        regFunc = Funcionario(in_RegID=Reg_ID, in_nome=nomeReg, in_cargo=cargoReg, in_salario=salarioReg)

        # Adicionamos esse funcionário à lista de registros
        registro.append(regFunc)

        print("\nFuncionário cadastrado com sucesso!")
        regFunc.mostraReg()  # Exibe os dados do funcionário recém-cadastrado

    elif opcao == '2':
        # Mostra a lista de funcionários cadastrados
        if not registro:  # Se a lista estiver vazia
            print("\nNenhum funcionário registrado ainda.")
        else:
            print("\nLista de Funcionários:")
            for funcionario in registro:
                funcionario.mostraReg()  # Exibe os dados de cada funcionário

    elif opcao == '3':
        # Sai do programa
        print("Encerrando o sistema...")
        break

    else:
        # Se o usuário digitar uma opção inválida, mostramos um aviso
        print("Opção inválida, tente novamente!")
