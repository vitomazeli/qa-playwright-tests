URL = "https://qualidade.apprbs.com.br/certificacao"

from playwright.sync_api import expect


class CertificacaoPage:

    def __init__(self, page):
        self.page = page

    def abrir(self):
        self.page.goto(URL)

    def preencher_nome(self, nome):
        self.page.fill('input[name="pessoa.nome"]', nome)

    def preencher_telefone(self, telefone):
        self.page.fill('input[name="pessoa.telefonePrincipal"]', telefone)

    def preencher_email(self, email):
        self.page.fill('input[placeholder="email@exemplo.com"]', email)

    def clicar_avancar(self):

        botao = self.page.locator("#rbBtnNext")

        expect(botao).to_be_enabled()

        botao.click()

    def mensagem_email_invalido(self):
        return self.page.locator("text=Email inválido")

    def botao_avancar(self):
        return self.page.locator("#rbBtnNext")