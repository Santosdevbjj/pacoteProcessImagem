# Criando um Pacote de Processamento de Imagens com Python.


....


---




## 🧠 README.md (profissional e didático)

```markdown
# 🖼️ pacoteProcessImagem

Pacote Python desenvolvido por **Sérgio Santos** para **processamento básico de imagens**, com funções para redimensionamento, conversão em tons de cinza e aplicação de filtros simples.

---
```

## 🚀 Tecnologias Utilizadas
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

🪪 **Licença**

Este projeto está licenciado sob a MIT License.

---


