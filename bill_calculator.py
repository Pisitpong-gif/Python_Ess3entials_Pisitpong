#ประยุกต์โปรแกรมคำนวณราคาสินค้าและภาษีมูลค่าเพิ่ม

product_name = str(input("ชื่อสินค้าของคุณ : "))
product_price = float(input("ราคาสินค้า : "))

vat= float(7/100 * product_price)
product_total = (product_price + vat)

print(f"ภาษี 7% : {vat:.2f} THB") 
print(f"ราคาสินค้าของคุณเมื่อรวมภาษี ทั้งหมด : {product_total:.2f} THB")