products = [
    ("حاسوب محمول", 2500),
    ("هاتف ذكي", 1500),
    ("سماعات بلوتوث", 200),
    ("لوحة مفاتيح", 120),
    ("فأرة لاسلكية", 80)
]


TAX = 0.15

print("قائمة المنتجات:\n")
for i, item in enumerate(products, 1):
    print(f"{i} - {item[0]} - السعر: {item[1]} ريال")


choice = input("\nأدخل رقم المنتج الذي تريده: ")

if not choice.isdigit():
    print("❌ الرجاء إدخال رقم صحيح!")
else:
    choice = int(choice)

    if 1 <= choice <= len(products):
        name, price = products[choice - 1]
        total = price + (price * TAX)

        print("\n------------------------------")
        print(f"اسم المنتج: {name}")
        print(f"السعر بدون ضريبة: {price} ريال")
        print(f"السعر شامل الضريبة (15%): {total:.2f} ريال")
        print("------------------------------")
    else:
        print("❌ رقم المنتج غير موجود في القائمة!")
