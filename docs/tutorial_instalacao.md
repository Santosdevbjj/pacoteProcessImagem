# Tutorial de Instalação

## Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/Santosdevbjj/pacoteProcessImagem.git


---


  2. Instale as dependências:

pip install -r requirements.txt


3. Execute a demonstração:

python -m src.pacote_process_imagem.demo



---

### `docs/guia_publicacao_pypi.md`
```markdown
# Guia para Publicar no PyPI

1. Instale as ferramentas:
   ```bash
   python -m pip install --upgrade pip setuptools wheel twine

2. Gere as distribuições:

python setup.py sdist bdist_wheel


3. Faça upload para o Test PyPI:

python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*


4. Teste a instalação:

pip install --index-url https://test.pypi.org/simple/ pacote-process-imagem


5. Publique oficialmente:

python -m twine upload dist/*



---
