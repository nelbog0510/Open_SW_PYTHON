from PIL import Image

print("===이미지 처리 프로그램===")
print("1. 이미지 크기 변경")
print("2. 이미지 자르기")
print("3. 이미지 회전")
print("4. 흑백 이미지로 변환")

menu = input("원하는 기능을 선택하세요. : ")

img = Image.open("cat.jpg")

if menu == "1":
    img = img.size((300, 300))
elif menu == "2":
    img = img.crop(100,100,500,500)
elif menu == "3":
    img = img.rotate(90, expand = True)
elif menu == "4":
    img = img.convert("L")
    
    
img.show()
img.save("result2.png")