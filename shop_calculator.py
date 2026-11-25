#ประยุกต์โปรแกรมคำนวณราคาสินค้าและส่วนลด

product_name = str(input("ชื่อสินค้าของคุณ : "))
product_price = float(input("ราคาสินค้า/ชิ้น : "))
product_quantity = int(input("จำนวนสินค้า : "))
product_discount = float(input("ส่วนลด % : "))

#คำนวณราคาสินค้าและส่วนลด (ราคาสินค้า * จำนวนสินค้า) - (ราคาสินค้า * จำนวนสินค้า * ส่วนลด / 100)
product_calculate = (product_price * product_quantity) - (product_price * product_quantity * product_discount / 100)
product_total = product_calculate

#แสดงใบเสร็จอย่างง่าย
print("=====RECEIPT=====")
print(f"ชื่อสินค้า : {product_name}")
print(f"ราคา/ชิ้น : {product_price:.2f} THB")
print(f"จำนวน : {product_quantity}")
print(f"ส่วนลด : {product_discount}%")
print(f"รวมทั้งหมด : {product_total:.2f} THB")
print("=================")