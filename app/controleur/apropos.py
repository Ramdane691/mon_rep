
from flask import Blueprint, render_template

main = Blueprint('apropos', __name__)

@main.route('/apropos')
def apropos():
    return render_template('apropos.html', titre ="LicenceInfoLyon1 – LIL1")