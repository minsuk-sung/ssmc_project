import pymysql as my

# 아이디 및 비밀번호 입력받으면 로그인하는 함수 
def loginSql( uid, upw ):
    connection = None
    row = None # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='python_db',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정

        if connection:
            print('DB Open : Login')
            #####################################################
            with connection.cursor() as cursor:
                sql    = "select * from users where uid=%s and upw=%s;"
                cursor.execute( sql, (uid, upw) )

                row    = cursor.fetchone()
                print( row )
                print( "%s님"  % row['name']  )
            #####################################################
    except Exception as e:
        print('->', e)
        row = None
    finally:
        if connection:
            connection.close()
            print('DB Close : Login Done')
    return row

# main 검색창에서 요청한 음식을 DB로부터 가져오는 함수
def searchFood(foodname):
    connection = None
    row = None # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='python_db',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            print('DB OPEN : Find Food')
            #####################################################
            with connection.cursor() as cursor:
                sql    = "select foodname,kcal from food where foodname=%s;"
                cursor.execute( sql, (foodname,) )
                row    = cursor.fetchone()  # 하나의 row를 뽑을때
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
    searchFood('음식')