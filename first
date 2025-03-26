import re  #search함수도입용
#로그인 함수
def login(x):
    print("기다려")

#회원가입함수
def makeId(regist_user):
 regist_id = []
 while True:
   uid = str(input('회원 아이디 입력 : '))
   if uid in regist_user:
     print("이미 등록된 id입니다.")
     ex = input("메인 화면으로 이동하시겠습니까? (y/n) :")
     if ex == "y" or ex=="Y":
      return False
     else:
       continue
   else:
    res_id = check_id(uid)
    if not res_id:
      continue
    else:
      regist_id.append(uid)
    break
   while True:
    pwd = str(input('비밀번호 입력: '))
    res_pwd = check_password(pwd)
    if not res_pwd:
      continue
    else:
      regist_id.append(pwd)
      break
    return regist_id


#아이디가 조건에 맞는지 확인하는 함수
def check_id(id):
  result = True
  reg = r'^[A-Za-z0-9_]{4,20}$'
  if not re.search(reg, id):
    print("아이디 생성 기준과 맞지않습니다.")
    result = False
  return result

#비밀번호가 조건에 맞는지 확인 하는 함수
def check_password(pwd):
  result = True
  reg = r'^[A-Za-z0-9_]{8,20}$'
  if not re.search(reg, id):
    print("비밀번호는 대소문자 가능 숫자가능 . 8~ 20자리 다시입력")
    result = False
  return result

#비밀번호 찾기.
def findidpassword(x):
 print("아직")


#메인함수
def main():

 while True:
  print("=========================================================\n")
  print("1번 로그인\n")
  print("2번 회원가입\n")
  print("3번 아이디 비밀번호 찾기\n")
  print("4번 프로그램 종료\n")
  print("=========================================================\n")
  x = int(input("메뉴 선택 1~4"))
  if(x==1):
   login(x)
  elif(x==2):
    makeId(x)
  elif(x==3):
   findidpassword(x)
  elif(x == 4):
    print("프로그램을 종료합니다.")
    return
  else:
   print("선택하신 번호는 메뉴에 없습니다. 번호 재선택")
