@app_sorvetunes.route("/deletar/<int:id>")
def deletar(id):
    user = Log.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin'))