password = 'a12345'#使用者的密碼
time = 3 #剩餘機會
while time > 0 :
	time = time - 1
	userEnter = input('請輸入密碼: ')#使用者所輸入的
	if userEnter == password :
		print('登入成功')
		break
	else :
		print('密碼錯誤')
		if time == 0 :
			print('帳號已被封鎖')
		else :
			print('還有',time,'次機會')