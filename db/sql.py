import pymysql as my
import datetime

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
def signin(uname,uid,upw,age,sex,weight,height,active):
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
                (`uname`,`uid`,`upw`,`age`,`sex`,`weight`,`height`,`active`)
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s)
                '''
                cursor.execute( sql,(uname,uid,upw,age,sex,weight,height,active) )
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
def selectFoodData(fid):
    connection = None
    rows       = None # 주식정보들을 담는 변수
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='ssmc_project',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 쿼리수행
        with connection.cursor() as cursor:            
            sql    = '''
                SELECT * 
                FROM food
                WHERE fid=%s
            '''%fid
            cursor.execute( sql )
            # 여러개 데이터를 다 가져올때
            rows    = cursor.fetchall()            
    except Exception as e:
        print('->', e)
        rows = None
    finally:
        if connection:
            connection.close()
    return rows

def searchFoods(foodname):
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
                    SELECT *
                    FROM food
                    WHERE foodname LIKE '%%%s%%'
                ''' % (foodname)
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
            #####################################################
    except Exception as e:
        print('->', e)
        row = None
    finally:
        if connection:
            print('Found Food : %s'%foodname)
            connection.close()
            print('DB Close : Find Food')
    return row

def Wordcloud():
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
                sql    = "select fid,COUNT(*) as cnt FROM meals group by fid ordey by cnt;"
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

# DB로 먹은 음식 데이터 
def insertFoodData(uid,fid,inbun):
    connection = None
    result     = 0 # 수정결과
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='ssmc_project',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 쿼리수행
        with connection.cursor() as cursor:            
            sql    = '''
                INSERT INTO meals
                (`uid`,`fid`,`inbun`)
                VALUES
                (%s,%s,%s)
            '''
            cursor.execute( sql,(uid,fid,inbun) )
            
        connection.commit()
        result = connection.affected_rows() # 1이 되야지 성공
        
    except Exception as e:
        print('->', e)
        result = 0
    finally:
        if connection:
            connection.close()
    return result

def deleteFoodData(uid,mid):
    connection = None
    result     = 0 # 수정결과
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='ssmc_project',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 쿼리수행
        with connection.cursor() as cursor:            
            sql    = '''
                DELETE
                FROM meals
                WHERE uid = %s and mid = %s
            '''
            cursor.execute( sql,(uid,mid) )
            
        connection.commit()
        result = connection.affected_rows() # 1이 되야지 성공
        
    except Exception as e:
        print('->', e)
        result = 0
    finally:
        if connection:
            connection.close()
    return result

# DB에서 모든 정보를 가지고오는 함수
# def searchFoodNutrient(foodname):

# 사용자가 입력해둔 개인정보를 가져오는 함수 -> 키 / 몸무게 등
# def searchUserInfo(uid):

# 사용자가 1일간 먹은 음식
def userOnePeriod(uid):
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
                ''' % (uid)
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

def searchRecentFood(uid,n):
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
                    select *
                    from meals
                    left outer join food 
                    on meals.fid = food.fid
                    where meals.uid=%s
                    order by date desc
                    LIMIT 0, %s;
                '''
                cursor.execute( sql,(uid,n) )
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
# 사용자가 1주일간 먹은 음식
# def userOneWeek(uid):

# 사용자가 1달간 먹은 음식
# def userOneMonth(uid):

def searchFoodNutrient(uid):
    connection = None
    row = None
    mydict = None 
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='ssmc_project',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정

        if connection:
            print('몰라')
            #####################################################
            with connection.cursor() as cursor:
                sql    = "select *from meals inner join food on meals.fid = food.fid where meals.uid='%s';"% uid
                cursor.execute( sql)

                row    = cursor.fetchall()
                print('++'*30)
                print( row )
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0,
                    'sugarSum':0,
                    'natriumSum':0,
                    'choleSum':0,
                    'satfatSum':0,
                    'transfatSum':0,
                    'carboSum1':0,
                    'proteinSum1':0,
                    'fatSum1':0
                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo']))
                    mydict['proteinSum']+=int(float(i['protein']))
                    mydict['fatSum']+=int(float(i['fat']))
                    mydict['sugarSum']+=int(float(i['sugar']))
                    mydict['natriumSum']+=int(float(i['natrium']))
                    mydict['choleSum']+=int(float(i['chole']))
                    mydict['satfatSum']+=int(float(i['satfat']))
                    mydict['transfatSum']+=int(float(i['transfat']))
                    mydict['carboSum1']+=int((float(i['carbo'])+float(i['sugar']))*4)
                    mydict['proteinSum1']+=int((float(i['protein'])*4))
                    mydict['fatSum1']+=int(float(i['fat'])*9+float(i['satfat'])*100+float(i['transfat'])*1000)
                #print('=*'*30)
                #print(mydict)
            #####################################################
    except Exception as e:
       print('->', e)
       row = None
    finally:
        if connection:
            connection.close()
            print('DB Close : Login Done')
    return mydict

