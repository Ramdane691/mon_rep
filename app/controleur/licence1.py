from flask import Blueprint, render_template

main = Blueprint('licence1', __name__)

@main.route('/L1')
def licence1():
    return render_template('licence1.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L1/unix')
def ue_unix():
    return render_template('ue_l1/unix.html', titre="UE UNIX (Linux)")

@main.route('/L1/algorithmique')
def ue_algo():
    return render_template('ue_l1/lifapi.html', titre="Algorithmique et Programmation Impérative")

