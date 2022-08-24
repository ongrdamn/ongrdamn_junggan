import requests #웹스크랩핑시 사용 모듈
res = requests.get("https://www.naver.com/") #get('링크주소') 링크주소를 열때
res.raise_for_status() #문제가 있으면 상태코드 출력, 문제없으면 웹 스크랩핑 진행 if문 없이 가능해서 자주사용


# print('응답코드 : ', res.status_code) # status_code(상태코드)웹서버에서 HTTP 요청이
                                    #성공했는지 실패했는지를 서버에서 알려주는 코드로, 200번대는 성공(100~500번대 존재)


#if res.status_code == requests.codes.ok:
#    print('정상입니다')
#else:
#    print("문제가 생겼습니다 [에러코드 ",res.status_code,"]")

print(len(res.text))

