from flask import Flask, url_for
import config.secrets as secret

from controller.auth_controller import auth

app = Flask(__name__)
app.secret_key = secret.SECRET_KEY


@app.route('/')
def home():
    return "It is good to come back home :)"


app.register_blueprint(auth, url_prefix='/auth')


if __name__ == "__main__":
    app.run(debug=True)