# 사용자가 입력해둔 개인정보를 가져오는 함수 -> 키 / 몸무게 등
def searchUserInfo(uid):
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
            print('키가 필요해용')
            #####################################################
            with connection.cursor() as cursor:
                sql    = "select * from users where uid=%s;"
                cursor.execute( sql,uid)

                row    = cursor.fetchone()
                # print('++'*30)
                # print( row )

            #####################################################
    except Exception as e:
       print('->', e)
       row = None
    finally:
        if connection:
            connection.close()
            print('DB Close : Login Done')
    return row
#print(searchUserInfo('eun'))

# def dailyData(uid):
#     connection = None
#     row = None # 로그인 결과를 담는 변수
#     mydict1 = None
#     try:
#         connection = my.connect(host='localhost', # DB 주소
#                                 user='root',      # DB 접속 계정
#                                 password='12341234', # DB 접속 비번
#                                 db='ssmc_project',   # Database 이름
#                                 #port=3306,        # Port     
#                                 charset='utf8',
#                                 cursorclass=my.cursors.DictCursor) # Cursor Type

#         if connection:
#             print('DB OPEN : 일주일치 열려요')
#             #####################################################
#             with connection.cursor() as cursor:
#                 sql = '''
#                     select *
#                         from meals
#                             left outer join food 
#                                 on meals.fid = food.fid
#                     where meals.uid = '%s' and meals.date LIKE '%%%s%%'
#                 ''' % (uid,datetime.date.today())
#                 cursor.execute( sql )
#                 cursor.execute( sql )
#                 row    = cursor.fetchall()  # 하나의 row를 뽑을때
#                 mydict1={
#                     'carboSum':0,
#                     'proteinSum':0,
#                     'fatSum':0
#                     }
#                 for i in row:
#                     mydict1['carboSum']+=int((float(i['carbo'])+float(i['sugar']))*4)
#                     mydict1['proteinSum']+=int(float(i['protein'])*4)
#                     mydict1['fatSum']+=int(float(i['fat'])*9+float(i['satfat'])*100+float(i['transfat'])*1000)
#                 #print('=*'*30)
#                 #print(mydict1)
#             #####################################################
#     except Exception as e:
#         print('->', e)
#         row = None
#     finally:
#         if connection:
#             connection.close()
#             print('일주일치에용')
#     return mydict1

# def weekData(uid):
#     connection = None
#     row = None # 로그인 결과를 담는 변수
#     mydict1 = None
#     try:
#         connection = my.connect(host='localhost', # DB 주소
#                                 user='root',      # DB 접속 계정
#                                 password='12341234', # DB 접속 비번
#                                 db='ssmc_project',   # Database 이름
#                                 #port=3306,        # Port     
#                                 charset='utf8',
#                                 cursorclass=my.cursors.DictCursor) # Cursor Type

#         if connection:
#             print('DB OPEN : 일주일치 열려요')
#             #####################################################
#             with connection.cursor() as cursor:
#                 sql = '''
#                     select *
#                         from meals
#                             left outer join food 
#                                 on meals.fid = food.fid
#                     where meals.date >'%s' and meals.uid = '%s'
#                 ''' % (datetime.date.today() - datetime.timedelta(days=7),uid)
#                 cursor.execute( sql )
#                 cursor.execute( sql )
#                 row    = cursor.fetchall()  # 하나의 row를 뽑을때
#                 mydict1={
#                     'carboSum':0,
#                     'proteinSum':0,
#                     'fatSum':0
#                     }
#                 for i in row:
#                     mydict1['carboSum']+=int((float(i['carbo'])+float(i['sugar']))*4)
#                     mydict1['proteinSum']+=int(float(i['protein'])*4)
#                     mydict1['fatSum']+=int(float(i['fat'])*9+float(i['satfat'])*100+float(i['transfat'])*1000)
#                 #print('=*'*30)
#                 #print(mydict1)
#             #####################################################
#     except Exception as e:
#         print('->', e)
#         row = None
#     finally:
#         if connection:
#             connection.close()
#             print('일주일치에용')
#     return mydict1
# #month Data
# def MonthData(uid):
#     connection = None
#     row = None # 로그인 결과를 담는 변수
#     mydict2 = None
#     try:
#         connection = my.connect(host='localhost', # DB 주소
#                                 user='root',      # DB 접속 계정
#                                 password='12341234', # DB 접속 비번
#                                 db='ssmc_project',   # Database 이름
#                                 #port=3306,        # Port     
#                                 charset='utf8',
#                                 cursorclass=my.cursors.DictCursor) # Cursor Type

