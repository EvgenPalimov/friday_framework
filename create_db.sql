PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS type_course;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS teacher;
DROP TABLE IF EXISTS course_type_course;
DROP TABLE IF EXISTS category;

CREATE TABLE type_course
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name VARCHAR(32)                       NOT NULL
);


CREATE TABLE course
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name    VARCHAR(32)                       NOT NULL
);

CREATE TABLE course_type_course
(
    course_id INTEGER NOT NULL,
    type_course_id  INTEGER NOT NULL,
    FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE,
    FOREIGN KEY (type_course_id) REFERENCES type_course (id) ON DELETE CASCADE
);

CREATE TABLE student
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    first_name VARCHAR(32)                       NOT NULL,
    last_name  VARCHAR(32)                       NOT NULL,
    age        INTEGER,
    phone      VARCHAR(20)                       NOT NULL UNIQUE,
    email      VARCHAR(32)                       NOT NULL UNIQUE,
    cource_id  INTEGER,
    FOREIGN KEY (cource_id) REFERENCES course (id) ON DELETE SET NULL
);

CREATE TABLE teacher
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    first_name VARCHAR(32)                       NOT NULL,
    last_name  VARCHAR(32)                       NOT NULL,
    phone      VARCHAR(20)                       NOT NULL UNIQUE,
    email      VARCHAR(32)                       NOT NULL UNIQUE,
    cource_id  INTEGER,
    student_id INTEGER,
    FOREIGN KEY (cource_id) REFERENCES course (id) ON DELETE SET NULL,
    FOREIGN KEY (student_id) REFERENCES student (id) ON DELETE SET NULL
);


CREATE TABLE category
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name       VARCHAR(32)                       NOT NULL,
    cource_id  INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (cource_id) REFERENCES course (id) ON DELETE SET NULL,
    FOREIGN KEY (teacher_id) REFERENCES teacher (id) ON DELETE SET NULL
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
