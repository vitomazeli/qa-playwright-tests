from pages.certificacao_page import CertificacaoPage

def test_email_invalido(page):

    formulario = CertificacaoPage(page)

    formulario.abrir()

    formulario.preencher_nome("Gabriel")

    formulario.preencher_telefone("11988113737")

    formulario.preencher_email("emailinvalido")

    formulario.clicar_avancar()

    erro = page.locator("text=inválido")

    assert erro.is_visible()