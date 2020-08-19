class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    filho = Pessoa(nome='Luciano')
    pai = Pessoa(filho, nome='Alfredo', idade=60)
    print(Pessoa.cumprimentar(pai))
    print(Pessoa.cumprimentar(filho))
    print(pai.nome)
    print(pai.idade)
    for i in pai.filhos:
        print(filho.nome)


