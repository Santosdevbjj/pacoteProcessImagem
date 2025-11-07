from pacote_process_imagem import redimensionar_imagem, converter_para_cinza, aplicar_filtro

def demo():
    """Demonstração do uso básico do pacote."""
    print("Executando demonstração...")
    imagem = "exemplo.jpg"

    redimensionar_imagem(imagem, 200, 200, "saida_redimensionada.jpg")
    converter_para_cinza(imagem, "saida_cinza.jpg")
    aplicar_filtro(imagem, "CONTOUR", "saida_filtro.jpg")

    print("Processamento concluído com sucesso!")
