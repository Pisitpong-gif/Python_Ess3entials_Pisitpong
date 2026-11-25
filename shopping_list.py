#โปรแกรมลิสต์รายการซื้อของ

shopping_list = []
while True:
    item = input("Enter item : ")
    if item.lower() == "done":
        break
shopping_list.append(item)

print("==================")

print("Your shopping list:")
for item in shopping_list:
    print("- " + item)