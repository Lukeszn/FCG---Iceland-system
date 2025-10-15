import tkinter as tk
from tkinter import messagebox
import sqlite3


class Database:
    """Handles all SQLite operations."""
    def __init__(self):
        self.conn = sqlite3.connect("system.db")
        self.create_tables()

    def create_tables(self):
        """Create tables if they don't exist."""
        c = self.conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id TEXT,
                        name TEXT,
                        surname TEXT,
                        email TEXT,
                        phone TEXT,
                        street TEXT,
                        house_number TEXT,
                        postcode TEXT,
                        county TEXT,
                        city TEXT
                    )""")

        c.execute("""CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_id TEXT,
                        product_id TEXT,
                        customer_id TEXT,
                        quantity INTEGER,
                        price REAL,
                        number_order TEXT,
                        timeslot TEXT
                    )""")

        c.execute("""CREATE TABLE IF NOT EXISTS stock (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_id TEXT,
                        name TEXT,
                        quantity INTEGER,
                        date TEXT,
                        price REAL,
                        product_level TEXT
                    )""")

        c.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        supplier_id TEXT,
                        product_id TEXT,
                        name TEXT,
                        quantity INTEGER,
                        street TEXT,
                        house_number TEXT,
                        email TEXT,
                        postcode TEXT
                    )""")
        self.conn.commit()

    def insert(self, table, data):
        """Insert a record into a given table."""
        c = self.conn.cursor()
        placeholders = ", ".join("?" * len(data))
        c.execute(f"INSERT INTO {table} VALUES (NULL, {placeholders})", data)
        self.conn.commit()

    def fetch_all(self, table):
        """Return all records from a table."""
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {table}")
        return c.fetchall()


class App(tk.Tk):
    """Main GUI Application."""
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("450x500")
        self.db = Database()
        self.show_login()

    # ------------------- Utility -------------------
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    @staticmethod
    def create_labeled_entries(window, fields):
        entries = {}
        for field in fields:
            tk.Label(window, text=field).pack()
            entry = tk.Entry(window)
            entry.pack()
            entries[field] = entry
        return entries

    # ------------------- Login -------------------
    def show_login(self):
        self.clear_window()
        tk.Label(self, text="Login", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self, text="Username").pack()
        username_entry = tk.Entry(self)
        username_entry.pack()

        tk.Label(self, text="Password").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        tk.Button(
            self, text="Enter", width=10,
            command=lambda: self.validate_login(username_entry, password_entry)
        ).pack(pady=15)

    def validate_login(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()

        if username == "staff1" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    # ------------------- Main Menu -------------------
    def show_main_menu(self):
        self.clear_window()
        self.title("Main Menu")

        tk.Label(self, text="Main Menu", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Button(self, text="Online Orders", width=25, command=self.show_orders).pack(pady=5)
        tk.Button(self, text="Customer Information", width=25, command=self.show_customers).pack(pady=5)
        tk.Button(self, text="Stock Levels", width=25, command=self.show_stock).pack(pady=5)
        tk.Button(self, text="Supplier Information", width=25, command=self.show_suppliers).pack(pady=5)
        tk.Button(self, text="View Database Records", width=25, command=self.view_records).pack(pady=10)
        tk.Button(self, text="Logout", width=25, command=self.show_login).pack(pady=10)

    # ------------------- Orders Screen -------------------
    def show_orders(self):
        self.clear_window()
        self.title("Orders")

        tk.Label(self, text="Online Orders", font=("Arial", 16, "bold")).pack(pady=10)
        fields = ["OrderID", "ProductID", "CustomerID", "Quantity", "Price", "NumberOrder", "Timeslot"]
        entries = self.create_labeled_entries(self, fields)

        def save():
            data = [entries[f].get() for f in fields]
            self.db.insert("orders", data)
            messagebox.showinfo("Success", "Order added successfully!")
            self.show_main_menu()

        tk.Button(self, text="Add Order", width=20, command=save).pack(pady=5)
        tk.Button(self, text="Back", width=20, command=self.show_main_menu).pack(pady=5)

    # ------------------- Customer Screen -------------------
    def show_customers(self):
        self.clear_window()
        self.title("Customer Information")

        tk.Label(self, text="Customer Information", font=("Arial", 16, "bold")).pack(pady=10)
        fields = ["CustomerID", "Name", "Surname", "Email", "Phone", 
                  "Street Name", "House Number", "Post Code", "County", "City"]
        entries = self.create_labeled_entries(self, fields)

        def save():
            data = [entries[f].get() for f in fields]
            self.db.insert("customers", data)
            messagebox.showinfo("Success", "Customer added successfully!")
            self.show_main_menu()

        tk.Button(self, text="Add Customer", width=20, command=save).pack(pady=5)
        tk.Button(self, text="Back", width=20, command=self.show_main_menu).pack(pady=5)

    # ------------------- Stock Screen -------------------
    def show_stock(self):
        self.clear_window()
        self.title("Stock Levels")

        tk.Label(self, text="Stock Levels", font=("Arial", 16, "bold")).pack(pady=10)
        fields = ["ProductID", "Name", "Quantity", "Date", "Price", "Product Level"]
        entries = self.create_labeled_entries(self, fields)

        def save():
            data = [entries[f].get() for f in fields]
            self.db.insert("stock", data)
            messagebox.showinfo("Success", "Stock record added successfully!")
            self.show_main_menu()

        tk.Button(self, text="Add Stock", width=20, command=save).pack(pady=5)
        tk.Button(self, text="Back", width=20, command=self.show_main_menu).pack(pady=5)

    # ------------------- Supplier Screen -------------------
    def show_suppliers(self):
        self.clear_window()
        self.title("Supplier Information")

        tk.Label(self, text="Supplier Information", font=("Arial", 16, "bold")).pack(pady=10)
        fields = ["SupplierID", "ProductID", "Name", "Quantity", 
                  "Street Name", "House Number", "Email", "Post Code"]
        entries = self.create_labeled_entries(self, fields)

        def save():
            data = [entries[f].get() for f in fields]
            self.db.insert("suppliers", data)
            messagebox.showinfo("Success", "Supplier added successfully!")
            self.show_main_menu()

        tk.Button(self, text="Add Supplier", width=20, command=save).pack(pady=5)
        tk.Button(self, text="Back", width=20, command=self.show_main_menu).pack(pady=5)

    # ------------------- View All Records -------------------
    def view_records(self):
        self.clear_window()
        self.title("Database Viewer")

        tk.Label(self, text="View Records", font=("Arial", 16, "bold")).pack(pady=10)
        tables = ["customers", "orders", "stock", "suppliers"]

        text_area = tk.Text(self, width=60, height=20)
        text_area.pack(pady=5)

        for table in tables:
            records = self.db.fetch_all(table)
            text_area.insert(tk.END, f"--- {table.upper()} ---\n")
            for record in records:
                text_area.insert(tk.END, f"{record}\n")
            text_area.insert(tk.END, "\n")

        tk.Button(self, text="Back", width=20, command=self.show_main_menu).pack(pady=5)


# ------------------- Main Entry -------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()
