import os
from PyPDF2 import PdfReader, PdfWriter

w = os.walk("/home/user/...") # Percorso della cartella scelta

listaFile = {}
listaNomiFile = {}

nuovoTitolo = ""

i = 0

for root, dirs, files in w:
    for name in files:
        if name[-4:].lower() == ".pdf":
            listaFile[i] = os.path.join(root, name)
            listaNomiFile[i] = name[:-4].replace("-", " ").upper()
            i += 1

for indice in listaFile:
    print("File: " + listaFile[indice])
    pdf = PdfReader(listaFile[indice])
    meta = pdf.metadata
    print("   Titolo: " + str(meta.title))
    inputText = input("   Nuovo titolo [INVIO per saltare, 'q' per terminare], 't' per usare '"+ listaNomiFile[indice] +"': ")
    if( inputText != ""):
        if( inputText == "q"): exit(0)

        if (inputText == "t"):
            nuovoTitolo = listaNomiFile[indice]
        else:
            nuovoTitolo = inputText

        writer = PdfWriter()
        pdf = PdfReader(listaFile[indice])

        writer.append_pages_from_reader(pdf)
        metadata = pdf.metadata
        writer.add_metadata(metadata)

        writer.add_metadata({"/Title": nuovoTitolo})

        with open(listaFile[indice], "wb") as fp:
            writer.write(fp)

        print("   Titolo salvato!")

