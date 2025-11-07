import os
from pacote_process_imagem.utils import listar_imagens

def test_listar_imagens(tmp_path):
    """Testa se apenas arquivos de imagem são listados."""
    (tmp_path / "foto1.jpg").touch()
    (tmp_path / "foto2.png").touch()
    (tmp_path / "documento.txt").touch()

    imagens = listar_imagens(tmp_path)

    assert "foto1.jpg" in imagens
    assert "foto2.png" in imagens
    assert "documento.txt" not in imagens

def test_lista_vazia(tmp_path):
    """Testa retorno quando não há imagens."""
    resultado = listar_imagens(tmp_path)
    assert resultado == []
