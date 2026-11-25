#โปรแกรมคำนวณเกรดเฉลี่ย

print("โปรแกรมคำนวณเกรดเฉลี่ยวิชาฟิสิกส์ของนักเรียนชั้น ม.6")

name = input("Enter student name : ")
score = int(input("Enter student score : "))

if score < 0 or score > 100:
    print("Student score must be between 0 and 100")
elif score < 50:
    print("Student Grade is F")
elif score < 60:
    print("Student Grade is D")
elif score < 70:
    print("Student Grade is C")
elif score < 80:
    print("Student Grade is B")
else:
    print("Student Grade is A")