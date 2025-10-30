from flask import Blueprint, render_template

main = Blueprint('licence2', __name__)

@main.route('/L2/')
def licence1():
    return render_template('licence2.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/lifapsd/')
def lifapsd():
    return render_template('ue_l2/lifapsd.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/lifarchi/')
def lifarchi():
    return render_template('ue_l2/lifarchi.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/stat/')
def stat():
    return render_template('ue_l2/stat.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/lifapcd/')
def lifapcd():
    return render_template('ue_l2/lifapcd.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/bdw/')
def bdw():
    return render_template('ue_l2/bdw.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/pf/')
def pf():
    return render_template('ue_l2/pf.html', titre ="LicenceInfoLyon1 – LIL1")

@main.route('/L2/lifse/')
def lifse():
    return render_template('ue_l2/lifse.html', titre ="LicenceInfoLyon1 – LIL1")