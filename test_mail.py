import smtplib
from email.mime.text import MIMEText

TON_EMAIL = "r.amaouz02@gmail.com"
MOT_DE_PASSE_APP = "njpnarthxjiotprr"  # <--- sans espace !!

msg = MIMEText("Ceci est un test depuis un script Python.")
msg['Subject'] = "Test de mail simple"
msg['From'] = TON_EMAIL
msg['To'] = TON_EMAIL

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(TON_EMAIL, MOT_DE_PASSE_APP)
        smtp.send_message(msg)
    print("✅ Mail envoyé avec succès.")
except Exception as e:
    print("❌ Erreur :", e)
