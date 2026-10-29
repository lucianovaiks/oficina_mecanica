from veiculo import Veiculo
from servico import TrocaOleo, Alinhamento
from ordem_servico import OrdemServico

veiculos = []
ordens = []

def cadastrar_veiculo():
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))

    veiculo = Veiculo(placa, modelo, ano)
    veiculos.append(veiculo)

    print("Veículo cadastrado com sucesso!")


def lancar_servico():
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return

    print("\nVeículos cadastrados:")
    for i, veiculo in enumerate(veiculos):
        print(f"{i + 1} - {veiculo}")

    indice = int(input("Escolha o veículo: ")) - 1

    if indice < 0 or indice >= len(veiculos):
        print("Veículo inválido.")
        return

    cliente = input("Nome do cliente: ")

    ordem = OrdemServico(cliente, veiculos[indice])

    print("\nTipos de serviço:")
    print("1 - Troca de óleo")
    print("2 - Alinhamento")

    opcao = input("Escolha: ")

    if opcao == "1":
        mao = float(input("Mão de obra: "))
        materiais = float(input("Valor dos materiais: "))
        servico = TrocaOleo(mao, materiais)

    elif opcao == "2":
        mao = float(input("Mão de obra: "))
        taxa = float(input("Taxa do equipamento: "))
        servico = Alinhamento(mao, taxa)

    else:
        print("Serviço inválido.")
        return

    ordem.adicionar_servico(servico)
    ordens.append(ordem)

    print("Serviço lançado com sucesso!")


def listar_ordens():
    if not ordens:
        print("Nenhuma ordem de serviço cadastrada.")
        return

    print("\nOrdens de Serviço:")
    for i, ordem in enumerate(ordens):
        print(f"\nOrdem {i + 1}")
        ordem.resumo()


def exibir_orcamento():
    if not ordens:
        print("Nenhuma ordem de serviço cadastrada.")
        return

    print("\nOrdens disponíveis:")
    for i, ordem in enumerate(ordens):
        print(f"{i + 1} - {ordem.cliente}")

    indice = int(input("Escolha a ordem: ")) - 1

    if indice < 0 or indice >= len(ordens):
        print("Ordem inválida.")
        return

    ordens[indice].resumo()


def menu():
    while True:
        print("\n--- OFICINA MECÂNICA ---")
        print("1 - Cadastrar veículo")
        print("2 - Lançar serviço")
        print("3 - Listar ordens de serviço")
        print("4 - Exibir orçamento")
        print("0 - Sair")

        opcao = input("Opção: ")

        try:
            if opcao == "1":
                cadastrar_veiculo()

            elif opcao == "2":
                lancar_servico()

            elif opcao == "3":
                listar_ordens()

            elif opcao == "4":
                exibir_orcamento()

            elif opcao == "0":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida!")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    menu()