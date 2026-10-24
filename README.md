# 🧪 Automação de Testes — Formulário de Certificação

Projeto de automação de testes web desenvolvido com **Python, Playwright e Pytest**, com foco na validação de formulários, organização dos testes e investigação de defeitos.

**Aplicação testada:** [Formulário de Certificação](https://qualidade.apprbs.com.br/certificacao)

## 🚀 Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Playwright** — automação de navegadores.
- **Pytest** — execução e organização dos testes automatizados.
- **pytest-html** — geração de relatórios HTML.

## 📂 Estrutura do projeto

```text
qa-playwright-tests/
├── pages/
│   └── certificacao_page.py
├── tests/
│   ├── test_botao_avancar.py
│   ├── test_campos_obrigatorios.py
│   ├── test_email_invalido.py
│   ├── test_fluxo_completo.py
│   └── test_telefone_invalido.py
├── assets/
├── fixtures/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## 🧩 Padrão de projeto: Page Object Model

O projeto utiliza o padrão **Page Object Model (POM)** para separar as ações e os elementos da página dos casos de teste.

- `pages/`: concentra os métodos de interação com o formulário.
- `tests/`: contém os cenários de teste automatizados.
- `conftest.py`: configurações e fixtures compartilhadas do Pytest.
- `pytest.ini`: configuração da descoberta dos testes.
- `requirements.txt`: dependências necessárias para executar o projeto.

Essa organização favorece a reutilização de código e facilita a manutenção dos testes.

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/vitomazeli/qa-playwright-tests.git
cd qa-playwright-tests
```

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Instalar os navegadores do Playwright

```bash
python -m playwright install
```

### 5. Executar os testes

```bash
python -m pytest tests/ -v
```

## 📊 Relatório HTML

Para gerar um relatório da execução dos testes:

```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

Após a execução, abra o arquivo `report.html` no navegador para consultar os resultados.

## 🧪 Cenários de teste

O projeto contempla cenários relacionados a:

- Campos obrigatórios.
- E-mail inválido.
- Telefone inválido.
- Estado do botão “Avançar”.
- Fluxo básico do formulário.

**Status dos testes:** os cenários estão em desenvolvimento e validação. Durante a investigação, foram identificados erros JavaScript na aplicação que podem impedir o avanço do formulário. Os resultados devem ser consultados nas execuções mais recentes do Pytest.

## 🐞 Investigação de defeitos

Foi aberta uma issue para documentar o comportamento observado durante os testes:

- [Issue #1 — Botão Avançar permanece desabilitado](https://github.com/vitomazeli/qa-playwright-tests/issues/1)

A investigação registrou erros JavaScript e o estado desabilitado do botão após o preenchimento dos campos. A causa raiz ainda precisa ser confirmada.

## 🎯 Objetivos de aprendizagem

Este projeto demonstra a prática de:

- Automação de testes de interface web.
- Validação de formulários.
- Organização de testes com Pytest.
- Aplicação do padrão Page Object Model.
- Investigação e documentação de defeitos.
- Coleta e análise de evidências durante a execução dos testes.

## 👩‍💻 Autora

**Vitória Tomazeli**  
QA Automation | Testes Automatizados

[GitHub](https://github.com/vitomazeli)