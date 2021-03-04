from flask import render_template, redirect, url_for
from app.datalattes import datalattes_bp


@datalattes_bp.route('/', methods=['GET'])
@datalattes_bp.route('/index/', methods=['GET'])
def index():

    return redirect(url_for('datalattes_bp.home'))


@datalattes_bp.route('/home/', methods=['GET'])
def home():
    return render_template('home.html')


@datalattes_bp.route('/vis1/', methods=['GET'])
def contato():
    return render_template('grafico1.html')


@datalattes_bp.route('/vis2/', methods=['GET'])
def indicadores():
    return render_template('grafico2.html')


@datalattes_bp.route('/vis3/', methods=['GET'])
def sobre():
    return render_template('grafico3.html')
