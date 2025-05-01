from flask import Blueprint, render_template

main = Blueprint('licence2', __name__)

@main.route('/L2')
def licence1():
    return render_template('licence2.html', titre ="LicenceInfoLyon1 – LIL1")