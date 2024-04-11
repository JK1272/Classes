class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def calcular_palavras_por_pagina(self, num_palavras):
        if self.num_paginas > 0:
            palavras_por_pagina = num_palavras / self.num_paginas
            return palavras_por_pagina
        else:
            print("O número de páginas do livro deve ser maior que zero.")
            return None


livro1 = Livro(titulo="Dom Casmurro", autor="Machado de Assis", num_paginas=200)

livro1.mostrar_informacoes()

num_palavras_total = 50000  
palavras_por_pagina = livro1.calcular_palavras_por_pagina(num_palavras_total)
if palavras_por_pagina is not None:
    print(f"Quantidade média de palavras por página: {palavras_por_pagina:.2f}")