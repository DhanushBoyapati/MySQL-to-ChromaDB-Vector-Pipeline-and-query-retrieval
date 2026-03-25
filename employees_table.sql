CREATE DATABASE company_db;
USE company_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    role VARCHAR(100),
    experience INT,
    skills TEXT
);

INSERT INTO employees (name, department, role, experience, skills) VALUES
('Rahul Sharma','AI','ML Engineer',3,'Python, Deep Learning, NLP'),
('Sneha Reddy','AI','Data Scientist',4,'Python, Statistics, Machine Learning'),
('Arjun Patel','Backend','Software Engineer',2,'Java, Spring Boot, MySQL'),
('Priya Nair','Frontend','UI Developer',2,'React, JavaScript, CSS'),
('Vikram Singh','Cloud','DevOps Engineer',5,'AWS, Docker, Kubernetes'),
('Neha Kapoor','Security','Cybersecurity Analyst',4,'Network Security, SIEM'),
('Kiran Kumar','AI','Computer Vision Engineer',3,'OpenCV, CNN, PyTorch'),
('Anjali Mehta','Data','Data Analyst',2,'SQL, Power BI, Excel'),
('Rohit Verma','Backend','API Developer',3,'Node.js, Express, MongoDB'),
('Pooja Das','Cloud','Cloud Architect',6,'Azure, Terraform, Kubernetes');