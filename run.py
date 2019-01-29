from flask import Flask, render_template ,url_for, request, redirect, session, jsonify
from db.sql import *
import os

app=Flask(__name__)

app.secret_key= 'qweasdzxc'


@app.route('/')
def main():
    return render_template('main.html')
# 로그인
@app.route('/login',methods=['POST'])
def login():
        uid = request.form['uid']
        print(uid)
        upw = request.form['upw']
        row = loginSql(uid,upw)
        if row:
            # 세션생성
            session['user_id']= uid
            session['user_nm']= row['uname']
            # 홈페이지로 이동    
            return redirect(url_for('main') )
        else:
            return render_template('error.html', msg='아이디 비번확인 요청')

@app.route('/logout')
def logout():
    # 세션 제거
    if 'user_id' in session:
        session.pop('user_id',None)
    if 'user_nm' in session:   
        session.pop('user_nm',None)
    # 홈페이지 이동
    return redirect(url_for('main'))

# 회원가입 홈페이지 띄어주는 함수
@app.route('/join')
def join():
     return render_template('signin.html')

# 회원가입 함수
@app.route('/join2',methods=['POST'])
def join2():  
    uid = request.form['uid']
    upw = request.form['upw']
    uname = request.form['uname']
    sex = request.form['sex']
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    active = request.form['active']
    
    row = signin(uname,uid,upw,age,sex,weight,height,active)
    return render_template('signin2.html')

# 음식데이터를 메인에 띄어주기위한 함수
@app.route('/foodlist',methods=['POST'])
def foodinfo():
    food_from_db = searchFoods(request.form['keyword'])
    if food_from_db:
        return render_template('main.html',foods=food_from_db,count=len(food_from_db))
    else:
        return render_template('sub/add.html',msg="해당 음식이 없습니다.")
@app.route('/mypage')
def mypage():
    uid =session['user_id']
    add_result_db = searchRecentFood(uid,10)
    return render_template('mypage.html',foods=add_result_db,count=len(add_result_db))

@app.route('/add',methods=['POST'])
def add():
    fid = request.form['fid']
    inbun= request.form['inbun']
    rows = selectFoodData(fid)

    uid = session['user_id']
    if 'user_id'in session:
        insertFoodData(uid,fid,inbun)
        return render_template("sub/add.html",msg="추가되었습니다")
    else:  
        return render_template("sub/add.html",msg="로그인해주세요" )

@app.route('/deletefood',methods=['POST'])
def deletefood():
    fid = request.form['fid']
    uid = session['user_id']
    deleteFoodData(uid,fid)
    return render_template("sub/delete.html",msg="삭제되었습니다",url='http://localhost:5000/mypage')
    

if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)