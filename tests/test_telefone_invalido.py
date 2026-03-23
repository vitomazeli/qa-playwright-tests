from pages.certificacao_page import CertificacaoPage


def test_telefone_invalido(page):

    formulario = CertificacaoPage(page)

    formulario.abrir()

    formulario.preencher_nome("Gabriel")
    formulario.preencher_telefone("123")
    formulario.preencher_email("teste@gmail.com")

    assert formulario.botao_avancar().is_disabled()