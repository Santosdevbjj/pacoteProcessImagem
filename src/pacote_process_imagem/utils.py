import os

def listar_imagens(pasta):
    """Lista os arquivos de imagem (.jpg, .png) de uma pasta."""
    return [f for f in os.listdir(pasta) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