#         if connection:
#             print('DB OPEN : 일주일치 열려요')
#             #####################################################
#             with connection.cursor() as cursor:
#                 sql = '''
#                     select *
#                         from meals
#                             left outer join food 
#                                 on meals.fid = food.fid
#                     where meals.date >'%s' and meals.uid = '%s'
#                 ''' % (datetime.date.today() - datetime.timedelta(days=30),uid)
#                 cursor.execute( sql )
#                 cursor.execute( sql )
#                 row    = cursor.fetchall()  # 하나의 row를 뽑을때
#                 mydict2={
#                     'carboSum':0,
#                     'proteinSum':0,
#                     'fatSum':0
#                     }
#                 for i in row:
#                     mydict2['carboSum']+=int((float(i['carbo'])+float(i['sugar']))*4)
#                     mydict2['proteinSum']+=int(float(i['protein'])*4)
#                     mydict2['fatSum']+=int(float(i['fat'])*9+float(i['satfat'])*100+float(i['transfat'])*1000)
#                 #print('=*'*30)
#                 #print(mydict2)
#             #####################################################
#     except Exception as e:
#         print('->', e)
#         row = None
#     finally:
#         if connection:
#             connection.close()
#             print('일주일치에용')
#     return mydict2

def dailyData(uid):
    connection = None
    row = None # 로그인 결과를 담는 변수
    mydict1 = None
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            #####################################################
            with connection.cursor() as cursor:
                sql = '''
                    select *
                        from meals
                            left outer join food
                                on meals.fid = food.fid
                        where meals.uid = '%s' and meals.date > '%s'
                ''' % (uid, datetime.date.today() - datetime.timedelta(days = 1))
                cursor.execute( sql )
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0,
                    'sugarSum':0,
                    'natriumSum':0,
                    'choleSum':0,
                    'satfatSum':0,
                    'transfatSum':0
                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo'])*4)
                    mydict['proteinSum']+=int(float(i['protein'])*4)
                    mydict['fatSum']+=int(float(i['fat'])*9)
                    mydict['sugarSum']+=int(float(i['sugar'])*4)
                    mydict['natriumSum']+=int(float(i['natrium']))
                    mydict['choleSum']+=int(float(i['chole']))
                    mydict['satfatSum']+=int(float(i['satfat'])*100)
                    mydict['transfatSum']+=int(float(i['transfat'])*1000)
                    # mydict['carboSum']+=int((float(i['carbo'])+float(i['sugar']))*4)
                    # mydict['proteinSum']+=int(float(i['protein'])*4)
                    # mydict['fatSum']+=int(float(i['fat'])*9+float(i['satfat'])*100+float(i['transfat'])*1000)
                #print('=*'*30)
                #print(mydict1)
            #####################################################
    except Exception as e:
        print('->', e)
        row = None
    finally:
        if connection:
            connection.close()
    return mydict

def weeklyData(uid):
    connection = None
    row = None # 로그인 결과를 담는 변수
    mydict1 = None
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            #####################################################
            with connection.cursor() as cursor:
                sql = '''
                    select *
                        from meals
                            left outer join food
                                on meals.fid = food.fid
                        where meals.uid = '%s' and meals.date > '%s'
                ''' % (uid, datetime.date.today() - datetime.timedelta(days = 7))
                cursor.execute( sql )
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0
                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo'])*4)
                    mydict['proteinSum']+=int(float(i['protein'])*4)
                    mydict['fatSum']+=int(float(i['fat'])*9)
            #####################################################
    except Exception as e:
        print('- weeklyData-> ', e)
        row = None
    finally:
        if connection:
            connection.close()
    return mydict
