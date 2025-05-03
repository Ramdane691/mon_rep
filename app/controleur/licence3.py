from flask import Blueprint, render_template

main = Blueprint('licence3', __name__)

@main.route('/L3')
def licence1():
    return render_template('licence3.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L3/lifpca')
def lifpca():
    return render_template('ue_l3/lifpca.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L3/lifpoo')
def lifpoo():
    return render_template('ue_l3/lifpoo.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L3/lifweb')
def lifweb():
    return render_template('ue_l3/lifweb.html', titre ="LicenceInfoLyon1 – LIL1")