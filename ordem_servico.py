from veiculo import Veiculo
from servico import Servico


class OrdemServico:
    def __init__(self, cliente, veiculo):
        if not cliente.strip():
            raise ValueError("O nome do cliente é obrigatório.")
        if not isinstance(veiculo, Veiculo):
            raise ValueError("Veículo inválido.")

        self._cliente = cliente.strip()
        self._veiculo = veiculo
        self._servicos = []

    @property
    def cliente(self):
        return self._cliente

    @property
    def veiculo(self):
        return self._veiculo

    def adicionar_servico(self, servico: Servico):
        if not isinstance(servico, Servico):
            raise ValueError("Serviço inválido.")

        self._servicos.append(servico)

    def calcular_total(self) -> float:
        return sum(servico.calcular_valor() for servico in self._servicos)

    def resumo(self):
        print("\n" + "=" * 45)
        print("OFICINA MECÂNICA - ORDEM DE SERVIÇO".center(45))
        print("=" * 45)

        print(f"Cliente: {self._cliente}")
        print(f"Veículo: {self._veiculo}")

        print("-" * 45)

        if not self._servicos:
            print("Nenhum serviço registrado.")
        else:
            for servico in self._servicos:
                print(
                    f"{servico.descricao}: "
                    f"R$ {servico.calcular_valor():.2f}"
                )

        print("-" * 45)
        print(f"TOTAL: R$ {self.calcular_total():.2f}")
        print("=" * 45)