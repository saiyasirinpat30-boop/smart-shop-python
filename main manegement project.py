students = []
while True:
    print("\n===== MENU =====")
    print("1. เพิ่มนักเรียน")
    print("2. เเสดงรายชื่อ")
    print("3. ค้นหานักเรียน")
    print("4. ลบนักเรียน")
    print("5. ออกจากโปรเเกรม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        student_id = input("รหัสนักเรียน: ")
        name = input("ชื่อนักเรียน: ")
        student = {
            "id": student_id,
            "name": name
        }
        students.append(student)
        print("เพิ่มข้อมูลสำเร็จ")
    elif choice == "2":
        print("\nรายชื่อนักเรียน")
        if len(students) == 0:
            print("ยังไม่มีข้อมูล")
        else:
            for student in students:
                print(
                    f"รหัส: {student['id']} | ชื่อ: {student['name']}"
                    )
    elif choice == "3":
        search_id = input("กรอกรหัสนักเรียน: ")
        found = False
        for student in students:
            if student["id"] == search_id:
                print(
                    f"พบข้อมูล -> รหัส: {student['id']} | ชื่อ: {student['name']}"
                )
                found = True
                break
        if not found:
            print("ไม่พบข้อมูล")
    elif choice == "4":
        delete_id = input("กรอกรหัสนักเรียนที่ต้องการลบ: ")
        found = False
        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("ลบข้อมูลสำเร็จ")
                found = True
                break
        if not found:
            print("ไม่พบรหัสนักเรียน")
    elif choice == "5":
        print("ออกจากโปรเเกรม")
        break
    else:
        print("กรุณาเลือกเมนู 1-5")