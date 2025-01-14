## SQL QUERIES LECTURE
### 4. Basic SQL CRUD Queries
- **INSERT:** Inserts data into the students table.
  - Example:
    ```sql
    INSERT INTO students (student_name, email, status) VALUES ('Alice Johnson', 'alice.johnson@example.com', 'active');
    ```

- **SELECT**: Retrieves all records from the `students` table.
  - Example:
    ```sql
    SELECT * FROM students;
    ```
- **SELECT with Filters**:
  - Example:
    ```sql
    SELECT * FROM students WHERE student_name = 'Alice Johnson';
    ```
- **UPDATE**: Updates the email of the student named 'Alice Johnson'.
  - Example:
    ```sql
    UPDATE students SET email = 'alicejohnson@example.com' WHERE student_name = 'Alice Johnson';
    ```
- **DELETE**: Removes the student named 'Alice Johnson' from the table.
  - Example:
    ```sql
    DELETE FROM students WHERE student_name = 'Alice Johnson';
    ```

## JOINs
- **Inner JOIN**: Combines data from `students`, `enrollments`, and `courses`.
  - Example:
    ```sql
    SELECT students.student_name, courses.title 
    FROM students 
    JOIN enrollments ON students.id = enrollments.student_id 
    JOIN courses ON enrollments.course_id = courses.id;
    ```
- **LEFT JOIN**: Returns all students, even those not enrolled in courses.
  - Example:
    ```sql
    SELECT students.student_name, courses.title 
    FROM students 
    LEFT JOIN enrollments ON students.id = enrollments.student_id 
    LEFT JOIN courses ON enrollments.course_id = courses.id;
    ```

## Other SQL Operators
- **WHERE Clause**: Filters records where the email contains 'example.com'.
  - Example:
    ```sql
    SELECT * FROM students WHERE email LIKE '%example.com';
    ```
- **ORDER BY Clause**: Sorts students by `student_name` in ascending order.
  - Example:
    ```sql
    SELECT * FROM students ORDER BY student_name ASC;
    ```
- **LIMIT/OFFSET Clause**: Retrieves 10 students starting from the 6th student.
  - Example:
    ```sql
    SELECT * FROM students ORDER BY student_name ASC LIMIT 10 OFFSET 5;
    ```