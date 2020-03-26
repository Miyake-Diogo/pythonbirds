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
    diogo.sobrenome = 'Miyake' # atributo somente para este objeto
    print(diogo.sobrenome)
    # Atributo para verificar todos os atributos de instancia (init e dinamicos)
    # __dict__
    print(jamile.__dict__)
    print(diogo.__dict__)
    # removendo um atributo
    del jamile.filhos
    print(jamile.__dict__)
    # Obs.: não é boa prática... o ideal é usar no __init__
    # É muito util para casos onde se deve trazer algo como em um app web durante uma requisição, pois só terá trazido naquele instante





