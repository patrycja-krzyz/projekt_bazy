CREATE OR REPLACE TABLE pracownicy (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
imię_i_nazwisko VARCHAR(50),
płeć ENUM('kobieta', 'mężczyzna') NOT NULL
);