from flask import Blueprint, request, render_template, redirect, flash
import smtplib
from email.mime.text import MIMEText

main = Blueprint('contact', __name__)

# 💌 Config Gmail
TON_EMAIL = "r.amaouz02@gmail.com"
MOT_DE_PASSE_APP = "njpnarthxjiotprr"  # Mot de passe d’application généré via Google

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    print("🛎️ Route /contact appelée")

    if request.method == 'POST':
        print("📩 Requête POST reçue")
        email_utilisateur = request.form['email']
        message_utilisateur = request.form['message']

        print("✉️ Email saisi :", email_utilisateur)
        print("📝 Message saisi :", message_utilisateur)

        ...

        # Tu composes le mail que TOI tu recevras
        contenu = f"Tu as reçu un message via LicenceInfoLyon1 !\n\n" \
                  f"De : {email_utilisateur}\n\n" \
                  f"Message :\n{message_utilisateur}"

        msg = MIMEText(contenu)
        msg['Subject'] = '📩 Nouveau message via LicenceInfoLyon1'
        msg['From'] = TON_EMAIL  # L’adresse de connexion SMTP (ton Gmail)
        msg['To'] = TON_EMAIL    # Tu le reçois aussi

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(TON_EMAIL, MOT_DE_PASSE_APP)
                smtp.send_message(msg)

            flash("Ton message a bien été envoyé, merci !")
        except Exception as e:
            print("Erreur :", e)
            flash("Oups ! Une erreur est survenue.")

        return redirect('/contact')

    return render_template('contact.html')









