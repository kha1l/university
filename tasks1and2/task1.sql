-- Создание таблицы факультет 
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL
);

-- Создание таблицы департамент
CREATE TABLE Department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    faculty_id INT REFERENCES Faculty(faculty_id)
);

-- Создание таблицы группа
CREATE TABLE Group_ (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES Department(department_id)
);

-- Создание таблицы курс
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES Department(department_id)
);

-- Создание таблицы студент
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    birth DATE,
    phone VARCHAR(30),
    group_id INT REFERENCES Group_(group_id),
    course_id INT REFERENCES Course(course_id)
);

-- Создание таблицы преподаватель
CREATE TABLE Teacher (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    birth DATE,
    phone VARCHAR(30),
    department_id INT REFERENCES Department(department_id)
);

-- Создание таблицы семестр
CREATE TABLE Semester (
    semester_id SERIAL PRIMARY KEY,
    semester_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Создание таблицы оценка
CREATE TABLE Grade (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Student(student_id),
    course_id INT REFERENCES Course(course_id),
    semester_id INT REFERENCES Semester(semester_id),
    value FLOAT
);

-- Создание таблицы здание
CREATE TABLE Building (
    building_id SERIAL PRIMARY KEY,
    building_name VARCHAR(100) NOT NULL,
    building_number INT NOT NULL
);

-- Создание таблицы аудитория
CREATE TABLE Auditorium (
    auditorium_id SERIAL PRIMARY KEY,
    auditorium_number VARCHAR(20) NOT NULL,
    building_id INT REFERENCES Building(building_id)
);

-- Создание таблицы рассписание
CREATE TABLE Schedule (
    schedule_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Course(course_id),
    teacher_id INT REFERENCES Teacher(teacher_id),
    auditorium_id INT REFERENCES Auditorium(auditorium_id),
    date_lesson DATE,
    day_of_week VARCHAR(20),
    start_time TIME,
    end_time TIME
);

-- Создание таблицы экзамен
CREATE TABLE Exam (
    exam_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Course(course_id),
    semester_id INT REFERENCES Semester(semester_id),
    exam_date DATE,
    start_time TIME,
    end_time TIME
);

-- Создание таблицы самостоятельная работа
CREATE TABLE Homework (
    homework_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Course(course_id),
    semester_id INT REFERENCES Semester(semester_id),
    homework_date DATE,
    deadline DATE,
    description TEXT
);

-- Создание таблицы программа курса
CREATE TABLE Program (
    program_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Course(course_id),
    semester_id INT REFERENCES Semester(semester_id),
    description TEXT
);

-- Создание таблицы учебный план
CREATE TABLE Syllabus (
    syllabus_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Course(course_id),
    semester_id INT REFERENCES Semester(semester_id),
    description TEXT
);