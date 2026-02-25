"""
أداة سهلة لتحديث أسعار الأيفونات والاكسسوارات
Easy Price Updater for Ahmed's iPhone Store Bot
"""

def print_menu():
    print("""
╔══════════════════════════════════════════╗
║   🛠️  أداة تحديث الأسعار - أحمد الصعيدي   ║
╚══════════════════════════════════════════╝

اختر ما تريد تحديثه:

1. تحديث أسعار الأيفونات
2. تحديث أسعار الاكسسوارات
3. إضافة أيفون جديد
4. إضافة اكسسوار جديد
5. حذف منتج
6. عرض جميع الأسعار
0. خروج

""")

# بيانات الأيفونات الحالية
current_iphones = {
    '1': {'name': 'iPhone 16 Pro Max', 'prices': {'256GB': '50,000', '512GB': '56,000', '1TB': '62,000'}},
    '2': {'name': 'iPhone 16 Pro', 'prices': {'128GB': '42,000', '256GB': '46,000', '512GB': '52,000', '1TB': '58,000'}},
    '3': {'name': 'iPhone 16 Plus', 'prices': {'128GB': '36,000', '256GB': '40,000', '512GB': '46,000'}},
    '4': {'name': 'iPhone 16', 'prices': {'128GB': '32,000', '256GB': '36,000', '512GB': '42,000'}},
    '5': {'name': 'iPhone 15 Pro Max', 'prices': {'256GB': '42,000', '512GB': '47,000', '1TB': '53,000'}},
    '6': {'name': 'iPhone 15', 'prices': {'128GB': '28,000', '256GB': '32,000', '512GB': '37,000'}},
    '7': {'name': 'iPhone 14', 'prices': {'128GB': '24,000', '256GB': '28,000', '512GB': '33,000'}},
    '8': {'name': 'iPhone 13', 'prices': {'128GB': '20,000', '256GB': '24,000', '512GB': '29,000'}},
}

# بيانات الاكسسوارات الحالية
current_accessories = {
    '1': {'name': 'سماعات AirPods Pro 2', 'price': '8,500'},
    '2': {'name': 'سماعات AirPods 3', 'price': '6,000'},
    '3': {'name': 'Apple Watch Series 10', 'price': '15,000'},
    '4': {'name': 'شاحن MagSafe', 'price': '1,800'},
    '5': {'name': 'كفر سيليكون أصلي', 'price': '1,200'},
    '6': {'name': 'كفر جلد أصلي', 'price': '2,000'},
    '7': {'name': 'واقي شاشة زجاجي', 'price': '300'},
    '8': {'name': 'كابل Lightning أصلي', 'price': '800'},
    '9': {'name': 'كابل USB-C أصلي', 'price': '900'},
    '10': {'name': 'محول Lightning to 3.5mm', 'price': '500'},
}

def show_iphones():
    print("\n📱 الأيفونات الحالية:\n")
    for key, iphone in current_iphones.items():
        print(f"{key}. {iphone['name']}")
        for storage, price in iphone['prices'].items():
            print(f"   - {storage}: {price} جنيه")
        print()

def show_accessories():
    print("\n🎧 الاكسسوارات الحالية:\n")
    for key, acc in current_accessories.items():
        print(f"{key}. {acc['name']}: {acc['price']} جنيه")

def update_iphone_prices():
    show_iphones()
    iphone_id = input("\nاختر رقم الأيفون لتحديث أسعاره: ")
    
    if iphone_id not in current_iphones:
        print("❌ رقم غير صحيح!")
        return
    
    iphone = current_iphones[iphone_id]
    print(f"\n🔄 تحديث أسعار {iphone['name']}\n")
    
    new_prices = {}
    for storage in iphone['prices'].keys():
        old_price = iphone['prices'][storage]
        new_price = input(f"السعر الجديد لـ {storage} (الحالي: {old_price} جنيه): ")
        if new_price:
            new_prices[storage] = new_price.replace(',', '').replace(' ', '')
        else:
            new_prices[storage] = old_price
    
    # تحديث الأسعار
    current_iphones[iphone_id]['prices'] = new_prices
    
    print("\n✅ تم تحديث الأسعار بنجاح!")
    print(f"\n{iphone['name']} - الأسعار الجديدة:")
    for storage, price in new_prices.items():
        print(f"   - {storage}: {price} جنيه")
    
    # إنشاء الكود الجديد
    generate_code_snippet(iphone_id, iphone['name'], new_prices, 'iphone')

