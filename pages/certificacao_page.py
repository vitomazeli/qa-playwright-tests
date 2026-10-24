
from playwright.sync_api import expect

URL = "https://qualidade.apprbs.com.br/certificacao"


class CertificacaoPage:
    def __init__(self, page):
        self.page = page

    def abrir(self):
        self.page.goto(URL)

    def preencher_nome(self, nome):
        self.page.locator(
            'input[name="pessoa.nome"]'
        ).fill(nome)

    def preencher_telefone(self, telefone):
        self.page.locator(
            'input[name="pessoa.telefonePrincipal"]'
        ).fill(telefone)

    def preencher_email(self, email):
        self.page.locator(
            'input[placeholder="email@exemplo.com"]'
        ).fill(email)

    
    def diagnosticar_campos(self):
        campos = {
            "nome": 'input[name="pessoa.nome"]',
            "telefone": 'input[name="pessoa.telefonePrincipal"]',
            "email": 'input[placeholder="email@exemplo.com"]',
        }

        for nome, seletor in campos.items():
            campo = self.page.locator(seletor)
            print(
                f"{nome}: valor={campo.input_value()!r}, "
                f"visivel={campo.is_visible()}, "
                f"habilitado={campo.is_enabled()}"
            )

        botao = self.botao_avancar()
        print("Botão habilitado:", botao.is_enabled())
        print("Botão HTML:", botao.evaluate("(el) => el.outerHTML"))


    def clicar_avancar(self):
        botao = self.botao_avancar()
        expect(botao).to_be_enabled()
        botao.click()

    def mensagem_email_invalido(self):
        return self.page.get_by_text(
            "Email inválido",
            exact=False
        )

    def botao_avancar(self):
        return self.page.locator("#rbBtnNext")
