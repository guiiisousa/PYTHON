class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
    
    def listar_livros(self):
        for livro in self.livros:
            print(livro)
            
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"{self.titulo} por {self.autor}"