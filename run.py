from flask import Flask, render_template ,url_for, request, redirect, session, jsonify
from db.sql import *
import os

app=Flask(__name__)

app.secret_key= 'qweasdzxc'


@app.route('/')
def main():
    # 세션이 없으면 로그인으로
    # if not 'user_id' in session:
    #     return redirect( url_for( 'login' ) )
    return render_template('main.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if  request.method == 'GET':
        # GET
        return render_template('header.html')
    else:  
         uid = request.form['uid']
         print(uid)
         upw = request.form['upw']
         row = loginSql(uid,upw)
         if row:
             # 세션생성
             session['user_id']= uid
             session['user_nm']= row['name']
             # 홈페이지로 이동    
             return redirect(url_for('main') )
         else:
            return render_template('error.html', msg='아이디 비번확인 요청')


if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)