from flask import Flask

def create_app():
    app = Flask(__name__)

    from .controleur.accueil import main as accueil_main
    from .controleur.licence1 import main as licence1_main
    from .controleur.licence2 import main as licence2_main
    from .controleur.licence3 import main as licence3_main
    from .controleur.cpp import main as cpp_main
    from .controleur.apropos import main as apropos_main
    from .controleur.contact import main as contact_main
   # from .controleur.licence2 import main
    # from .controleur.licence3 import main
    # from .controleur.cpp import main
    # from .controleur.apropos import main
    # from .controleur.contact import main
    # from .controleur.accueil import main


 #   from .controleur.licence1 import main

    app.register_blueprint(accueil_main)
    app.register_blueprint(licence1_main)
    app.register_blueprint(licence2_main)
    app.register_blueprint(licence3_main)
    app.register_blueprint(cpp_main)
    app.register_blueprint(apropos_main)
    app.register_blueprint(contact_main)

    
    return app