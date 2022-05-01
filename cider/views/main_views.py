from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for



bp = Blueprint('main', __name__, url_prefix='/') #별칭, 인수(__name__ = main_views.py), url



@bp.route('/')
def index():    
    return render_template('index.html')



@bp.route('/main')
# @app.route('/main', methods=["GET"])
def index():
    render_template('main.html')

def algo1():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from pandas_datareader import data  
    from datetime import datetime
    import pandas as pd

    # 데이터를 가져올 날짜 설정
    start_date = datetime(2013,1,3)
    end_date = datetime(2021,1,22)

    # 야후에서 삼성전자 데이터 가져오기
    samsung = data.get_data_yahoo("005930.ks", start_date, end_date)

    samsung = samsung.reset_index()
    samsung['Date'] = samsung['Date'].apply(lambda x : datetime.strftime(x, '%Y-%m-%d')) # Datetime to str

    stock_name = '삼성전자'

    fig = go.Figure(data=[go.Candlestick(x=samsung['Date'],
                                        open=samsung['Open'],
                                        high=samsung['High'],
                                        low=samsung['Low'],
                                        close=samsung['Close'])])
    # x축 type을 카테고리 형으로 설정, 순서를 오름차순으로 날짜순서가 되도록 설정
    fig.layout = dict(title=stock_name, 
                            xaxis = dict(type="category", 
                                        categoryorder='category ascending'))
    fig.update_xaxes(nticks=5)

    return fig.show() 
    



#app -> bp로 변경해서 사용
@bp.route("/check", methods=['POST'])
def login():        
    if request.form["_username"] == "ubion" and request.form["_password"] == "tkdlek7":
        flash("환영합니다!")
        # return  redirect(url_for("main.html"))
        return redirect(url_for("main.index"))
        return render_template("main.html")
    else:
        flash("다시 입력해주세요!")            
        return redirect(url_for("index"))


#붕어빵 기계 어떻게 바꿀것인지?
# @bp.route("/algo1", methods=['POST'])
# def algo1():
#     import plotly.graph_objects as go
#     from plotly.subplots import make_subplotsW
#     from pandas_datareader import data  
#     from datetime import datetime
#     import pandas as pd

#     # 데이터를 가져올 날짜 설정
#     start_date = datetime(2013,1,3)
#     end_date = datetime(2021,1,22)

#     # 야후에서 삼성전자 데이터 가져오기
#     samsung = data.get_data_yahoo("005930.ks", start_date, end_date)

#     from plotly.subplots import make_subplots
#     import plotly.graph_objects as go

#     samsung = samsung.reset_index()
#     samsung['Date'] = samsung['Date'].apply(lambda x : datetime.strftime(x, '%Y-%m-%d')) # Datetime to str

#     stock_name = '삼성전자'

#     fig = go.Figure(data=[go.Candlestick(x=samsung['Date'],
#                                         open=samsung['Open'],
#                                         high=samsung['High'],
#                                         low=samsung['Low'],
#                                         close=samsung['Close'])])
#     # x축 type을 카테고리 형으로 설정, 순서를 오름차순으로 날짜순서가 되도록 설정
#     fig.layout = dict(title=stock_name, 
#                             xaxis = dict(type="category", 
#                                         categoryorder='category ascending'))
#     fig.update_xaxes(nticks=5)
#     fig.show()
###################(def_algo)###################3############################