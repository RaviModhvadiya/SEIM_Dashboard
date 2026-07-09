USE SEIM_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Admin','Analyst','User') DEFAULT 'User',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

USE SEIM_db;

CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,

    filename VARCHAR(255) NOT NULL,

    log_type VARCHAR(50) NOT NULL,

    uploaded_by INT NOT NULL,

    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    status ENUM('Uploaded','Parsed') DEFAULT 'Uploaded',

    FOREIGN KEY(uploaded_by)
        REFERENCES users(id)
        ON DELETE CASCADE
);