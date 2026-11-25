i = 1

#พิมพ์ 5 ครั้ง ค่า i จะเพิ่มขึ้นครั้งละ 1 จนถึง 5 
while i <= 5:
    print("Hello Python", i)
    i += 1 #ป้องกัน infinite loop

print("End of Program")

while True: #ใช้กับ input เพื่อให้ผู้ใช้ใส่รหัสผ่านถูกต้องก่อนเข้าโปรแกรม
    password = input("Enter Password : ")
    if password == "1234":
        print("Login Success")
        break
    else:
        print("Incorrect Password, Please try again")