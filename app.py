from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route("/")
def inicio():
    consentimiento_cookies = request.cookies.get("consentimiento_cookies")
    return render_template("inicio.html", consentimiento_cookies=consentimiento_cookies)

@app.route("/administrar_cookies", methods=["GET", "POST"])
def administrar_cookies():
    if request.method == "POST":
        pass
    return render_template("administrar_cookies.html")


@app.route("/establecer_cookies", methods=["GET", "POST"])
def establecer_cookies():
    accion = request.form["accion"]
    respuesta = make_response(redirect(url_for("inicio")))
    if accion == "aceptar":
        respuesta.set_cookie("consentimiento_cookies", "aceptado", max_age=3600 )
    elif accion == "rechazar":
        respuesta.set_cookie("consentimiento_cookies", "rechazado", max_age=3600)
    return respuesta

@app.route("/restablecer_cookies", methods=["GET", "POST"])
def restablecer_cookies():
    respuesta = make_response(redirect(url_for("inicio")))
    respuesta.delete_cookie("consentimiento_cookies")
    return respuesta

if __name__ == '__main__':
    app.run()
