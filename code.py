<<<<<<< HEAD
import re  # 정규 표현식 사용

# 로그인 함수
def login(regist_user):
    uid = input("아이디 입력: ")
    pwd = input("비밀번호 입력: ")
    
    if uid in regist_user and regist_user[uid] == pwd:
        print("로그인 성공!")
    else:
        print("아이디 또는 비밀번호가 올바르지 않습니다.")

# 회원가입 함수
def makeId(regist_user):
    while True:
        uid = input('회원 아이디 입력: ')
        if uid in regist_user:
            print("이미 등록된 ID입니다.")
            ex = input("메인 화면으로 이동하시겠습니까? (y/n): ")
            if ex.lower() == "y":
                return
            else:
                continue
        else:
            if not check_id(uid):
                continue
            break

    while True:
        pwd = input('비밀번호 입력: ')
        if not check_password(pwd):
            continue
        break

    regist_user[uid] = pwd  # 등록된 유저 저장
    print("회원가입이 완료되었습니다!")

# 아이디가 조건에 맞는지 확인하는 함수
def check_id(uid):
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, uid):
        print("아이디는 4~20자의 영문 대소문자, 숫자, 언더바(_)만 사용 가능합니다.")
        return False
    return True

# 비밀번호가 조건에 맞는지 확인하는 함수
def check_password(pwd):
    reg = r'^[A-Za-z0-9_]{8,20}$'
    if not re.search(reg, pwd):  # 변수명을 제대로 사용
        print("비밀번호는 8~20자의 영문 대소문자, 숫자, 언더바(_)만 사용 가능합니다.")
        return False
    return True

# 비밀번호 찾기 함수
def findidpassword(regist_user):
    uid = input("아이디 입력: ")
    if uid in regist_user:
        print(f"비밀번호 힌트: {regist_user[uid][:2]}******")  # 비밀번호 일부만 노출
    else:
        print("해당 아이디가 존재하지 않습니다.")

# 메인 함수
def main():
    regist_user = {}  # 등록된 유저 정보 저장 (딕셔너리 사용)

    while True:
        print("\n=========================================================")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 아이디 비밀번호 찾기")
        print("4. 프로그램 종료")
        print("=========================================================\n")
        try:
            choice = int(input("메뉴 선택 (1~4): "))
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if choice == 1:
            login(regist_user)
        elif choice == 2:
            makeId(regist_user)
        elif choice == 3:
            findidpassword(regist_user)
        elif choice == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

# 실행
main()
=======
#okay
>>>>>>> junseo
