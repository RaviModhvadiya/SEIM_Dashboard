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

USE SEIM_db;

CREATE TABLE log_entries (

    id INT AUTO_INCREMENT PRIMARY KEY,

    log_id INT NOT NULL,

    event_time DATETIME NULL,

    event_level VARCHAR(50),

    source VARCHAR(100),

    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (log_id)
        REFERENCES logs(id)
        ON DELETE CASCADE
);

USE SEIM_db;

CREATE TABLE alerts (

    id INT AUTO_INCREMENT PRIMARY KEY,

    log_entry_id INT NOT NULL,

    alert_type VARCHAR(100),

    severity ENUM(
        'Low',
        'Medium',
        'High',
        'Critical'
    ),

    description TEXT,

    status ENUM(
        'Open',
        'Resolved'
    ) DEFAULT 'Open',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (log_entry_id)
        REFERENCES log_entries(id)
        ON DELETE CASCADE
);