class Pessoa:
    def __init__(self, nome = None, idade=None):
        self.idade = idade
        self.nome = nome # lado direito atributo, esquerdo recebe o parametro

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Jamile')
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Diogo'
    print(p.nome)


