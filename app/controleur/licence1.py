from flask import Blueprint, render_template

main = Blueprint('licence1', __name__)

@main.route('/L1/')
def licence1():
    return render_template('licence1.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L1/unix/')
def ue_unix():
    return render_template('ue_l1/unix.html', titre="UE UNIX (Linux)")

@main.route('/L1/algorithmique/')
def ue_algo():
    return render_template('ue_l1/lifapi.html', titre="Algorithmique et Programmation Impérative")

@main.route('/L1/recursif/')
def ue_prog_recur():
    return render_template('ue_l1/programation_recurcive.html', titre="Programmation Récursive et Algorithmique Avancée")


@main.route('/L1/lifami/')
def ue_lifami():
    return render_template('ue_l1/lifami.html', titre="Applucation Math/info")