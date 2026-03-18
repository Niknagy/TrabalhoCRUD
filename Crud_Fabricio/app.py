import os

from flask import Flask, redirect, render_template, request, url_for

from database import (
    atualizar_frete,
    buscar_frete_por_id,
    criar_frete,
    excluir_frete,
    init_db,
    listar_fretes,
)

app = Flask(__name__)


@app.route("/")
def tela_principal():
    return render_template("index.html")


@app.route("/consultar")
def tela_consultar():
    fretes = listar_fretes()
    return render_template("consultar.html", fretes=fretes)


@app.route("/inserir", methods=["GET", "POST"])
def tela_inserir():
    mensagem = ""

    if request.method == "POST":
        valor_texto = request.form.get("valor", "0").strip().replace(",", ".")
        try:
            valor = float(valor_texto)
        except ValueError:
            mensagem = "Valor invalido. Use um numero, por exemplo 1500.75"
            return render_template("inserir.html", mensagem=mensagem)

        frete_id = criar_frete(
            request.form.get("caminhao", "").strip(),
            request.form.get("motorista", "").strip(),
            request.form.get("origem", "").strip(),
            request.form.get("destino", "").strip(),
            request.form.get("carga", "").strip(),
            valor,
            request.form.get("status", "").strip(),
            request.form.get("data_entrega", "").strip(),
        )
        mensagem = f"Frete cadastrado com sucesso. ID: {frete_id}"

    return render_template("inserir.html", mensagem=mensagem)


@app.route("/excluir", methods=["GET", "POST"])
def tela_excluir():
    mensagem = ""
    frete = None

    if request.method == "POST":
        acao = request.form.get("acao", "buscar")
        frete_id_texto = request.form.get("frete_id", "").strip()

        if not frete_id_texto.isdigit():
            mensagem = "Digite um ID valido (numero inteiro)."
            return render_template("excluir.html", mensagem=mensagem, frete=frete)

        frete_id = int(frete_id_texto)
        frete = buscar_frete_por_id(frete_id)

        if not frete:
            mensagem = "Frete nao encontrado."
            return render_template("excluir.html", mensagem=mensagem, frete=frete)

        if acao == "excluir":
            if excluir_frete(frete_id):
                mensagem = "Frete excluido com sucesso."
                frete = None
            else:
                mensagem = "Nao foi possivel excluir o frete."

    return render_template("excluir.html", mensagem=mensagem, frete=frete)


@app.route("/atualizar", methods=["GET", "POST"])
def tela_atualizar():
    mensagem = ""
    frete = None

    if request.method == "POST":
        acao = request.form.get("acao", "buscar")
        frete_id_texto = request.form.get("frete_id", "").strip()

        if not frete_id_texto.isdigit():
            mensagem = "Digite um ID valido (numero inteiro)."
            return render_template("atualizar.html", mensagem=mensagem, frete=frete)

        frete_id = int(frete_id_texto)
        frete = buscar_frete_por_id(frete_id)

        if not frete:
            mensagem = "Frete nao encontrado."
            return render_template("atualizar.html", mensagem=mensagem, frete=frete)

        if acao == "salvar":
            valor_texto = request.form.get("valor", "0").strip().replace(",", ".")
            try:
                valor = float(valor_texto)
            except ValueError:
                mensagem = "Valor invalido. Use um numero, por exemplo 1500.75"
                return render_template("atualizar.html", mensagem=mensagem, frete=frete)

            ok = atualizar_frete(
                frete_id,
                request.form.get("caminhao", "").strip(),
                request.form.get("motorista", "").strip(),
                request.form.get("origem", "").strip(),
                request.form.get("destino", "").strip(),
                request.form.get("carga", "").strip(),
                valor,
                request.form.get("status", "").strip(),
                request.form.get("data_entrega", "").strip(),
            )

            if ok:
                mensagem = "Frete atualizado com sucesso."
                frete = buscar_frete_por_id(frete_id)
            else:
                mensagem = "Nao foi possivel atualizar o frete."

    return render_template("atualizar.html", mensagem=mensagem, frete=frete)


@app.route("/voltar")
def voltar_inicio():
    return redirect(url_for("tela_principal"))


if __name__ == "__main__":
    init_db()
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
