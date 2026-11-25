#แสดงตัวเลขระหว่างช่วง 1 ถึง 10
for i in range(1, 11):
    print(i)

#พิมซ้ำ 3 ครั้ง
for i in range(3):
    print("I love Python")

#หยุดการทำงานก่อนถึงครั้งที่ 5 (พิมพ์ถึงครั้งที่4และหยุด)
for i in range(1, 9):
    if i == 5:
        break
    print("Hello Python", i)

#ข้ามการทำงานครั้งที่ 2 (ไม่พิมพ์เลข 2)
for i in range(1, 6):
    if i == 2:
        continue
    print(i)

for i in range(3): #การกรอกรหัสผ่านให้ถูกต้อง จำกัดการกรอกผิดได้ 3 ครั้ง
    password = input("Enter Password : ")
    if password == "1234":
        print("Login Success")
        break
    else:
        print("Incorrect Password, Please try again")