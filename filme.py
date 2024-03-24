class Filme:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano

    def __str__(self):
        return f"Título: {self.titulo} | Gênero: {self.genero} | Ano: {self.ano}"