#month Data
def monthlyData(uid):
    connection = None
    row = None # 로그인 결과를 담는 변수
    mydict2 = None
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            #####################################################
            with connection.cursor() as cursor:
                sql = '''
                    select *
                        from meals
                            left outer join food
                                on meals.fid = food.fid
                        where meals.uid = '%s' and meals.date > '%s'
                ''' % (uid, datetime.date.today() - datetime.timedelta(days = 30))
                print(uid, datetime.date.today() - datetime.timedelta(days = 30))
                cursor.execute( sql )
                cursor.execute( sql )
                row = cursor.fetchall()  # 하나의 row를 뽑을때
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0
                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo'])*4)
                    mydict['proteinSum']+=int(float(i['protein'])*4)
                    mydict['fatSum']+=int(float(i['fat'])*9)
            #####################################################
    except Exception as e:
        print('- monthlyData->', e)
        row = None
    finally:
        if connection:
            connection.close()
    return mydict

def dailyDataPersent(uid):
    connection = None
    row = None # 로그인 결과를 담는 변수
    mydict1 = None
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            #####################################################
            with connection.cursor() as cursor:
                sql = '''
                    select *
                        from meals
                            left outer join food
                                on meals.fid = food.fid
                        where meals.uid = '%s' and meals.date > '%s'
                ''' % (uid, datetime.date.today() - datetime.timedelta(days = 1))
                cursor.execute( sql )
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0,
                    'mySum':0

                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo'])*4)
                    mydict['proteinSum']+=int(float(i['protein'])*4)
                    mydict['fatSum']+=int(float(i['fat'])*9)
                mydict['mySum'] = mydict['carboSum']+mydict['proteinSum']+mydict['fatSum']
                print('mysum=>',mydict['mySum'])
                mydict['carboSum']=int((mydict['carboSum']/mydict['mySum'])*100)
                mydict['proteinSum']=int((mydict['proteinSum']/mydict['mySum'])*100)
                mydict['fatSum']=int((mydict['fatSum']/mydict['mySum'])*100)
            #####################################################
    except Exception as e:
        print('- weeklyData-> ', e)
        row = None
    finally:
        if connection:
            connection.close()
    return mydict




def weeklyDataPersent(uid):
    connection = None
    row = None # 로그인 결과를 담는 변수
    mydict1 = None
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            #####################################################
            with connection.cursor() as cursor:
                sql = '''
                    select *
                        from meals
                            left outer join food
                                on meals.fid = food.fid
                        where meals.uid = '%s' and meals.date > '%s'
                ''' % (uid, datetime.date.today() - datetime.timedelta(days = 7))
                cursor.execute( sql )
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0,
                    'mySum':0

                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo'])*4)
                    mydict['proteinSum']+=int(float(i['protein'])*4)
                    mydict['fatSum']+=int(float(i['fat'])*9)
                mydict['mySum'] = mydict['carboSum']+mydict['proteinSum']+mydict['fatSum']
                print('mysum=>',mydict['mySum'])
                mydict['carboSum']=int((mydict['carboSum']/mydict['mySum'])*100)
                mydict['proteinSum']=int((mydict['proteinSum']/mydict['mySum'])*100)
                mydict['fatSum']=int((mydict['fatSum']/mydict['mySum'])*100)
            #####################################################
    except Exception as e:
        print('- weeklyData-> ', e)
        row = None
    finally:
        if connection:
            connection.close()
    return mydict

def monthlyDataPersent(uid):
    connection = None
    row = None # 로그인 결과를 담는 변수
    mydict1 = None
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='ssmc_project',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            #####################################################
            with connection.cursor() as cursor:
                sql = '''
                    select *
                        from meals
                            left outer join food
                                on meals.fid = food.fid
                        where meals.uid = '%s' and meals.date > '%s'
                ''' % (uid, datetime.date.today() - datetime.timedelta(days = 30))
                cursor.execute( sql )
                cursor.execute( sql )
                row    = cursor.fetchall()  # 하나의 row를 뽑을때
                mydict={
                    'carboSum':0,
                    'proteinSum':0,
                    'fatSum':0,
                    'mySum':0

                    }
                for i in row:
                    mydict['carboSum']+=int(float(i['carbo'])*4)
                    mydict['proteinSum']+=int(float(i['protein'])*4)
                    mydict['fatSum']+=int(float(i['fat'])*9)
                mydict['mySum'] = mydict['carboSum']+mydict['proteinSum']+mydict['fatSum']
                print('mysum=>',mydict['mySum'])
                mydict['carboSum']=int((mydict['carboSum']/mydict['mySum'])*100)
                mydict['proteinSum']=int((mydict['proteinSum']/mydict['mySum'])*100)
                mydict['fatSum']=int((mydict['fatSum']/mydict['mySum'])*100)
            #####################################################
    except Exception as e:
        print('- weeklyData-> ', e)
        row = None
    finally:
        if connection:
            connection.close()
    return mydict

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
    # print(signin(info))
    