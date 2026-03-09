from urllib import request
from urllib.error import URLError

lpo = ["coño", "bobo", "culiao", "pinche", "estupido", "estupida"]

def verificar_web(url):
    try:
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        f = request.urlopen(req)

    except URLError as e:
        return "Error al abrir la URL: " + str(e)

    else:
        contenido = f.read().decode("utf-8").lower()
        palabras = contenido.split()

        palabras_encontradas = []

        for insulto in lpo:
            for palabra in palabras:
                if insulto in palabra:
                    palabras_encontradas.append(insulto)

        if palabras_encontradas:
            return "Palabras ofensivas encontradas: " + str(set(palabras_encontradas))
        else:
            return "No se encontraron palabras ofensivas"

url = "https://www.esquire.com/es/actualidad/a17763828/insultos-graciosos-inteligentes-originales/"

print("Informe del sitio: ")
print(verificar_web(url))