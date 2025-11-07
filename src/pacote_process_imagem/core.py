from PIL import Image

def redimensionar_imagem(caminho_imagem, largura, altura, salvar_como=None):
    """Redimensiona uma imagem para as dimensões especificadas."""
    img = Image.open(caminho_imagem)
    img = img.resize((largura, altura))
    if salvar_como:
        img.save(salvar_como)
    return img

def converter_para_cinza(caminho_imagem, salvar_como=None):
    """Converte uma imagem para escala de cinza."""
    img = Image.open(caminho_imagem).convert("L")
    if salvar_como:
        img.save(salvar_como)
    return img
