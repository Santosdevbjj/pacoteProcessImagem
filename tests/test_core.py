from pacote_process_imagem.core import converter_para_cinza, redimensionar_imagem
from PIL import Image
import os

def test_converter_para_cinza(tmp_path):
    img = Image.new("RGB", (10, 10), color="red")
    caminho = tmp_path / "teste.jpg"
    img.save(caminho)
    saida = tmp_path / "saida.jpg"
    converter_para_cinza(caminho, saida)
    assert os.path.exists(saida)
