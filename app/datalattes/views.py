from flask import render_template, redirect, url_for

from app.datalattes import datalattes_bp


@datalattes_bp.route('/', methods=['GET'])
@datalattes_bp.route('/index/', methods=['GET'])
def index():
    return redirect(url_for('datalattes_bp.home'))


@datalattes_bp.route('/home/', methods=['GET'])
def home():
    return render_template('index.html')


@datalattes_bp.route('/contato/', methods=['GET'])
def contato():
    return render_template('contato.html')


@datalattes_bp.route('/indicadores/', methods=['GET'])
def indicadores():
    return render_template('indicadores.html')


@datalattes_bp.route('/sobre/', methods=['GET'])
def sobre():
    return render_template('sobre.html')
