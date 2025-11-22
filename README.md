# Criando um Pacote de Processamento de Imagens com Python.


![SuzanoPython003](https://github.com/user-attachments/assets/171946bf-d9f2-4ade-8213-b16500fec681)


**Bootcamp Suzano - Python Developer #2**



---

**DESCRIÇÃO:** 

Neste projeto você aprenderá a criar o seu primeiro pacote de processamento de imagens em Python e disponibilizá-lo no repositório Pypi. 

Assim você poderá reutilizá-lo facilmente e compartilhá-lo com outras pessoas. 


---



🖼️ **pacoteProcessImagem**

Pacote Python desenvolvido por **Sérgio Santos** para **processamento básico de imagens**, com funções para redimensionamento, conversão em tons de cinza e aplicação de filtros simples.

---


## 🚀 **Tecnologias Utilizadas**
- **Python 3.8+**
- **Pillow (PIL Fork)**
- **Pytest**
- **Setuptools e Twine (para empacotamento e publicação)**

---

## ⚙️ Requisitos de Hardware e Software
| Requisito | Especificação mínima |
|------------|----------------------|
| Sistema Operacional | Windows, Linux ou macOS |
| Python | 3.8 ou superior |
| Memória RAM | 4 GB |
| Disco | 200 MB livres |
| Dependências | Pillow, Pytest |

---

## 📦 Estrutura do Projeto

<img width="947" height="1107" alt="Screenshot_20251107-143559" src="https://github.com/user-attachments/assets/6a08ff86-9949-4dc1-9b4a-b4a4c5ed0458" />

---


## 🧰 Instalação
```bash
git clone https://github.com/Santosdevbjj/pacoteProcessImagem.git
cd pacoteProcessImagem
pip install -r requirements.txt


---
```

🧪 **Testes**

pytest tests/


---

🖥️ **Uso Básico**

from pacote_process_imagem import redimensionar_imagem, converter_para_cinza, aplicar_filtro

redimensionar_imagem("foto.jpg", 200, 200, "foto_menor.jpg")
converter_para_cinza("foto.jpg", "foto_pb.jpg")
aplicar_filtro("foto.jpg", "CONTOUR", "foto_filtro.jpg")


---

📘 **Publicação no PyPI**

Consulte o guia completo em docs/guia_publicacao_pypi.md






---

# 🧱 Estrutura Detalhada do Projeto

A seguir está a explicação de cada arquivo e pasta do repositório **`pacoteProcessImagem`**, descrevendo sua função e importância dentro do pacote Python.

---

## ⚙️ Arquivos de Configuração e Empacotamento

### 🧩 `.gitignore`
Define quais arquivos e pastas o **Git deve ignorar** durante o versionamento.  
Isso mantém o repositório limpo, sem arquivos temporários, caches, logs, ambientes virtuais ou configurações locais de IDEs.  
Principais exemplos:
- `__pycache__/`, `.pytest_cache/`, `.venv/`
- `dist/`, `build/`, `*.egg-info/`
- `.vscode/`, `.idea/`, `.DS_Store`

---

### ⚙️ `setup.py`
É o **núcleo do empacotamento Python**.  
Define as informações do projeto, dependências, autor, versão e parâmetros necessários para gerar e instalar o pacote.  
Usado para criar distribuições e publicar no PyPI com `setuptools` e `twine`.

**Principais campos:**
- `name` — nome oficial do pacote (ex.: `pacote-process-imagem`)
- `version` — controle de versão semântico
- `install_requires` — dependências (ex.: Pillow)
- `packages` — localização do código-fonte

---

### 📦 `requirements.txt`
Lista todas as **bibliotecas externas** necessárias para rodar o projeto.  
Facilita a instalação com um único comando:

```bash
pip install -r requirements.txt


---

```


**Inclui:**

Pillow → manipulação de imagens

pytest → testes automatizados



---

📜 **MANIFEST.in**

Garante que arquivos não-Python também sejam incluídos nas distribuições, como:

README.md

LICENSE

Pastas src/ e tests/


Sem esse arquivo, apenas o código-fonte puro seria empacotado, omitindo a documentação e os testes.


---

• **Código-Fonte do Pacote**

📁 **src/pacote_process_imagem/__init__.py**

Identifica o diretório como um pacote Python e torna públicas as funções principais.
Permite importar diretamente de forma simplificada:

from pacote_process_imagem import redimensionar_imagem

Também define metadados como __version__ e __author__.


---

🧮 **src/pacote_process_imagem/core.py**

Contém as funções centrais de processamento de imagens:

redimensionar_imagem() → altera as dimensões da imagem

converter_para_cinza() → transforma a imagem para escala de cinza


Usa a biblioteca Pillow e manipula objetos Image para abrir, processar e salvar arquivos.


---

🎨 **src/pacote_process_imagem/filters.py**

Responsável por aplicar filtros visuais nas imagens com o módulo ImageFilter do Pillow.

Função principal:

aplicar_filtro(caminho, filtro="BLUR", salvar_como=None)

Filtros disponíveis: BLUR, CONTOUR, DETAIL, EDGE_ENHANCE.
Filtros inválidos são tratados automaticamente como BLUR.


---

🧰 **src/pacote_process_imagem/utils.py**

Contém funções auxiliares de apoio ao pacote.

Função implementada:

listar_imagens(pasta) → retorna uma lista de imagens (.jpg, .png, .jpeg) dentro de um diretório.


Essencial para automações e execução em lote.


---

🧪 **src/pacote_process_imagem/demo.py**

Demonstra o uso prático do pacote.
Quando executado, processa uma imagem de exemplo com todas as funções principais:

python -m src.pacote_process_imagem.demo

Gera os arquivos de saída:

saida_redimensionada.jpg

saida_cinza.jpg

saida_filtro.jpg


É ideal para testar rapidamente o funcionamento do pacote.


---

🧾 **Testes Automatizados**

🧩 **tests/__init__.py**

Indica que a pasta tests é um pacote Python.
Permite que o pytest detecte automaticamente todos os arquivos de teste.


---

🧪 **tests/test_core.py**

Verifica as funções do módulo core.py, garantindo que:

As imagens sejam corretamente convertidas para cinza;

O redimensionamento funcione e gere novos arquivos.


Usa imagens temporárias criadas com o Pillow para testes limpos e independentes.


---

🧪 **tests/test_filters.py**

Valida o módulo filters.py, testando:

Aplicação de filtros válidos (BLUR, CONTOUR);

Comportamento com filtros inválidos (uso padrão BLUR);

Existência dos arquivos gerados.


Garante a estabilidade do pipeline visual do pacote.


---

🧪 **tests/test_utils.py**

Confere o funcionamento do módulo utils.py, assegurando que:

Apenas arquivos de imagem sejam listados;

Arquivos não suportados sejam ignorados;

O retorno seja correto em diretórios vazios.


Esses testes confirmam a precisão e previsibilidade das funções auxiliares.


---

📘 **Documentação Técnica**

📗 **docs/tutorial_instalacao.md**

Guia rápido para instalação e uso do pacote localmente.

Passos principais:

1. Clonar o repositório


2. Instalar dependências


3. Executar a demonstração



Ideal para quem está conhecendo o projeto pela primeira vez.


---

📘 **docs/guia_publicacao_pypi.md**

Manual completo para empacotar e publicar o projeto no PyPI.
Contém instruções passo a passo para:

Criar as distribuições (sdist, wheel);

Testar no TestPyPI;

Publicar oficialmente no PyPI;

Verificar instalação e versionamento.


Inclui comandos práticos e boas práticas de manutenção e automação.


---

🧭 **Resumo Geral**

Categoria	Arquivo	Descrição

🧩 Configuração	.gitignore, setup.py, requirements.txt, MANIFEST.in	Controle, empacotamento e dependências
🧠 Código-fonte	__init__.py, core.py, filters.py, utils.py, demo.py	Implementação e exemplos de uso
🧪 Testes	test_core.py, test_filters.py, test_utils.py	Garantia de qualidade e integridade
📘 Documentação	tutorial_instalacao.md, guia_publicacao_pypi.md	Guias de uso, instalação e publicação



---

> 🏁 **Conclusão:**
O projeto pacoteProcessImagem foi estruturado seguindo boas práticas de engenharia de software em Python, com foco em modularidade, testabilidade, empacotamento e documentação completa.
Essa organização facilita o aprendizado, o reuso e a publicação profissional de pacotes Python no PyPI.




---






🪪 **Licença**

Este projeto está licenciado sob a MIT License.

---
**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 



