from flask import Flask, render_template, request, flash, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pymysql

import config

#######################################################################
# sql 서버는 두고 일단 시키는대로 SQLAlchemy사용
# db = pymysql.connect(
#                 host="ls-a20f4420f7aa9967e25c1e0aecf4d8b641af5f13.cgtgapkuvqbt.ap-northeast-2.rds.amazonaws.com",
#                 db="ML",
#                 user = "dbmasteruser",
#                 password= "r,3Ipn|O7mL2vL4S)9Q~;7QVdHMV6R9j",
#                 port = 3306)

# cursor = db.cursor(pymysql.cursors.DictCursor)       
#######################################################################

db = SQLAlchemy()
migrate = Migrate()
    

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) #config.py읽어오기
    app.secret_key = 'super secret key' #다중실행시 오류발생 커버용

    # 0RM
    db.init_app(app)
    migrate.init_app(app,db)

    #블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app


#########################################
# main_views.py로 이동
# @app.route('/')
# def index():
#     return render_template('index.html')
##############################################



#########################################
# main_views.py로 이동
# @app.route('/main', methods=["GET"])
# def main():
#     return render_template('main.html')
##############################################

#####################################################
# main_views.py로 이동
# @app.route("/check", methods=['POST'])
# def login():        
#     if request.form["_username"] == "ubion" and request.form["_password"] == "tkdlek7":
#         flash("환영합니다!")
#         # return  redirect(url_for("main.html"))
#         return render_template("main.html")
#     else:
#         flash("다시 입력해주세요!")            
#         return redirect(url_for("index"))
#####################################################


# if __name__ == '__main__':
#     app.run(debug = True, port=8080)