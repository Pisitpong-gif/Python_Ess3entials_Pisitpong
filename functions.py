#Function
def call(name): #สร้างฟังก์ชันชื่อ call และมีพารามิเตอร์ name
    print(f"Hello, {name}!")

call("Python") #เรียกใช้ฟังก์ชัน call พร้อมส่งค่า "Python" เป็นอาร์กิวเมนต์

def calculate(num1, num2): #สร้างฟังก์ชันชื่อ calculate และมีพารามิเตอร์ num1 และ num2
    return num1 + num2 #ส่งค่าผลรวมของ num1 และ num2 กลับไป

result = calculate(10, 5) #เรียกใช้ฟังก์ชัน calculate พร้อมส่งค่า 10 และ 5 เป็นอาร์กิวเมนต์
print(f"Result: {result}") #แสดงผลลัพธ์

print("\n******************\n")

#รูปแบบไม่มี return
def calculate(num1, num2):
    total = num1 + num2
    print(f"Total: {total}") 

result = calculate(5, 2)
print(f"Result: {result}") #ผลลัพธ์จะเป็น None เพราะฟังก์ชันไม่มี return (ส่งค่ากลับไป)
