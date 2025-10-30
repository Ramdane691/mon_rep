# freeze.py
import os
import shutil
from flask_frozen import Freezer
from app import create_app

# --- Création de l'app ---
flask_app = create_app()

# --- Configuration Frozen-Flask ---
flask_app.config['FREEZER_BASE_URL'] = '/'
flask_app.config['FREEZER_DESTINATION'] = os.path.join(os.path.dirname(__file__), 'build')  # chemin absolu
flask_app.config['FREEZER_REMOVE_EXTRA_FILES'] = True
flask_app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
flask_app.config['FREEZER_RELATIVE_URLS'] = True
flask_app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

# --- Vérification des routes disponibles ---
with flask_app.app_context():
    print("=== ROUTES DETECTEES ===")
    for rule in flask_app.url_map.iter_rules():
        print(f"{rule.methods} -> {rule.rule}")


if os.path.exists(flask_app.config['FREEZER_DESTINATION']):
    shutil.rmtree(flask_app.config['FREEZER_DESTINATION'])

# --- Création du Freezer ---
freezer = Freezer(flask_app)

# --- Liste explicite des routes à geler ---
@freezer.register_generator
def static_routes():
    yield '/'
    yield '/L1/'
    yield '/L1/unix/'
    yield '/L1/algorithmique/'
    yield '/L1/recursif/'
    yield '/L1/lifami/'
    yield '/L2/'
    yield '/L2/lifapsd/'
    yield '/L2/lifarchi/'
    yield '/L2/stat/'
    yield '/L2/lifapcd/'
    yield '/L2/bdw/'
    yield '/L2/pf/'
    yield '/L2/lifse/'
    yield '/L3/'
    yield '/L3/lifpca/'
    yield '/L3/lifpoo/'
    yield '/L3/lifweb/'
    yield '/apropos/'
    yield '/contact/'

# --- Lancement du freeze ---
if __name__ == "__main__":
    print(f"📦 Dossier de sortie : {flask_app.config['FREEZER_DESTINATION']}")
    freezer.freeze()
