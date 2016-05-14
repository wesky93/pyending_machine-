import sqlite3

db = "test.db"



'''
아이템 추가용 함수
-- 현재 insert에서의 문제로 작동 불가
--  sql명령어가 ""로 쌓여 있기에 변수가 대입되지 않은것으로 추론됨
--  실제로 책에선 플레이스 홀더를 통하여 대입을 하지 직접 변수를 넣지 않음
--  위 문제와 더불어 명령어가 ""로 감싸있기에 format 문자열 변수를 대입하더라도 ""로 감싸주어 문자열이라는 표시가 도어야 한다.
'''
def 아이템추가(번호, 음료명, 재고):
    print("함수 시작",db)
    with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute('INSERT INTO item VALUES ({0},\"{1}\",{2})'.format(번호,음료명,재고))
        print("자료 추가")
        DB.commit()
        print("db 커밋")
        print("{1}을 {0}번에 추가하였습니다.".format(번호,음료명))

#조회 문구는 문제 없이 실행됨
def 아이템조회():
    print("함수 시작",db)
    with sqlite3.connect(db) as DB:
        print("DB연결")
        질의 = DB.cursor()
        print("커서 연결")
        질의.execute("SELECT * FROM item")
        print("조회 완료")
        for row in 질의:
            print(row)

아이템추가(4,"고코팡",13)

#아이템 추가 함수 오류로 인한 확인용 구문
#DB의 연결 문제인지 insert 구문 오류인지 판단하기 위함
아이템조회()
