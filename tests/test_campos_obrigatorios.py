from pages.certificacao_page import CertificacaoPage



def test_campos_obrigatorios(page):

    formulario = CertificacaoPage(page)

    formulario.abrir()

    botao = formulario.botao_avancar()

    assert botao.is_disabled()