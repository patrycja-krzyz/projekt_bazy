CREATE TABLE IF NOT EXISTS attractions (
    attraction_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    attraction_name VARCHAR(50),
    built_date DATETIME
);

CREATE TABLE IF NOT EXISTS inspections (
    inspection_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    attraction_id INT UNSIGNED,
    inspection_date DATETIME,
    result VARCHAR(200),
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
);

CREATE TABLE IF NOT EXISTS malfunctions (
    malfunction_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    attraction_id INT UNSIGNED NOT NULL,
    accident_date DATETIME NOT NULL,
    fix_date DATETIME,
    comment VARCHAR(400),
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
);

CREATE TABLE IF NOT EXISTS guest (
    guest_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

CREATE TABLE IF NOT EXISTS visit (
    visit_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    guest_id INT UNSIGNED NOT NULL,
    visit_date DATETIME NOT NULL,
    FOREIGN KEY (guest_id) REFERENCES guest(guest_id)
);

CREATE TABLE IF NOT EXISTS incident_type (
    incident_type_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    risk_level INT
);
CREATE TABLE IF NOT EXISTS insurance (
    insurance_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    coverage_amount DECIMAL(10,2)
);
CREATE TABLE IF NOT EXISTS guest_insurance (
    guest_id INT UNSIGNED,
    insurance_id INT UNSIGNED,
    PRIMARY KEY (guest_id, insurance_id),
    FOREIGN KEY (guest_id) REFERENCES guest(guest_id),
    FOREIGN KEY (insurance_id) REFERENCES insurance(insurance_id)
);
CREATE TABLE IF NOT EXISTS incident (
    incident_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    incident_type_id INT UNSIGNED NOT NULL,
    guest_id INT UNSIGNED NOT NULL,
    attraction_id INT UNSIGNED,
    incident_date DATETIME,
    description VARCHAR(400),
    FOREIGN KEY (incident_type_id) REFERENCES incident_type(incident_type_id),
    FOREIGN KEY (guest_id) REFERENCES guest(guest_id),
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
);

CREATE TABLE IF NOT EXISTS costs (
    cost_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    cost_type VARCHAR(50),
    amount DECIMAL(10,2),
    how_often VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    payment_date DATETIME,
    amount DECIMAL(10,2),
    income BOOLEAN NOT NULL, 
    description VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(6,2),
    hire_date DATE
);

CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(4,2),
    ticket_type VARCHAR(50)
);