from pages.certificacao_page import CertificacaoPage


def test_fluxo_completo(page):

    formulario = CertificacaoPage(page)

    formulario.abrir()

    formulario.preencher_nome("Gabriel")
    formulario.preencher_telefone("11988113737")
    formulario.preencher_email("teste@gmail.com")

    formulario.clicar_avancar()

    assert page.url != "https://qualidade.apprbs.com.br/certificacao"