import webbrowser

while(1) :
    print("------------------------------------------------")
    url1 = 'https://www.dimigo.hs.kr/'
    url2 = 'https://dimigo.life/#/login'
    url3 = 'https://dimigo.in/#/auth/login'
    url4 = 'https://student.dimigo.hs.kr/total-achieve/introduce'
    print("사이트 접속 목록 : \n\t\t\t1.디미고 홈페이지 \n\t\t\t2.디미고 라이프\n\t\t\t3.디미고 인\t\t\n\t\t\t4.소양인증제\n입력 :" ,end = '')
    a = input()
    if a == '1' :
        print("디미고 홈페이지 사이트를 엽니다.")
        webbrowser.open(url1)
    elif a == '2' :
        print("디미고 라이프 사이트를 엽니다.")
        webbrowser.open(url2)
    elif a == '3' :
        print("디미고 인 사이트를 엽니다.")
        webbrowser.open(url3)
    elif a == '4' :
        print("소양인증제 사이트를 엽니다.")
        webbrowser.open(url4)
    print("------------------------------------------------")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")