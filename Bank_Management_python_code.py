import mysql.connector

# ------------------ DB CONNECTION ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sehr@123",
    database="BANK_MANAGEMENT"
)
cur = conn.cursor()

# ------------------ MAIN MENU ------------------
def start():
    print('''
    ====== BANK MANAGEMENT SYSTEM ======
    1. OPEN NEW ACCOUNT 
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE ACCOUNT
    0. EXIT
    =====================================
    ''')
    choice = input("Enter the task number you want to perform: ")

    if choice == '1':
        openAcc()
    elif choice == '2':
        deposit_Amt()
    elif choice == '3':
        withdraw_Amt()
    elif choice == '4':
        balance_Enq()
    elif choice == '5':
        customer_Details()
    elif choice == '6':
        close_Acc()
    elif choice == '0':
        print("Exiting... Thank you for using our system!")
        conn.close()
        exit()
    else:
        print("❌ Invalid choice. Try again!")
        start()

# ------------------ OPEN NEW ACCOUNT ------------------
def openAcc():
    name = input('Enter Your Name: ')
    dob = input('Enter Your Date of Birth (YYYY-MM-DD): ')
    add = input('Enter Your Address: ')
    Con = input('Enter Your Contact Number: ')
    open_bal = float(input('Enter Your Opening Balance: '))

    # ✅ Generate 8-digit Account Number
    cur.execute("SELECT MAX(AccNo) FROM account_table")
    last_acc = cur.fetchone()[0]
    acc_no = 10000000 if last_acc is None else last_acc + 1

    # Insert into both tables
    sql1 = """INSERT INTO account_table (AccNo, Name, DOB, Address, ContactNO, Opening_Balance) 
              VALUES (%s,%s,%s,%s,%s,%s)"""
    sql2 = """INSERT INTO amount_table (AccNo, Name, Balance) 
              VALUES (%s,%s,%s)"""
    cur.execute(sql1, (acc_no, name, dob, add, Con, open_bal))
    cur.execute(sql2, (acc_no, name, open_bal))
    conn.commit()

    print("\n✅ Account Created Successfully!")
    print("Your Account Number is:", acc_no)
    start()

# ------------------ DEPOSIT AMOUNT ------------------
def deposit_Amt():
    Account_No = int(input('Enter Your Account Number: '))
    amt = float(input('Enter the Amount you want to Deposit: '))

    # Check if account exists
    cur.execute("SELECT Balance FROM amount_table WHERE AccNo=%s", (Account_No,))
    result = cur.fetchone()
    if not result:
        print("❌ Account not found!")
    else:
        cur.execute("UPDATE amount_table SET Balance=Balance+%s WHERE AccNo=%s", (amt, Account_No))
        conn.commit()
        print("✅ Amount successfully deposited!")

    start()

# ------------------ WITHDRAW AMOUNT ------------------
def withdraw_Amt():
    Account_No = int(input('Enter Your Account Number: '))
    amt = float(input('Enter the Amount you want to Withdraw: '))

    # Check balance first
    cur.execute("SELECT Balance FROM amount_table WHERE AccNo=%s", (Account_No,))
    result = cur.fetchone()
    if not result:
        print("❌ Account not found!")
    else:
        balance = result[0]
        if amt > balance:
            print("❌ Insufficient Balance!")
        else:
            cur.execute("UPDATE amount_table SET Balance=Balance-%s WHERE AccNo=%s", (amt, Account_No))
            conn.commit()
            print("✅ Withdrawal successful!")

    start()

# ------------------ BALANCE ENQUIRY ------------------
def balance_Enq():
    Account_No = int(input('Enter Your Account Number: '))
    cur.execute("SELECT Balance FROM amount_table WHERE AccNo=%s", (Account_No,))
    result = cur.fetchone()

    if result:
        print(f"\n💰 Current Balance for Account {Account_No}: {result[0]}\n")
    else:
        print("\n❌ Account not found!\n")

    start()

# ------------------ CUSTOMER DETAILS ------------------
def customer_Details():
    Account_No = int(input('Enter Your Account Number: '))
    cur.execute("SELECT * FROM account_table WHERE AccNo=%s", (Account_No,))
    result = cur.fetchone()

    if result:
        print(f'''
======= CUSTOMER DETAILS =======
Account No : {result[0]}
Name       : {result[1]}
DOB        : {result[2]}
Address    : {result[3]}
Contact No : {result[4]}
Opening Bal: {result[5]}
================================
''')
    else:
        print("❌ Account not found!")

    start()

# ------------------ CLOSE ACCOUNT ------------------
def close_Acc():    
    Account_No = int(input('Enter Your Account Number: '))

    # Confirm before deleting
    confirm = input("⚠️ Are you sure you want to close this account? (y/n): ")
    if confirm.lower() != 'y':
        print("❌ Account closure cancelled.")
        start()
        return

    # Delete from both tables
    cur.execute("DELETE FROM amount_table WHERE AccNo=%s", (Account_No,))
    cur.execute("DELETE FROM account_table WHERE AccNo=%s", (Account_No,))
    conn.commit()

    if cur.rowcount > 0:
        print("✅ Account successfully closed!")
    else:
        print("❌ Invalid account number.")

    start()

# ------------------ START APP ------------------
start()
