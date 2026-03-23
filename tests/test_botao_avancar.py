from pages.certificacao_page import CertificacaoPage


def test_botao_avancar(page):

    certificacao = CertificacaoPage(page)

    certificacao.abrir()

    certificacao.preencher_nome("Gabriel")
    certificacao.preencher_telefone("11 98966-3131")
    certificacao.preencher_email("teste@gmail.com")

    certificacao.clicar_avancar()

    page.wait_for_timeout(2000)

    assert page.url != "https://qualidade.apprbs.com.br/certificacao"