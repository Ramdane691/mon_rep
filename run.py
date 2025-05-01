from app import create_app

app = create_app()  # Objet global accessible par gunicorn

if __name__ == '__main__':
    app.run(debug=True)
