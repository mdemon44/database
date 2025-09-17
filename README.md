# 🏦 Bank Management System (Python + MySQL)

## 📖 Project Overview
This project is a **Bank Management System** built with **Python (for logic)** and **MySQL (for data storage)**.  
It simulates real-world banking operations, enabling users to perform **account management and transaction handling** through a command-line interface.  

The system is designed with **data integrity, usability, and persistence** in mind, making it a great foundation for understanding **database-driven applications**.

---

## ✨ Key Features
- **Account Creation** → Auto-generates unique 8-digit account numbers.  
- **Transaction Handling** → Deposit and withdraw funds securely with balance validation.  
- **Balance Enquiry** → Retrieve real-time balance for any account.  
- **Customer Information** → Display account holder details with one query.  
- **Account Closure** → Securely delete accounts with confirmation.  
- **Database Integration** → Persistent data storage in MySQL.

---

## 🗂️ Database Design
The project uses a **normalized database schema** to ensure clarity and data consistency:

1. **`account_table`** – Stores personal and static account details.  
2. **`amount_table`** – Stores financial data and is updated after each transaction.  
3. **`transactions`** – (Optional) Table structure provided for tracking transaction history.

This separation ensures **data modularity**, making it easier to track customer details and balances independently.

---

## ⚙️ Tech Stack
- **Programming Language:** Python 3.x  
- **Database:** MySQL  
- **Connector:** `mysql-connector-python`  

Install requirements:
```bash
pip install mysql-connector-python

## 📸 Preview
![Account Table](sq2.png)  
![Balance View](sq1.png)

---

## ▶️ How to Run
1. Create the database and tables using the provided SQL script:
   ```sql
   SOURCE Create_Database.sql;
   ```

2. Update database credentials in the Python script:
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="YOUR_PASSWORD",  # Change to your MySQL password
       database="BANK_MANAGEMENT"
   )
   ```

3. Run the program:
   ```bash
   python Bank_Management_python_code.py
   ```

---

## 🐛 Error Handling & Solutions
The system includes comprehensive error handling:

1. **Date Format Validation** – Ensures dates are entered in YYYY-MM-DD format  
   ```python
   # Example: '2004-09-26' instead of '26-09-2004'
   ```

2. **Insufficient Balance Check** – Prevents overdrafts  
   ```python
   if amt > balance:
       print("❌ Insufficient Balance!")
   ```

3. **Account Existence Verification** – Validates account numbers before operations  
   ```python
   if not result:
       print("❌ Account not found!")
   ```

4. **Confirmation for Critical Actions** – Prevents accidental account deletion  
   ```python
   confirm = input("⚠️ Are you sure you want to close this account? (y/n): ")
   ```

---

## 📈 Outcomes & Impact
- Simplified banking operations in a **digital format**  
- Provided a **learning foundation** for database-driven applications  
- Enhanced understanding of **Python-MySQL integration**  
- Built a base that can be extended into **web apps or GUIs**

---

## 🌟 Future Improvements
- Add **user authentication & roles (Admin/Customer)**  
- Implement **transaction history logging** using the transactions table  
- Build a **GUI (Tkinter/Flask/Django)** for better usability  
- Add **email notifications** for transactions  
- Deploy on **cloud with remote database access**

---

## 📁 Project Structure
```
Bank-Management-System/
│
├── Bank_Management_python_code.py  # Main application
├── Create_Database.sql             # Database schema
├── README.md                       # Project documentation
├── sq1.png                         # Balance view screenshot
├── sq2.png                         # Account table screenshot
├── b1.png, b2.png, b3.png          # Application screenshots
└── e1.png, e2.png, e3.png          # Error handling examples
```

---

## 👥 Contributing
Feel free to contribute to this project by:
1. Forking the repository  
2. Creating a feature branch  
3. Submitting a pull request

---

## 📄 License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## ⭐ Support
If you find this project useful, please consider giving it a **star ⭐** on GitHub — it motivates me to improve and share more projects!
```

