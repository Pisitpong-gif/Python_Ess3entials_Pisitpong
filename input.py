#คำสั่ง input
name = input("Enter your name : ")
print("Welcome : " , name)

age = int(input("Enter your age : ")) #intiger จำนวนเต็ม
print("Your age is", age)

gpax = float(input("Enter your GPAX : "))
print("Your GPAX is" , gpax) #float ทศนิยม

#บวกเลขจำนวนเด็ม
num01 = int(input("Enter Number : "))
num02 = int(input("Enter Number : "))
print(f"Answer : {num01 + num02}")

#บวกเลขทศนิยม 2 ตำแหน่ง
num01 = float(input("Enter Number : "))
num02 = float(input("Enter Number : "))
print(f"Answer : {num01 + num02:.2f}")