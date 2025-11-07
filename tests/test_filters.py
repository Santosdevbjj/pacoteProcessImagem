import os
from PIL import Image
from pacote_process_imagem.filters import aplicar_filtro

def test_aplicar_filtro_blur(tmp_path):
    """Testa aplicação do filtro BLUR."""
    img = Image.new("RGB", (10, 10), color="blue")
    caminho = tmp_path / "teste.jpg"
    img.save(caminho)

    saida = tmp_path / "saida_blur.jpg"
    aplicar_filtro(caminho, "BLUR", saida)

    assert os.path.exists(saida)
    assert Image.open(saida).size == (10, 10)

def test_aplicar_filtro_contour(tmp_path):
    """Testa aplicação do filtro CONTOUR."""
    img = Image.new("RGB", (10, 10), color="green")
    caminho = tmp_path / "teste.jpg"
    img.save(caminho)

    saida = tmp_path / "saida_contour.jpg"
    aplicar_filtro(caminho, "CONTOUR", saida)

    assert os.path.exists(saida)
    assert Image.open(saida).size == (10, 10)

def test_aplicar_filtro_invalido(tmp_path):
    """Testa filtro inválido — deve aplicar padrão (BLUR)."""
    img = Image.new("RGB", (10, 10), color="red")
    caminho = tmp_path / "teste.jpg"
    img.save(caminho)

    saida = tmp_path / "saida_invalido.jpg"
    aplicar_filtro(caminho, "INVALIDO", saida)

    assert os.path.exists(saida)
