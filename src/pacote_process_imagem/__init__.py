"""
Pacote de Processamento de Imagens - pacote_process_imagem

Funções principais disponíveis:
- redimensionar_imagem
- converter_para_cinza
- aplicar_filtro
"""

from .core import redimensionar_imagem, converter_para_cinza
from .filters import aplicar_filtro

__version__ = "0.1.0"
__author__ = "Sérgio Santos"
