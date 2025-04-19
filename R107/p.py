class ContadorPalabras:

    def __init__(self, archivo):
        self.archivo = archivo
        self.palabras = []
        
    def lector_archivo(self):
        with open(self.archivo, 'r') as archivo:
            for linea in archivo:
                for palabra in linea.split():
                    self.palabras.append(palabra)
    
    def contar_palabras(self):
        for palabra in self.palabras:
            i = 0
            i += 1
        return i
    
contador = ContadorPalabras('palabras.txt')
contador.lector_archivo()
resultado = contador.contar_palabras()
print(resultado)