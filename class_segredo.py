class Segredo:
    def __init__(self, segredo):
        self.__segredo = segredo  # Atributo privado
    
    def set_segredo(self, novo_segredo):
        self.__segredo = novo_segredo
    
    def get_segredo(self):
        return self.__segredo

# Exemplo de uso
segredo = Segredo("Este é um segredo!")
print(f'Segredo: {segredo.get_segredo()}')

segredo.set_segredo("Novo segredo revelado!")
print(f'Segredo atualizado: {segredo.get_segredo()}')
