from flask import Flask

def create_app():
    app = Flask(__name__)

    from .controleur.accueil import main as accueil_main
    from .controleur.licence1 import main as licence1_main
    from .controleur.licence2 import main as licence2_main
    from .controleur.licence3 import main as licence3_main

 #   from .controleur.licence1 import main

    app.register_blueprint(accueil_main)
    app.register_blueprint(licence1_main)
    app.register_blueprint(licence2_main)
    app.register_blueprint(licence3_main)
    
    return app