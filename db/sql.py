import pymysql as my

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
            print('디비 오픈')
            #####################################################
            with connection.cursor() as cursor:
                # 파라미터 자리를 '' 포함해서 %s로 대체
                # 'm' => %s 
                # 방법 1
                sql    = "select * from users where uid=%s and upw=%s;"
                cursor.execute( sql, (uid, upw) )

                # 방법 2 : 적절히 섞어서 사용한다(적합한 타이밍이 나온다)
                # select * from users where uid=m and upw=1;
                #sql    = "select * from users where uid='%s' and upw='%s';" % ('m', '1')
                #print( sql )
                #cursor.execute( sql )

                row    = cursor.fetchone()  # 하나의 row를 뽑을때
                # {'id': 1, 'name': '멀티', 'uid': 'm', 'upw': '1', 'regdate': datetime.datetime(2019, 1, 7, 14, 14, 23)}
                print( row )
                print( "%s님 방갑습니다."  % row['name']  )
                #cursor.close()
            #####################################################
    except Exception as e:
        print('->', e)
        row = None
    finally:
        if connection:
            connection.close()
            print('디비 닫기')
    return row
