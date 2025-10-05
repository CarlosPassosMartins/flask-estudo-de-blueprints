from flask import Blueprint, render_template, redirect, url_for, request, session
from data import Data

auth_bp = Blueprint('auth', __name__, template_folder='template', static_folder='static', static_url_path='/auth/static')


#LOGIN

@auth_bp.route('/')
def ver_login():
    if session.get('id') != None:
        return redirect(url_for('home.home'))
    return redirect(url_for('auth.login_get'))

@auth_bp.route('/login')
def login_get():
    return render_template('login_form.html')

@auth_bp.route('/login', methods=['POST'])
def login_post():

    name = request.form.get('nome')
    senha = request.form.get('senha')

    for user in Data:
        if user['nome'] == name and user['senha'] == senha:
            session['id'] = user['id']
            return redirect(url_for('home.home'))
    return '<h1>ERRO</h1> <p> nome de usuario ou senha errados <a href="/"> voltar </a> </p>'

@auth_bp.route('/cadastro', methods=['POST'])
def cadastro():
    name = request.form.get('nome')
    senha = request.form.get('senha')

    for user in Data:
        if user['nome'] == name:
            return 'nome invalido <a href="/"> voltar para o login </a>'
        
    Data.append({
    'id': len(Data) + 1,
    'nome': name,
    'senha': senha
    })
    return redirect(url_for('auth.login_get'))

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session['id'] = None
    return redirect(url_for('auth.login_get'))


# LISTA

@auth_bp.route('/lista')
def lista():
    return Data
    
    
