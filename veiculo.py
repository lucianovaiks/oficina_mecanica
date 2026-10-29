class Veiculo:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A placa é obrigatória.")
        self._placa = valor.strip().upper()

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O modelo é obrigatório.")
        self._modelo = valor.strip()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O ano deve ser um número inteiro.")
        if valor < 1886 or valor > 2100:
            raise ValueError("Ano do veículo inválido.")
        self._ano = valor

    def __str__(self):
        return f"{self.modelo} ({self.ano})\nPlaca: {self.placa}"