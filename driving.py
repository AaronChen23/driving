country = input("請輸入你的國家: ")
age = input("請輸入你的年齡: ")
age = int(age)

if country == "台灣":
	if age >= 18:
		print("你可以開車")
	else:
		print("你還不可以開車")	
elif country == "美國":
	if age >= 16:
		print("你可以開車")
	else:
		print("你還不可以開車")
else:
	print("請只能輸入 台灣/ 美國")
