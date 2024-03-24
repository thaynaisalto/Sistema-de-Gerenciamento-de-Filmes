from filme import Filme

class SistemaFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, titulo, genero, ano):
        filme = Filme(titulo, genero, ano)
        self.filmes.append(filme)
        print(f"O filme '{titulo}' foi adicionado com sucesso!")

    def excluir_filme(self, titulo):
        for filme in self.filmes:
            if filme.titulo == titulo:
                self.filmes.remove(filme)
                print(f"O filme '{titulo}' foi removido com sucesso!")
                return
        print(f"Erro: O filme '{titulo}' não foi encontrado.")

    def listar_filmes(self):
        if not self.filmes:
            print("Nenhum filme cadastrado ainda.")
            return
        print("Lista de Filmes:")
        for filme in self.filmes:
            print(filme)

    def listar_filmes_por_genero(self, genero):
        genero = genero.lower()
        filmes_por_genero = [filme for filme in self.filmes if filme.genero.lower() == genero]
        if not filmes_por_genero:
            print(f"Nenhum filme do gênero '{genero}' foi encontrado.")
            return
        print(f"Lista de Filmes do gênero '{genero.capitalize()}':")
        for filme in filmes_por_genero:
            print(filme)

def menu():
    print("\n======= MENU =======")
    print("1. Adicionar Filme")
    print("2. Excluir Filme")
    print("3. Lista de Filmes")
    print("4. Lista de Filmes por Gênero")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    sistema = SistemaFilmes()

    while True:
        escolha = menu()

        if escolha == '1':
            titulo = input("Digite o título do filme: ")
            genero = input("Digite o gênero do filme: ")
            ano = input("Digite o ano de lançamento do filme: ")
            sistema.adicionar_filme(titulo, genero, ano)
        elif escolha == '2':
            titulo = input("Digite o título do filme que deseja excluir: ")
            sistema.excluir_filme(titulo)
        elif escolha == '3':
            sistema.listar_filmes()
        elif escolha == '4':
            genero = input("Digite o gênero que deseja listar: ")
            sistema.listar_filmes_por_genero(genero)
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
