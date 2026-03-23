# 🧪 Automação de Testes – Formulário de Certificação

Este projeto contém testes automatizados para o formulário disponível em:

https://qualidade.apprbs.com.br/certificacao

Os testes foram desenvolvidos utilizando **Python**, **Playwright** e **Pytest**, com foco na validação de campos obrigatórios e comportamento do formulário.

---

# 🚀 Tecnologias utilizadas

* Python
* Playwright
* Pytest
* Pytest-html (para geração de relatórios)

---

# 📂 Estrutura do Projeto

```
project
│
├── pages
│   └── certificacao_page.py
│
├── tests
│   ├── test_email_invalido.py
│   ├── test_telefone_invalido.py
│   ├── test_campos_obrigatorios.py
│   └── test_fluxo_completo.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# 🧩 Padrão de Projeto

O projeto utiliza o padrão **Page Object Model (POM)**, que separa:

* **Elementos e ações da página** (pasta `pages`)
* **Casos de teste** (pasta `tests`)

Isso melhora a organização, manutenção e reutilização do código.

---

# ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2️⃣ Entrar na pasta

```
cd seu-repositorio
```

### 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 4️⃣ Instalar Playwright

```
playwright install
```

### 5️⃣ Executar os testes

```
pytest -v
```

---

# 📊 Gerar relatório HTML

Para gerar um relatório automático da execução:

```
pytest --html=report.html
```

Após a execução, será gerado um arquivo `report.html` com os resultados dos testes.

---

# 🧪 Cenários de teste automatizados

Os seguintes cenários foram automatizados:

* Validação de **campos obrigatórios**
* Validação de **email inválido**
* Validação de **telefone inválido**
* Validação do **botão avançar**
* Execução do **fluxo básico do formulário**

---


# 🎯 Objetivo do projeto

Demonstrar habilidades em automação de testes web utilizando Playwright,
com foco em:

* Validação de formulários
* Escrita de testes robustos e reutilizáveis
* Aplicação de boas práticas de QA Automation
* Estrutura escalável com Page Object Model
---

# 👩‍💻 Autora

Vitória Tomazeli
QA Automation | Testes Automatizados
