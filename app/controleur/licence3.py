from flask import Blueprint, render_template

main = Blueprint('licence3', __name__)

@main.route('/L3')
def licence1():
    return render_template('licence3.html', titre ="LicenceInfoLyon1 – LIL1")