#Dic = {"key": "value"} ;หลักการสร้าง Dictionary

student = {
    "name": "Python",
    "age": 20,
    "city": "Bangkok"
}

#แสดงผลแบบรวม 
print(student)

#แสดงผลแบบแยก key
print(student["name"])
print(student["age"])

print(student["city"][0]) #แสดงผลตัวอักษรตัวแรกของ key city

print("\n******************\n")

#method (เสริม Dictionary)
student.update({"country": "Thailand"}) #เพิ่ม key country เข้าไปใน Dictionary
print(student)
print(student.keys()) #แสดงผล key ทั้งหมดใน Dictionary
print(student.values()) #แสดงผล value ทั้งหมดใน Dictionary
print(student.items()) #แสดงผล key และ value ทั้งหมดใน Dictionary