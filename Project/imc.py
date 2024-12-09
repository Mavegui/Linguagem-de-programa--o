class Pessoa:
    def __init__(self, peso, altura):
        """
        Inicializa os atributos peso e altura.
        :param peso: Peso da pessoa em kg
        :param altura: Altura da pessoa em metros
        """
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        """
        Calcula o IMC da pessoa.
        :return: Valor do IMC
        """
        return self.peso / (self.altura ** 2)

    def classificar_imc(self):
        """
        Classifica a pessoa com base no IMC.
        :return: Categoria do IMC (ex.: "magro", "normal", etc.)
        """
        imc = self.calcular_imc()
        if imc < 18.5:
            return "magro"
        elif imc <= 24.9:
            return "normal"
        elif imc <= 29.9:
            return "sobrepeso"
        elif imc <= 39.9:
            return "obesidade"
        else:
            return "obesidade grave"


def main():
    """
    Função principal para entrada de dados e exibição de resultados.
    """
    try:
        # Solicita os dados do usuário
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))

        # Cria um objeto da classe Pessoa
        pessoa = Pessoa(peso, altura)

        # Calcula e exibe o IMC e a classificação
        imc = pessoa.calcular_imc()
        classificacao = pessoa.classificar_imc()

        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Você é classificado como: {classificacao}.")

    except ValueError:
        # Trata erros de entrada inválida
        print("Por favor, insira valores numéricos válidos para peso e altura!")

if __name__ == "__main__":
    main()
