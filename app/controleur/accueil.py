from flask import Blueprint, render_template

main = Blueprint('accueil', __name__)

@main.route('/')
def accueil():
    return render_template('accueil.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/apropos')
def apropos():
    return render_template('apropos.html', titre ="LicenceInfoLyon1 – LIL1")