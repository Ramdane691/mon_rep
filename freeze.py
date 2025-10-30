# freeze.py
from flask_frozen import Freezer

# Cas 1: ton app Flask est directement "app" dans app/__init__.py
from app import app as flask_app

# # Cas 2 (factory) : décommente et adapte
# from app import create_app
# flask_app = create_app()

flask_app.config['FREEZER_BASE_URL'] = '/'          # URLs relatives
flask_app.config['FREEZER_DESTINATION'] = 'build'   # dossier de sortie
flask_app.config['FREEZER_REMOVE_EXTRA_FILES'] = True

freezer = Freezer(flask_app)

# Exemple de générateurs si tu as des routes dynamiques avec variables.
# Décommente/édite si besoin :
# @freezer.register_generator
# def ue_l1():
#     # si tu avais une route de type /ue_l1/<slug>
#     for slug in ["lifami", "lifapi", "programation_recurcive", "unix"]:
#         yield {'slug': slug}

if __name__ == "__main__":
    freezer.freeze()
