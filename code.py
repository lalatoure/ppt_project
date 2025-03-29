<<<<<<< HEAD
import re  # 정규 표현식 사용


# 로그인 함수
def login(regist_user):
    uid = input("아이디 입력: ")
    pwd = input("비밀번호 입력: ")

    if uid in regist_user and regist_user[uid] == pwd: #id가 regist_user안에(key값으로) 있고 그안에 (value값으로) 패스워드가 있다면
        print("로그인 성공!")
    else:
        print("아이디 또는 비밀번호가 올바르지 않습니다.")


# 회원가입 함수
def makeId(regist_user):
    while True:
        uid = input('회원 아이디 입력: ')
        if uid in regist_user: #id가 형식에 맞는지 확인하는 함수
            print("이미 등록된 ID입니다.")
            while True:
               ex = input("메인 화면으로 이동하시겠습니까? (y/n): ")
               if ex.lower() == "y":
                 return
               elif ex.lower() == "n":
                 break
               else:
                print("대소문자 구별없이 (Y/N)입력하시오")
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
    print(regist_user)  # 잘 저장되었는지 확인용 코드
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
  while True:
    uid = input("아이디 입력: ")  #찾으려는 비밀번호의 아이디 입력 한다
    if uid in regist_user:      #저장된 아이디가 맞다면
      print("아이디 인증됨")      #아이디 인증됨을 출력
      while True:
<<<<<<< HEAD
       x = int(input("비밀번호 변경1 비밀번호 두자리확인 2  돌아가기는 3 을 입력해주세요"))  #메뉴선택
=======
       x = int(input("1 : 비밀번호 변경  2 : 비밀번호 두자리확인  3:  돌아가기를 입력해주세요  입력 : "))  #메뉴선택
>>>>>>> d2a9ff7 (change)
       if(x==1):
            oldpw = input("기존 비밀번호를 입력하세요 : ") #oldpw에 기존 비밀번호 입력
            if ( oldpw == regist_user[uid]):          #딕셔너리안 아이디(key) 에 매칭되는 비밀번호(Value) 가 기존비밀번호와 같다면
                while True:                           #새 비밀번호를 입력받게 한다.
                    newpwd = input('새 비밀번호 입력: ')
                    if not check_password(newpwd):    #새비밀번호가 형식에 맞는지 확인하는 코드
                        continue
                    break
                print("변경전 아이디 비번")
                print(regist_user)  # 확인용 코드
                regist_user[uid] = newpwd             #딕셔너리안 아이디(key) 에 새 비밀번호(Value) newpd로 대체
                print("변경후 아이디 비번")
                print(regist_user) #확인용 코드 문제없으니 삭제해도 됨 편의상 남겨도 됨
                return
            else:
              print("기존 비밀번호가 일치하지 않습니다.") #만약 아이디랑 비밀번호가 일치하지 않느다면
              continue                              #다시 (비밀번호 변경1 비밀번호 두자리확인 2  돌아가기는 3 을 입력해주세요) 를 출력
       elif(x==2):
             print(f"비밀번호 힌트: {regist_user[uid][:2]}******")  #2번메뉴 선택시 비밀번호 일부만 노출실행
       elif(x==3):
            return                                #3번메뉴 선택시 메인화면 돌아가기
       else:
            print("없는 숫자입니다 다시 입력하세요")   # 1,2,3 이외의 값 눌렀을때 처리코드
            continue
    else:
      print("해당 아이디가 존재하지 않습니다.")       # 아이디가 기존에 저장되어있지 않은 없는 아이디라면?
      while True:
          yn = input("다시입력은 Y 메인 복귀는 N (Y/N)")
          if (yn == "Y" or yn == "y"): #대소문자 구분없이 입력
            break
          elif(yn == "N" or yn == "n"):
            return
          else:
           print("잘못입력 대소문자 (Y/N) 만 입력가능합니다.") #만약 yn예외의 값을 입력받으면
           continue                                     # 다시 입력하라는  창 띄우기



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
#okay
>>>>>>> junseo
