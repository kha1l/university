-- Выбрать всех студентов, обучающихся на курсе "Математика".
SELECT *
FROM student JOIN course on course.course_id = student.course_id
WHERE course_name='Математика';

-- Обновить оценку студента по курсу.
UPDATE grade
SET value = 5
WHERE student_id = 1 AND course_id = 1;

-- Выбрать всех преподавателей, которые преподают в здании 3.
SELECT *
FROM teacher
JOIN schedule ON teacher.teacher_id = schedule.teacher_id
JOIN auditorium on schedule.auditorium_id = auditorium.auditorium_id
JOIN building ON auditorium.building_id = building.building_id
WHERE building.building_id = 3;

-- Удалить задание для самостоятельной работы, которое было создано более года назад
DELETE FROM homework
WHERE homework_date < CURRENT_DATE - interval '1 year';

-- Добавить новый семестр в учебный год.
INSERT INTO semester (semester_name, start_date, end_date)
VALUES ('Первый семестр', '2023-09-01', '2024-01-01');
