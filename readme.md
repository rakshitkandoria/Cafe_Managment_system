# ☕ Cafe Management System

Welcome to the **Cafe Management System**! This application is designed to streamline the process of ordering and managing a cafe's menu. 🛠️ Built using **Tkinter** for the GUI and **MySQL** for database management.

---

## 📋 Features

- 📝 **Interactive Menu:** Users can select items from a cafe menu with prices displayed.
- 🛍️ **Order Summary:** Displays selected items, customer name, and the total bill.
- ✅ **Order Placement:** Saves orders to the database with customer details.
- ❌ **Remove Order:** Option to cancel an order if needed.
- 🎉 **Thank You Screen:** A personalized message after placing an order.

---

## ⚙️ Installation Guide

1. **Download the Project Files**:
   - Click on the green "Code" button at the top of this repository.
   - Select "Download ZIP".
   - Extract the downloaded ZIP file.

2. **Install Python**:
   - Ensure Python 3.7 or later is installed on your system.
   - You can download Python from [python.org](https://www.python.org/).

3. **Install Required Libraries**:
   - Open a terminal or command prompt.
   - Install the required library for database connectivity:
     ```bash
     pip install pymysql
     ```

4. **Set Up MySQL Database**:
   - Open your MySQL Workbench or any MySQL client.
   - Create a database named `cafe_management`:
     ```sql
     CREATE DATABASE cafe_management;
     ```
   - Create a table named `orders`:
     ```sql
     CREATE TABLE orders (
         id INT AUTO_INCREMENT PRIMARY KEY,
         customer_name VARCHAR(255),
         items TEXT,
         total_bill FLOAT
     );
     ```
   - Update the connection settings in the script (`host`, `user`, `password`, `database`) to match your MySQL credentials.

5. **Run the Application**:
   - Double-click on the `cafe_management.py` file, or run it through your terminal using:
     ```bash
     python cafe_management.py
     ```

---

## 📜 Usage Instructions

1. Launch the application.
2. Select items from the menu and proceed to the order summary.
3. Enter the customer's name and place the order.
4. A personalized thank-you message will appear after the order is placed. Alternatively, you can remove the order if needed.

---

## 🛠️ Technologies Used

- **Python**: For application logic.
- **Tkinter**: For the graphical user interface.
- **MySQL**: For database management.

---

## 📸 Screenshots

### 🗂️ Main Menu

<img width="371" alt="image" src="https://github.com/user-attachments/assets/d48c45c9-1d2c-48e6-add0-f369fa6818d2" />


### 🛒 Order Summary

<img width="412" alt="image" src="https://github.com/user-attachments/assets/9e1bae03-22f4-4c76-b659-c655d13e457d" />

### 🎉 Thank You Screen

<img width="479" alt="image" src="https://github.com/user-attachments/assets/a3557635-2226-4d98-bdda-c676c8f71741" />

---

