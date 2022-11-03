import sqlite3

a=int(input("Запис чи виведення данних? 1-запис, 2-виведення \n"))

if a == 1:
    rec = int(input("Уведіть 1, якщо потрібно занести в картку дані пацієнта \n 2, якщо хочете ввести дані для лікаря\n"))

    if rec == 1:
        a1 = input("Номер пацієнта: ")
        a2 = input("ПІБ пацієнта: ")
        a3 = input("адреса: ")
        a4 = input("стать: ")
        a5 = input("вік: ")
        a6 = input("номер страхового полісу: ")
        a7 = input("дата відвідування: ")
        a8 = input("скарги: ")
        a9 = input("діагноз: ")
        a10 = input("призначення лікарів: ")
        a11 = input("лікар пацієнта: ")
        a12 = input("дата заповнення картки пацієнта: ")
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query1 = f"""INSERT INTO пацієнти (номер, піб, адреса, стать, вік, номер_страхового_полісу, дата_відвідування, скарги, діагноз, призначення, лікар, дата_заповнення_картки)
                VALUES ("{a1}", "{a2}", "{a3}", "{a4}", "{a5}", "{a6}", "{a7}", "{a8}", "{a9}", "{a10}", "{a11}", "{a12}")"""
            cursor.execute(query1)

    if rec == 2:
        b1 = input("ПІБ лікаря: ")
        b2 = input("категорія: ")
        b3 = input("стаж: ")
        b4 = input("дата народження: ")
        b5 = input("ділянка: ")
        b6 = input("час прийому: ")
        b7 = input("номер кабінету: ")
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query1 = f"""INSERT INTO лікарі (піб, категорія, стаж, дата_народження, ділянка, час_прийому, номер_кабінету)
                VALUES ("{b1}", "{b2}", "{b3}", "{b4}", "{b5}", "{b6}", "{b7}")"""
            cursor.execute(query1)

        


if a == 2:
    usatel = int(input("Що вам потрібно дізнати? \
        \nУведіть:\
        \n1 якщо хочете дізнатись про дані хворого, \
        \n2- прізвища та ініціали лікаря даного хворого, \
        \n3-номер кабінету та час прийому, \
        \n4-хворі що знаходятсья на лікуванні у даного лікаря, \
        \n5- Призначення лікарів при зазначеному захворюванні, \
        \n6- хто працює в даний момент в зазначеному кабінеті, \
        \n7- скільки разів за минулий місяць звертався до клініки хворий,\
        \n8- яку кількість хворих обслужив за минулий місяць кожен з лікарів клініки. \n"))
    if usatel == 1:
        abobik = int(input("1-вивести дані про усіх пацієнтів, 2-дані конкретного пацієнта: "))
        if abobik == 1:
            with sqlite3.connect('database.db') as db:
                cursor = db.cursor()
                query = """SELECT * FROM пацієнти"""
                cursor.execute(query)
                for res in cursor:
                    print(res)
        if abobik == 2:
            bobik = str(input("Будь ласка, уведіть ПІБ пацієнта: "))
            with sqlite3.connect('database.db') as db:
                cursor = db.cursor()
                query = f"""SELECT * FROM пацієнти WHERE піб == '{bobik}'"""
                cursor.execute(query)
                for res in cursor:
                    print(res)

    if usatel == 2:
        bobik_1 = str(input("Будь ласка, уведіть ПІБ пацієнта: "))
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query = f"""SELECT лікар FROM пацієнти WHERE піб == '{bobik_1}'"""
            cursor.execute(query)
            for res in cursor:
                print("ПІБ лікаря: ", res)
    
    if usatel == 3:
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query = f"""SELECT номер, час_прийому FROM кабінети"""
            cursor.execute(query)
            for res in cursor:
                print(res)

    
    if usatel == 4:
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query_bobik = """SELECT лікар FROM пацієнти"""
            query_aboba = """SELECT піб FROM пацієнти"""
            glek = cursor.execute(query_bobik)
            glek_1 = cursor.execute(query_aboba)
            for res in glek:
                query1 = f"""INSERT INTO кабінети (лікар)
                    VALUES ("{res}")"""
                query2 = f"""INSERT INTO лікарі (піб)
                    VALUES ("{res}")"""
                cursor.execute(query1)
                cursor.execute(query2)
            for res in glek_1:
                query3 = f"""INSERT INTO лікарі (хворі)
                    VALUES ("{res}")"""
                cursor.execute(query3)
        query4 = f"""SELECT піб, хворі FROM лікарі"""
        glek_2 = cursor.execute(query4)
        for res in glek_2:
            print(res)
        

    
    if usatel == 5:
        bobik_2 = str(input("Будь ласка, уведіть ПІБ пацієнта: "))
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query = f"""SELECT призначення FROM пацієнти WHERE піб == '{bobik_2}'"""
            cursor.execute(query)
            for res in cursor:
                print('Назначення: ', res)

    if usatel == 6:
        bobik_3 = int(input("Будь ласка, уведіть номер кабінету: "))
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            query = f"""SELECT лікар FROM кабінети Where номер == '{bobik_3}'"""
            cursor.execute(query)
            for res in cursor:
                print('У даному кабінеті працює лікар: ', res)
