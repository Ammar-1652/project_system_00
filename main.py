#main.oop file
#that is a file for me (Ammar) to work on oop and make sure every thing is going well "just ignore it"
from oop import *


# Create instances of Student, Instructor, Professor, and Professor_asst
student = Student()
student2 = Student()
student3=Student()
student4=Student()

professor = Professor()
professor2=Professor()

professor_asst = Professor_asst()
professor_asst2 = Professor_asst()

admin=Admin()

course1 = Courses()
course2 = Courses()
course3 = Courses()
course4 = Courses()

course1.add_new_course("Math101", 3, False)
course2.add_new_course("Physics201", 4, False)
course3.add_new_course("ChemistryLab", 2, True)
course4.add_new_course("BiologyLab", 2, True)



# Assign values to Student's attributes
student.set_first_name("Alice")
student.set_middle_name("ahmed")
student.set_last_name("Smith")
student.set_personal_id("987654")
student.set_contact_num("987-654-3210")
student.set_email("alice.smith@example.com")
student.set_date_of_birth("03/20/1995")
student.set_level(2)
student.set_department("Mathematics")
student.set_date_of_birth("05/16/2004")

#student.assign_values()


student2.set_first_name("John")
student2.set_middle_name("ahmed")
student2.set_last_name("Doe")
student2.set_personal_id("987654")
student2.set_contact_num("123-456-7890")
student2.set_email("john.doe@example.com")
student2.set_date_of_birth("01/15/1998")
student2.set_level(2)

student2.set_department("Computer Science")
student2.assign_values()


student3.set_first_name("Alice")
student3.set_middle_name("ahmed")
student3.set_last_name("Smith")
student3.set_personal_id("S67890")
student3.set_contact_num("987-654-3210")
student3.set_email("alice.smith@example.com")
student3.set_date_of_birth("03/22/2000")

student3.set_level(1)
student3.set_department("Electrical Engineering")
student3.assign_values()


student4.set_first_name("Eva")
student4.set_middle_name("ahmed")
student4.set_last_name("Johnson")
student4.set_personal_id("S54321")
student4.set_contact_num("555-123-4567")
student4.set_email("eva.johnson@example.com")
student4.set_date_of_birth("05/10/1999")

student4.set_level(3)
student4.set_department("Mechanical Engineering")
student4.assign_values()



# Assign values to Professor's attributes
professor.set_first_name("Charlie")
professor.set_middle_name("ahmed")
professor.set_last_name("Brown")
professor.set_personal_id("653525")
professor.set_contact_num("654-321-0987")
professor.set_email("charlie.brown@example.com")
professor.set_date_of_birth("07/25/1975")
professor.set_department("Electrical Engineering")
professor.set_salary(70000)
professor.assign_values()



professor2.set_first_name("John")
professor2.set_middle_name("ahmed")
professor2.set_last_name("Doe")
professor2.set_personal_id("P98765")
professor2.set_contact_num("555-987-6543")
professor2.set_email("john.doe@example.com")
professor2.set_date_of_birth("12/15/1970")
professor2.set_department("Computer Science")
professor2.set_salary(90000)    
professor2.assign_values()



# Assign values to Professor_asst's attributes
professor_asst.set_first_name("David")
professor_asst.set_middle_name("ahmed")
professor_asst.set_last_name("Clark")
professor_asst.set_personal_id("789012")
professor_asst.set_contact_num("789-012-3456")
professor_asst.set_email("david.clark@example.com")
professor_asst.set_date_of_birth("09/18/1992")
professor_asst.set_department("Computer science")
professor_asst.set_salary(60000)
professor_asst.assign_values()

professor_asst2.set_first_name("Alice")
professor_asst2.set_middle_name("ahmed")
professor_asst2.set_last_name("Smith")
professor_asst2.set_personal_id("PA12345")
professor_asst2.set_contact_num("555-123-4567")
professor_asst2.set_email("alice.smith@example.com")
professor_asst2.set_date_of_birth("05/20/1985")
professor_asst2.set_department("Physics")
professor_asst2.set_salary(60000)
professor_asst2.assign_values()


course1.set_professor_teaching_course(professor)
course2.set_professor_teaching_course(professor)
course3.set_professor_teaching_course(professor2)
course4.set_professor_teaching_course(professor2)



course3.set_assistant_giving_lab(professor_asst)
course4.set_assistant_giving_lab(professor_asst2)



student.enroll_in_course(course1) 
student.enroll_in_course(course3) 


student2.enroll_in_course(course1) 
student2.enroll_in_course(course2) 


student3.enroll_in_course(course3) 
student3.enroll_in_course(course2)


student4.enroll_in_course(course1) 
student4.enroll_in_course(course4) 


# print(student.get_enrolled_courses())
# print(professor.get_students_teaching(1))
# print(student.get_age())
# print(student.get_profile_id())
# print(student2.get_profile_id())
# print(professor2.get_profile_id())
# print(professor.get_profile_id())
# print(professor_asst.get_profile_id())



# print(student.get_is_admin())
# print(student.get_role())
# print(student.get_profile_approved())
# print("=========================================")
# print(professor.get_is_admin())
# print(professor.get_role())
# print(professor.get_profile_approved())
# print("=========================================")
# print(professor_asst.get_is_admin())
# print(professor_asst.get_role())
# print(professor_asst.get_profile_approved())
# print("=========================================")
# print(admin.get_is_admin())
# print(admin.get_role())
# print(admin.get_profile_approved())

