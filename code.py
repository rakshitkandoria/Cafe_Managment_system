import tkinter as tk
from tkinter import messagebox
import pymysql

# Database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='passward',
    database='cafe_management'
)
cursor = connection.cursor()


def calculate_total_bill():
    total = 0
    for item in selected:
        total += items[item]
    return total

def go_to_order_summary():
    selected_items.set(", ".join(selected))  # Update selected items label
    total_bill.set(f"Total Bill: ₹{calculate_total_bill()}")  # Set total bill on the summary screen
    menu_frame.pack_forget()  # Hide menu frame
    thanks_frame.pack_forget()  # Hide thanks frame
    order_summary_frame.pack(fill="both", expand=True)  # Show order summary frame

def place_order():
    if customer_name.get() and selected:  # Check if customer name is entered and items are selected
        total = calculate_total_bill()  # Calculate total bill
        # Insert order into database
        cursor.execute('INSERT INTO orders (customer_name, items, total_bill) VALUES (%s, %s, %s)', 
                       (customer_name.get(), selected_items.get(), total))
        connection.commit()
        messagebox.showinfo("Order Placed", f"Your order has been placed!")

        # Clear selected items and customer name after placing order
        customer_name.set("")  # Clear customer name
        selected.clear()  # Clear the selected items list
        selected_items.set("")  # Clear selected items display
        update_selected_items()  # Reset displayed selected items list

        # Show thanks for ordering message with emoji on the thanks screen
        thanks_label.config(text=f"Thanks for ordering, {customer_name.get()}! 🍵\nYour total bill is ₹{total} 💸")

        # Show thanks frame
        order_summary_frame.pack_forget()  # Hide order summary frame
        thanks_frame.pack(fill="both", expand=True)  # Show thanks frame

        # Reset checkboxes (uncheck all checkboxes)
        for button in checkbuttons:
            button.deselect()

    else:
        messagebox.showerror("Error", "Please enter your name and select at least one item.")

def remove_order():
    if messagebox.askyesno("Remove Order", "Are you sure you want to remove the order?"):
        # Clear selected items and customer name when removing order
        customer_name.set("")  # Clear customer name
        selected.clear()  # Clear selected items
        selected_items.set("")  # Reset selected items display
        update_selected_items()  # Update displayed selected items list

        messagebox.showinfo("Order Removed", "Your order has been removed.")
        order_summary_frame.pack_forget()  # Hide the order summary frame
        menu_frame.pack(fill="both", expand=True)  # Show the menu frame again

def toggle_item(item):
    if item in selected:
        selected.remove(item)
    else:
        selected.append(item)

def update_selected_items():
    selected_items_display.config(text=", ".join(selected))  # Update the selected items display

# Create the main window
root = tk.Tk()
root.title("Cafe Management System")
root.geometry("800x500")
root.configure(bg="#faf3e0")

# Variables
selected_items = tk.StringVar()
customer_name = tk.StringVar()
selected = []
total_bill = tk.StringVar()

# Menu Frame (now also acts as Home Frame)
menu_frame = tk.Frame(root, bg="#faf3e0")
menu_label = tk.Label(menu_frame, text="Cafe Menu", font=("Helvetica", 32, "bold"), bg="#faf3e0", fg="#6b4226")
menu_label.pack(pady=20)

items = {"Espresso": 250, "Cappuccino": 300, "Latte": 350, "Mocha": 400, "Black Coffee": 200}

menu_items_frame = tk.Frame(menu_frame, bg="#faf3e0")
menu_items_frame.pack(pady=10)

# List to store checkbuttons
checkbuttons = []

# Display checkboxes vertically
for item, price in items.items():
    button = tk.Checkbutton(menu_items_frame, text=f"{item} - ₹{price}", font=("Helvetica", 18), bg="#fbe7c6", fg="#3e2723", activebackground="#f8efe9", selectcolor="#f8efe9", command=lambda i=item: (toggle_item(i), update_selected_items()))
    button.pack(side="top", padx=10, pady=5)  # Pack checkboxes vertically using side="top"
    checkbuttons.append(button)  # Add button to checkbuttons list

next_button = tk.Button(menu_frame, text="Proceed to Order", font=("Helvetica", 20, "bold"), bg="#6b4226", fg="white", command=go_to_order_summary)
next_button.pack(pady=20)

selected_items_display = tk.Label(menu_frame, text="", font=("Helvetica", 16), bg="#faf3e0", fg="#3e2723")
selected_items_display.pack(pady=10)

# Order Summary Frame
order_summary_frame = tk.Frame(root, bg="#faf3e0")
summary_label = tk.Label(order_summary_frame, text="Order Summary", font=("Helvetica", 32, "bold"), bg="#faf3e0", fg="#6b4226")
summary_label.pack(pady=20)

name_label = tk.Label(order_summary_frame, text="Enter Your Name:", font=("Helvetica", 20), bg="#faf3e0", fg="#3e2723")
name_label.pack(pady=10)

name_entry = tk.Entry(order_summary_frame, textvariable=customer_name, font=("Helvetica", 18))
name_entry.pack(pady=10)

items_label = tk.Label(order_summary_frame, textvariable=selected_items, font=("Helvetica", 18), bg="#faf3e0", fg="#3e2723")
items_label.pack(pady=10)

total_bill_label = tk.Label(order_summary_frame, textvariable=total_bill, font=("Helvetica", 18), bg="#faf3e0", fg="#3e2723")
total_bill_label.pack(pady=10)

place_order_button = tk.Button(order_summary_frame, text="Place Order", font=("Helvetica", 20, "bold"), bg="#4caf50", fg="white", command=place_order)
place_order_button.pack(pady=10)

remove_order_button = tk.Button(order_summary_frame, text="Remove Order", font=("Helvetica", 20, "bold"), bg="#f44336", fg="white", command=remove_order)
remove_order_button.pack(pady=10)

# Thanks Frame
thanks_frame = tk.Frame(root, bg="#faf3e0")
thanks_label = tk.Label(thanks_frame, text="", font=("Helvetica", 32, "bold"), bg="#faf3e0", fg="#4caf50")
thanks_label.pack(pady=40)

# Start with Menu Frame
menu_frame.pack(fill="both", expand=True)

root.mainloop()

# Close database connection on exit
connection.close()
