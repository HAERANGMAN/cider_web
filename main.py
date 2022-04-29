from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Flask
from flask_migrate import Migrate
from app.config.config import APP_CONFIG
from app.db.database import db

def create_app():
    """App factory"""
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG["development"])
    db.init_app(app)
    Migrate(app,db)

    # Register blueprint apps
    app.register_blueprint(homeViews)

    return app
    
app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/check", methods=['POST'])
def login():        
    if request.form["_username"] == "ubion" and request.form["_password"] == "tkdlek7":
        flash("환영합니다!")
        # return  redirect(url_for("main.html"))
        return render_template("main.html")
    else:
        flash("다시 입력해주세요!")            
        return redirect(url_for("index"))

@app.route('/main', methods=["GET"])
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug = True, port=8080)