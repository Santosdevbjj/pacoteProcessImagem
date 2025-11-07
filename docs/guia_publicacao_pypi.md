# 🚀 Guia Completo: Publicando seu Pacote no PyPI

Este guia explica como empacotar e publicar o projeto **pacoteProcessImagem** no **PyPI** — o repositório oficial de pacotes Python.

---

## 🧰 Pré-requisitos

Certifique-se de que você tem instalado:

```bash
python -m pip install --upgrade pip setuptools wheel twine

---
```

🏗️ **1. Gerar Distribuições**

Acesse a raiz do projeto e execute:

python setup.py sdist bdist_wheel

Isso criará a pasta dist/ contendo dois arquivos:

pacote_process_imagem-x.x.x.tar.gz

pacote_process_imagem-x.x.x-py3-none-any.whl



---

🧪 **2. Testar o Upload no TestPyPI**

Antes de publicar oficialmente, envie para o ambiente de testes do PyPI:

python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Durante o envio, você precisará inserir seu usuário e senha do TestPyPI.
Crie uma conta gratuita em: https://test.pypi.org/account/register/


---

🔍 **3. Testar Instalação pelo TestPyPI**

Depois de publicado, teste a instalação:

pip install --index-url https://test.pypi.org/simple/ pacote-process-imagem


---

🌐 **4. Publicar no PyPI Oficial**

Quando o pacote estiver pronto para o público:

python -m twine upload dist/*

Crie sua conta em: https://pypi.org/account/register/


---

✅ **5. Instalar o Pacote Publicado**

Após a publicação bem-sucedida:

pip install pacote-process-imagem


---

💡 **Dicas Extras**

Sempre atualize a versão no setup.py antes de publicar novamente.

Teste o pacote localmente antes do upload:

pip install .

Consulte a documentação oficial:

Setuptools

Twine

PyPI




---

📜 **Exemplo de Ciclo Completo**

# 1. Limpar builds anteriores
rm -rf build dist *.egg-info

# 2. Gerar nova distribuição
python setup.py sdist bdist_wheel

# 3. Testar no TestPyPI
python -m twine upload --repository testpypi dist/*

# 4. Publicar oficialmente
python -m twine upload dist/*


---

**Autor:** Sérgio Santos
Repositório: github.com/Santosdevbjj/pacoteProcessImagem
**Licença:** MIT License

---
