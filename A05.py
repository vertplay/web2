from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import migration as db

app = Flask(__name__)

db.init()

@app.route('/')
def listar_usuarios():
    usuarios = db.listar_usuarios()
    return render_template('lista.html', usuarios=usuarios)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_usuarios():
    if request.method == 'POST':
        
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
       
        db.inserir_usuario(nome, email, senha)
       
        return redirect(url_for('listar_usuarios'))

    return render_template('formulario.html', acao='Adicionar')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuarios(id):
    usuario = db.buscar_usuario_por_id(id)

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        db.atualizar_usuario(id, nome, email, senha)

        return redirect(url_for('listar_usuarios'))

    return render_template('formulario.html', acao='Editar', usuario=usuario)

@app.route('/deletar/<int:id>')
def deletar_usuario(id):
    db.deletar_usuario(id)

    return redirect(url_for('listar_usuarios'))


if __name__ == '__main__':
    app.run(debug=True)
