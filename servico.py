from abc import ABC, abstractmethod


class Servico(ABC):
    def __init__(self, descricao: str, mao_de_obra: float):
        if not descricao or not descricao.strip():
            raise ValueError("A descrição é obrigatória.")
        if mao_de_obra < 0:
            raise ValueError("A mão de obra não pode ser negativa.")

        self._descricao = descricao.strip()
        self._mao_de_obra = mao_de_obra

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def mao_de_obra(self) -> float:
        return self._mao_de_obra

    @abstractmethod
    def calcular_valor(self) -> float:
        """Cada serviço deve implementar seu próprio cálculo."""
        pass

class TrocaOleo(Servico):
    def __init__(self, mao_de_obra: float, valor_materiais: float):
        super().__init__("Troca de óleo", mao_de_obra)

        if valor_materiais < 0:
            raise ValueError("O valor dos materiais não pode ser negativo.")

        self._valor_materiais = valor_materiais

    @property
    def valor_materiais(self) -> float:
        return self._valor_materiais

    def calcular_valor(self) -> float:
        # Polimorfismo: cálculo específico
        # da troca de óleo
        return self._mao_de_obra + self._valor_materiais

class TrocaOleo(Servico):
    def __init__(self, mao_de_obra: float, valor_materiais: float):
        super().__init__("Troca de óleo", mao_de_obra)

        if valor_materiais < 0:
            raise ValueError("O valor dos materiais não pode ser negativo.")

        self._valor_materiais = valor_materiais

    @property
    def valor_materiais(self) -> float:
        return self._valor_materiais

    def calcular_valor(self) -> float:
        # Polimorfismo: cálculo específico
        # da troca de óleo
        return self._mao_de_obra + self._valor_materiais

class Alinhamento(Servico):
    def __init__(self, mao_de_obra: float, taxa_equipamento: float):
        super().__init__("Alinhamento", mao_de_obra)

        if taxa_equipamento < 0:
            raise ValueError("A taxa do equipamento não pode ser negativa.")

        self._taxa_equipamento = taxa_equipamento

    @property
    def taxa_equipamento(self) -> float:
        return self._taxa_equipamento

    def calcular_valor(self) -> float:
        # Polimorfismo: cálculo específico
        # do alinhamento
        return self._mao_de_obra + self._taxa_equipamento