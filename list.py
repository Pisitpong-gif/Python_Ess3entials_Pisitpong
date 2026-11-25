#list
fruits = ["Apple", "Banana", "Orange"]
print(fruits)

print(fruits[0]) #แสดงผลลัพธ์ Apple
print(fruits[1]) #แสดงผลลัพธ์ Banana

fruits[0] = "Grape" #เปลี่ยนค่า Apple เป็น Grape
print(fruits)

fruits.append("Mango")# เพิ่มผลไม้ Mango เข้าไปใน list
print(fruits)

print("\n******************\n")

for i in fruits: #แสดงผลลัพธ์ผลไม้ทั้งหมดใน list ทีละบรรทัด
    print(i)

print("\n******************\n")

print(len(fruits)) #แสดงผลลัพธ์จำนวนผลไม้ทั้งหมดใน list