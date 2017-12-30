INSERT INTO marks_system_examination (name, date) VALUES ('MathsExam', '2018-01-26 22:28:15');
INSERT INTO marks_system_examination (name, date) VALUES ('EnglishExam', '2018-01-27 22:30:37');

INSERT INTO marks_system_student (last_name, first_name, birth_date) VALUES ('BERTRAND', 'Guillaume', '1995-07-21 22:34:23');
INSERT INTO marks_system_student (last_name, first_name, birth_date) VALUES ('BOUGUETTOUCHA', 'Khaled', '1995-03-07 22:39:02');
INSERT INTO marks_system_student (last_name, first_name, birth_date) VALUES ('JACQUET', 'Anne', '1995-05-18 22:45:39');

INSERT INTO marks_system_course (code, subject, start_date, end_date, examination_id) VALUES ('M101', 'Maths', '2017-12-26 22:48:22', '2018-01-28 22:48:30', 1);
INSERT INTO marks_system_course (code, subject, start_date, end_date, examination_id) VALUES ('E101', 'English', '2017-12-26 22:49:01', '2018-01-31 22:49:08', 2);

INSERT INTO marks_system_mark (mark, examination_id) VALUES (20, 1);
INSERT INTO marks_system_mark (mark, examination_id) VALUES (19, 1);
INSERT INTO marks_system_mark (mark, examination_id) VALUES (19.5, 1);
INSERT INTO marks_system_mark (mark, examination_id) VALUES (15, 2);
INSERT INTO marks_system_mark (mark, examination_id) VALUES (17, 2);

INSERT INTO marks_system_mark_students (mark_id, student_id) VALUES (1, 3);
INSERT INTO marks_system_mark_students (mark_id, student_id) VALUES (2, 1);
INSERT INTO marks_system_mark_students (mark_id, student_id) VALUES (3, 2);
INSERT INTO marks_system_mark_students (mark_id, student_id) VALUES (4, 3);
INSERT INTO marks_system_mark_students (mark_id, student_id) VALUES (5, 1);
INSERT INTO marks_system_mark_students (mark_id, student_id) VALUES (5, 2);

INSERT INTO marks_system_course_students (course_id, student_id) VALUES (1, 2);
INSERT INTO marks_system_course_students (course_id, student_id) VALUES (1, 3);
INSERT INTO marks_system_course_students (course_id, student_id) VALUES (2, 1);
INSERT INTO marks_system_course_students (course_id, student_id) VALUES (2, 2);
INSERT INTO marks_system_course_students (course_id, student_id) VALUES (2, 3);
