#Conditions (if-else) Example
print("โครงการห้องเรียน SMTE")

answer = input("ต้องการสมัครหรือไม่? (ใช่/ไม่): ").strip()

while answer not in ("ใช่", "ไม่"):
    print("กรุณาตอบ 'ใช่' หรือ 'ไม่'")
    answer = input("ต้องการสมัครหรือไม่? (ใช่/ไม่): ").strip()

if answer == "ไม่":
    print("ยกเลิกการสมัคร")
else:
    name = input("ชื่อ-นามสกุล : ")
    classroom = input("ห้อง : ")
    gpax = float(input("GPAX รวม : "))
    math = float(input("GPAX คณิตศาสตร์ : "))
    sci = float(input("GPAX วิทยาศาสตร์ : "))
    eng = float(input("GPAX ภาษาอังกฤษ : "))

    print("ชื่อ-นามสกุล : ", name)
    print("ห้อง : ", classroom)
    print("GPAX รวม : ", gpax)
    print("GPAX คณิตศาสตร์ : ", math)
    print("GPAX วิทยาศาสตร์ : ", sci)
    print("GPAX ภาษาอังกฤษ : ", eng)

    if gpax >= 3.25 and math >= 3.25 and sci >= 3.0 and eng >= 2.75:
        print("คุณผ่านเกณฑ์การคัดเลือกสมัครเข้าศึกษาต่อในโครงการห้องเรียน SMTE")
    else:
        print("คุณไม่ผ่านเกณฑ์การคัดเลือกสมัครเข้าศึกษาต่อ")
        print("ขอบคุณที่สนใจสมัครเข้าศึกษาต่อในโครงการห้องเรียน SMTE")
    