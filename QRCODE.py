import pyqrcode as pqr
import png
import io
url=pqr.create("https://conteudo.univem.edu.br/11a-olimpiada-de-informatica/")
with open('code.png','w') as fstream:
    url.png('code.png',scale=5)
url.png("code.png",scale=5)
buffer=io.BytesIO()
url.png(buffer)
print(list(buffer.getvalue()))