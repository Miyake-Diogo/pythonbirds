class Pessoa:
    # atributo de classe geralmente é para aqueles atributos que são iguais a todos os objetos
    olhos = 2
    def __init__(self, *filhos,nome = None, idade=28):
        self.idade = idade
        self.nome = nome # lado direito atributo, esquerdo recebe o parametro
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 'decorators'
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'\nAcesso aos atributos da classe: \n{cls} - olhos = {cls.olhos}'


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
    # __dict__: apenas possui os atributos de instancia, e não de classe
    print(jamile.__dict__)
    print(diogo.__dict__)
    # removendo um atributo
    del jamile.filhos
    print(jamile.__dict__)
    # Obs.: não é boa prática... o ideal é usar no __init__
    # É muito util para casos onde se deve trazer algo como em um app web durante uma requisição, pois só terá trazido naquele instante
    print(Pessoa.olhos)
    print(diogo.olhos)
    diogo.olhos = 1
    print(diogo.olhos)
    print(diogo.__dict__)
    del diogo.olhos
    print("Note que é deletado o atributo do objeto e não da classe: \n",diogo.__dict__)
    print(id(Pessoa.olhos),id(jamile.olhos),id(diogo.olhos))

    # para metodos estaticos
    print(Pessoa.metodo_estatico(), diogo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), jamile.nome_e_atributos_de_classe())

