-- CREATE DATABASE BANK_MANAGEMENT;
USE BANK_MANAGEMENT;
CREATE TABLE ACCOUNT_TABLE(
Name VARCHAR(50) NOT NULL,
AccNo INT(20) PRIMARY KEY NOT NULL ,
DOB DATE ,
Address TEXT NOT NULL,
ContactNO BIGINT NOT NULL,
Opening_Balance decimal NOT NULL);

CREATE TABLE AMOUNT_TABLE(
Name VARCHAR(50) NOT NULL,
AccNo INT(20) NOT NULL,
Balance decimal NOT NULL);

CREATE TABLE transactions (
    TransID INT AUTO_INCREMENT PRIMARY KEY,   -- unique transaction ID
    AccNo INT(8) NOT NULL,                   -- account number (must exist in ACCOUNT_TABLE)
    TransType VARCHAR(20) NOT NULL,          -- 'Deposit', 'Withdrawal', etc.
    Amount DECIMAL(10,2) NOT NULL,           -- transaction amount
    TransDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- auto date/time
    FOREIGN KEY (AccNo) REFERENCES ACCOUNT_TABLE(AccNo) ON DELETE CASCADE -- link to account table
);

SELECT * FROM ACCOUNT_TABLE;
SELECT * FROM AMOUNT_TABLE;

DESC ACCOUNT_TABLE;
DESC AMOUNT_TABLE;