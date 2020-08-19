class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa('Luciano', 40)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)

