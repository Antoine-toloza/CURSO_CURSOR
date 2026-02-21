import re
from collections import Counter


class ContadorDePalabras:
    def __init__(self):
        self.texto = ""

    def leer_archivo(self, ruta: str) -> bool:
        """Lee el archivo de texto y guarda su contenido. Devuelve True si tuvo éxito."""
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                self.texto = f.read()
            return True
        except FileNotFoundError:
            print("El archivo no existe.")
            return False
        except OSError:
            print("La ruta del archivo no es válida.")
            return False

    def contar_palabras(self) -> tuple[int, list[tuple[str, int]]]:
        """
        Cuenta las palabras en el texto leído.
        Devuelve (total_palabras, lista de las 10 palabras más frecuentes).
        """
        palabras = re.findall(r"\w+", self.texto.lower())
        total_palabras = len(palabras)
        contador = Counter(palabras)
        mas_comunes = contador.most_common(10)
        return total_palabras, mas_comunes


# Uso del contador
if __name__ == "__main__":
    archivo = input("Ingrese la ruta del archivo de texto: ")
    contador = ContadorDePalabras()

    if contador.leer_archivo(archivo):
        total, mas_comunes = contador.contar_palabras()
        print(f"El archivo tiene {total} palabras.")
        print("Las 10 palabras más frecuentes son:")
        for palabra, freq in mas_comunes:
            print(f"{palabra}: {freq}")
