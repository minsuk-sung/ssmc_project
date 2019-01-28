import pymysql as my

# 아이디 및 비밀번호 입력받으면 로그인하는 함수 
def loginSql( uid, upw ):
    connection = None
    row = None # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='ssmc_project',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정

        if connection:
            print('DB Open : Login')
            #####################################################
            with connection.cursor() as cursor:
                sql    = '''
                    SELECT *
                    FROM users
                    WHERE uid=%s and upw=%s;
                '''
                cursor.execute( sql, (uid, upw) )

                row    = cursor.fetchone()
                print( row )
                print( "%s(%s)님이 로그인하였습니다."  % (row['uid'],row['uname'])  )
            #####################################################
    except Exception as e:
        print('->', e)
        row = None
    finally:
        if connection:
            connection.close()
            print('DB Close : Login Done')
    return row

# 회원가입하는 함수
def signin(uname,uid,upw,age,sex,weight,height):
    connection = None
    result = 0 # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            print('user DB OPEN')
            #####################################################
            with connection.cursor() as cursor:
                sql    ='''
                INSERT INTO users
                (`uname`,`uid`,`upw`,`age`,`sex`,`weight`,`height`)
                VALUES
                (%s,%s,%s,%s,%s,%s,%s)
                '''
                cursor.execute( sql,(uname,uid,upw,age,sex,weight,height) )
                connection.commit()
                result = connection.affected_rows() # 1이 되야지 성공
            #####################################################
    except Exception as e:
        print('->', e)
        result = 0
    finally:
        if connection:
            connection.close()
            print('user DB CLOSE')
    return result

# main 검색창에서 요청한 음식을 DB로부터 가져오는 함수 -> ajax에서 쓸 용도
def searchFoodAjax(foodname):
    connection = None
    row = None # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            print('DB OPEN : Find Food')
            #####################################################
            with connection.cursor() as cursor:
                sql    = '''
                    SELECT foodname,kcal
                    FROM food
                    WHERE foodname LIKE '%%%s%%'
                    LIMIT 0, 10;
                ''' % (foodname)
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
            #####################################################
    except Exception as e:
        print('->', e)
        row = None
    finally:
        if connection:
            connection.close()
            print('DB Close : Find Food')
    return row

# DB에서 모든 정보를 가지고오는 함수
# def searchFoodNutrient(foodname):

# 사용자가 입력해둔 개인정보를 가져오는 함수 -> 키 / 몸무게 등
# def searchUserInfo(uid):

# 사용자가 1일간 먹은 음식
# def userOnePeriod(uid,):

# 사용자가 1주일간 먹은 음식
# def userOneWeek(uid):

# 사용자가 1달간 먹은 음식
# def userOneMonth(uid):

if __name__ == '__main__':
    # ajax에서 음식 리스트 찾는 연습
    # print('-'*50)
    # for flist in searchFoodAjax(input('음식을 검색하세요 : ')):
    #     print( flist['foodname'],'\t',flist['kcal'],'kcal')
    # print('-'*50)

    # loginSql('m','1')

    info = {
        'uname':'multi',
        'uid':'m',
        'upw':'1',
        'age':20,
        'sex':'m',
        'height':170,
        'weight':70
    }
    print(signin(info))