def update_accessory_price():
    show_accessories()
    acc_id = input("\nاختر رقم الاكسسوار لتحديث سعره: ")
    
    if acc_id not in current_accessories:
        print("❌ رقم غير صحيح!")
        return
    
    acc = current_accessories[acc_id]
    print(f"\n🔄 تحديث سعر {acc['name']}")
    print(f"السعر الحالي: {acc['price']} جنيه")
    
    new_price = input("السعر الجديد: ")
    if new_price:
        current_accessories[acc_id]['price'] = new_price.replace(',', '').replace(' ', '')
        
        print(f"\n✅ تم تحديث السعر بنجاح!")
        print(f"{acc['name']}: {current_accessories[acc_id]['price']} جنيه")
        
        # إنشاء الكود الجديد
        generate_code_snippet(acc_id, acc['name'], current_accessories[acc_id]['price'], 'accessory')

def add_new_iphone():
    print("\n➕ إضافة أيفون جديد\n")
    
    name = input("اسم الأيفون (مثال: iPhone 17 Pro): ")
    
    print("\nأدخل الأسعار للمساحات التالية (اضغط Enter للتخطي):")
    prices = {}
    
    for storage in ['128GB', '256GB', '512GB', '1TB']:
        price = input(f"سعر {storage}: ")
        if price:
            prices[storage] = price.replace(',', '').replace(' ', '')
    
    if not prices:
        print("❌ يجب إدخال سعر واحد على الأقل!")
        return
    
    # إضافة للقائمة
    new_id = str(len(current_iphones) + 1)
    current_iphones[new_id] = {'name': name, 'prices': prices}
    
    print(f"\n✅ تم إضافة {name} بنجاح!")
    generate_code_snippet(new_id, name, prices, 'iphone')

def add_new_accessory():
    print("\n➕ إضافة اكسسوار جديد\n")
    
    name = input("اسم الاكسسوار: ")
    price = input("السعر: ")
    
    if not price:
        print("❌ يجب إدخال السعر!")
        return
    
    # إضافة للقائمة
    new_id = str(len(current_accessories) + 1)
    current_accessories[new_id] = {'name': name, 'price': price.replace(',', '').replace(' ', '')}
    
    print(f"\n✅ تم إضافة {name} بنجاح!")
    generate_code_snippet(new_id, name, price, 'accessory')

def generate_code_snippet(item_id, name, prices, item_type):
    """إنشاء كود جاهز للنسخ"""
    print("\n" + "="*50)
    print("📋 انسخ الكود التالي وضعه في ملف whatsapp_iphone_bot.py:")
    print("="*50 + "\n")
    
    if item_type == 'iphone':
        print(f"'{item_id}': {{")
        print(f"    'name': '{name}',")
        print(f"    'storage': {list(prices.keys())},")
        print(f"    'colors': ['لون 1', 'لون 2', 'لون 3'],  # عدّل الألوان")
        for storage, price in prices.items():
            storage_key = storage.lower().replace('gb', '').replace('tb', 'tb')
            print(f"    'price_{storage_key}': '{price} جنيه',")
        print(f"    'features': 'أضف المواصفات هنا'")
        print("},")
    
    elif item_type == 'accessory':
        print(f"'{item_id}': {{")
        print(f"    'name': '{name}',")
        print(f"    'price': '{prices} جنيه',")
        print(f"    'desc': 'أضف الوصف هنا'")
        print("},")
    
    print("\n" + "="*50)

def show_all_prices():
    print("\n" + "="*50)
    print("💰 جميع الأسعار الحالية")
    print("="*50)
    
    show_iphones()
    print("\n" + "-"*50 + "\n")
    show_accessories()

def main():
    while True:
        print_menu()
        choice = input("اختيارك: ")
        
        if choice == '1':
            update_iphone_prices()
        elif choice == '2':
            update_accessory_price()
        elif choice == '3':
            add_new_iphone()
        elif choice == '4':
            add_new_accessory()
        elif choice == '6':
            show_all_prices()
        elif choice == '0':
            print("\n👋 مع السلامة!")
            break
        else:
            print("❌ اختيار غير صحيح!")
        
        input("\n📌 اضغط Enter للمتابعة...")

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════╗
║                                                  ║
║         🛠️  أداة تحديث الأسعار                   ║
║         محل أحمد الصعيدي للموبايلات             ║
║                                                  ║
╚══════════════════════════════════════════════════╝
    """)
    main()
