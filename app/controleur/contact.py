from flask import Blueprint, request, render_template, redirect, flash
import smtplib
from email.mime.text import MIMEText

main = Blueprint('contact', __name__)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

        msg = MIMEText(f"Message de {email}:\n\n{message}")
        msg['Subject'] = 'Message via LicenceInfoLyon1'
        msg['From'] = email
        msg['To'] = 'abc@gmail.com'

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ton_mail@gmail.com', 'mot_de_passe_app')
                smtp.send_message(msg)
            flash("Message envoyé avec succès !")
        except Exception as e:
            print(e)
            flash("Erreur lors de l'envoi du message.")

        return redirect('/contact')

    return render_template('contact.html')
