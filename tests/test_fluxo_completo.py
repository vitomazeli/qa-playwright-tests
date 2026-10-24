
from pages.certificacao_page import CertificacaoPage


def test_fluxo_completo(page):
    formulario = CertificacaoPage(page)
    erros_js = []
    
    requisicoes_falhas = []

    page.on(
        "requestfailed",
        lambda request: requisicoes_falhas.append(
            f"{request.url} | {request.failure}"
        )
    )


    page.on(
        "pageerror",
        lambda erro: erros_js.append(str(erro))
    )

    formulario.abrir()

    print("\n--- Diagnóstico JavaScript ---")
    print(
        "ActionsForm:",
        page.evaluate("typeof window.ActionsForm")
    )

    print(
        "goToNextStage:",
        page.evaluate(
            "typeof window.ActionsForm?.goToNextStage"
        )
    )

    formulario.preencher_nome("Gabriel")
    formulario.preencher_telefone("11988113737")
    formulario.preencher_email("teste@gmail.com")

    formulario.diagnosticar_campos()

    print("\n--- Erros JavaScript ---")
    if erros_js:
        for erro in erros_js:
            print(erro)
    else:
        print("Nenhum erro JavaScript capturado.")

    
    print("\n--- Requisições que falharam ---")

    if requisicoes_falhas:
        for falha in requisicoes_falhas:
            print(falha)
    else:
        print("Nenhuma requisição com falha registrada.")

