from PIL import Image, ImageFilter

def aplicar_filtro(caminho_imagem, filtro="BLUR", salvar_como=None):
    """Aplica um filtro simples à imagem."""
    img = Image.open(caminho_imagem)
    filtros = {
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
    }
    img = img.filter(filtros.get(filtro, ImageFilter.BLUR))
    if salvar_como:
        img.save(salvar_como)
    return img
