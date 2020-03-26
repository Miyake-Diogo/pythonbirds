class Pessoa:
    def __init__(self, *filhos,nome = None, idade=28):
        self.idade = idade
        self.nome = nome # lado direito atributo, esquerdo recebe o parametro
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    olivia = Pessoa(nome='Olivia')
    lara = Pessoa(nome='Lara')
    jamile = Pessoa(olivia, nome='Jamile')
    diogo = Pessoa(nome='Diogo', idade=30)
    print(Pessoa.cumprimentar(diogo))
    print(id(jamile))
    print(jamile.nome)
    print(jamile.idade)
    for filho in jamile.filhos:
        print(filho.nome)
    print(diogo.idade)


