GENERAL INFO

FOR GROUP MEMBER INFORMATION

--ADDING TABLES---

Add DB model to models.py 

then load DB instance in python and excute "db.create_all()" to a add new table.

--ADDING DATA-- 

CREATE INSTANCE OF MODEL WITH REQUIRED INFO EG:
> testToAdd = test("John Smith")
ADD TO DB AND COMMIT CHANGES
> db.add(testToAdd)
> db.commit() 

References/Sources 
