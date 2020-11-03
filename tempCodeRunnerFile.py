@app_sorvetunes.route("/form", methods=["PUT", "POST"])
def form():
    usuarios = Log.query.all()
    print(usuarios)
    login = request.form['usuarioform']
    password = request.form['senhaform']
    for user in usuarios:
        if user['usuario'] == login and user['senha'] == password:
            return render_template("index.html", login=login)
    return render_template("login.html", mensagem = "Login inválido.")