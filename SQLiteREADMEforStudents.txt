SQLITE GENERAL INFO

FOR GROUP MEMBER INFORMATION

GUI INFERACE FOR SQL VIA 'DB BROSWER FOR SQLITE"
FREE INSTALL ON PERSONAL PCS
CAN GET ON UNI LAPTOPS VIA ZENworks. 

SQLite require no installtion to work with python, python can acess it nativly. 

To use with in this server interact VIA sql_alchemy 

--ADDING TABLES---

Add DB model to models.py 

then load DB instance in python and excute "db.create_all()" to a add new table.

--ADDING DATA-- 

CREATE INSTANCE OF MODEL WITH REQUIRED INFO EG:
> testToAdd = test("John Smith")
ADD TO DB AND COMMIT CHANGES
> db.add(testToAdd)
> db.commit() 