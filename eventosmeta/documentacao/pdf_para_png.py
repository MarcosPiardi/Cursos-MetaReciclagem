import pymupdf

doc = pymupdf.open("RecuperacaoSenha.pdf")
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(dpi=200)
    pix.save(f"pagina_{i}.png")
print(f"Gerados {len(doc)} arquivos .png")