# https://wikidocs.net/153821
# https://appia.tistory.com/624

import win32com.client

# 1) Outlook Application에 대한 객체 생성하기
outlook=win32com.client.Dispatch("Outlook.Application")

# 2) 메일을 보내기 위한 객체 생성
send_mail = outlook.CreateItem(0)

# 3) 메일 보내기에 필요한 정보 입력
send_mail.To = "khleegood@hyundai.com" #메일 수신인
# send.mail.CC = "참조@gmail.com" #메일 참조
# send_mail.BCC = "khleegood@hyundai.com" #메일 숨은 참조
send_mail.Subject = "라이드 하이트/휠얼라인먼트 데이터 오류 발생 " #메일 제목
send_mail.HTMLBody = "DB로 정상적으로 저장되지 않았습니다" #내용

# send_mail.Display(True)  # 메일 팝업 창 띄우기

# 4) 메일 보내기
send_mail.Send() #메일 보내기