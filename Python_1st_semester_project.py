from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QColor
from datetime import datetime
import sys
import json
import os

# ═══════════════════════════════════════
# SHARED DATA
# ═══════════════════════════════════════
CORRECT_PIN = "914"
inventory = {}
sale_history = []

# ═══════════════════════════════════════
# DATA SAVE & LOAD
# ═══════════════════════════════════════
import sys
import os

if getattr(sys, 'frozen', False):
    # exe se chal raha hai
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # PyCharm se chal raha hai
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "data.json")


# ═══════════════════════════════════════
# NAME VALIDATION HELPER
# ═══════════════════════════════════════
def is_valid_name(text):
    """
    Returns True agar name mein at least ek letter ho.
    Pure numbers (123, 456) reject hote hain.
    Mixed (Ali123, Product2) allow hote hain.
    """
    return any(c.isalpha() for c in text)


def save_data():
    data = {
        "inventory": inventory,
        "sale_history": sale_history
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


def load_data():
    global inventory, sale_history
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            inventory.update(data.get("inventory", {}))
            sale_history.extend(data.get("sale_history", []))


class ProfitLossWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("profit.ui", self)
        self.calculate()
        self.back.clicked.connect(self.close)

    def calculate(self):
        total_sales = 0
        total_cost = 0
        best_product = "-"
        best_qty = 0

        # Sale history se calculate karo
        for sale in sale_history:
            product = sale["product"]
            qty = sale["quantity"]
            total_sales += sale["total"]

            # Cost calculate karo
            if product in inventory:
                buying_price = inventory[product].get("buying_price", 0)
                total_cost += buying_price * qty

            # Best selling product
            if qty > best_qty:
                best_qty = qty
                best_product = product

        # Profit ya Loss
        profit = total_sales - total_cost
        loss = 0
        if profit < 0:
            loss = abs(profit)
            profit = 0

        # Profit percentage
        if total_sales > 0:
            profit_percent = (profit / total_sales) * 100
        else:
            profit_percent = 0

        # Labels update karo
        self.totalsaleslabel.setText(f"Total Sales: Rs.{total_sales}")
        self.totalcostlabel.setText(f"Total Cost: Rs.{total_cost}")
        self.profitlabel.setText(f"Total Profit: Rs.{profit}")
        self.totallosslabel.setText(f"Total Loss: Rs.{loss}")
        self.bestsellinglabel.setText(f"🏆 Best Selling Product: {best_product}")
        self.Totalprofitlabel.setText(f"📊 Profit %: {profit_percent:.1f}%")


# ═══════════════════════════════════════
# HISTORY WINDOW
# ═══════════════════════════════════════
class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("history.ui", self)
        self.load_table()
        self.backBtn.clicked.connect(self.close)

    def load_table(self):
        self.historytable.setRowCount(0)
        self.historytable.setColumnCount(6)
        self.historytable.setHorizontalHeaderLabels([
            "#", "Customer", "Product", "Qty", "Total (Rs)", "Date & Time"
        ])
        self.historytable.verticalHeader().setVisible(False)
        self.historytable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.historytable.horizontalHeader().setStretchLastSection(True)

        for row, sale in enumerate(sale_history):
            self.historytable.insertRow(row)
            self.historytable.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.historytable.setItem(row, 1, QTableWidgetItem(sale["customer"]))
            self.historytable.setItem(row, 2, QTableWidgetItem(sale["product"]))
            self.historytable.setItem(row, 3, QTableWidgetItem(str(sale["quantity"])))
            self.historytable.setItem(row, 4, QTableWidgetItem(str(sale["total"])))
            self.historytable.setItem(row, 5, QTableWidgetItem(sale["datetime"]))

        if len(sale_history) == 0:
            self.historytable.insertRow(0)
            self.historytable.setItem(0, 1, QTableWidgetItem("Koi sale nahi hui abhi tak!"))


# ═══════════════════════════════════════
# LOW STOCK WINDOW
# ═══════════════════════════════════════
class LowStockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lowstock.ui", self)
        self.load_table()
        self.backBtn.clicked.connect(self.close)

    def load_table(self):
        self.lowstocktable.setRowCount(0)
        self.lowstocktable.setColumnCount(4)
        self.lowstocktable.setHorizontalHeaderLabels(["#", "Product Name", "Quantity", "Status"])
        self.lowstocktable.verticalHeader().setVisible(False) #rowno.hide
        self.lowstocktable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.lowstocktable.horizontalHeader().setStretchLastSection(True)

        row = 0
        for name, details in inventory.items():
            if details["quantity"] <= 5:
                self.lowstocktable.insertRow(row)
                self.lowstocktable.setItem(row, 0, QTableWidgetItem(str(row + 1)))
                self.lowstocktable.setItem(row, 1, QTableWidgetItem(name))
                self.lowstocktable.setItem(row, 2, QTableWidgetItem(str(details["quantity"])))
                self.lowstocktable.setItem(row, 3, QTableWidgetItem("⚠️ Low Stock!"))
                for col in range(4):
                    self.lowstocktable.item(row, col).setBackground(QColor("#ffcdd2"))
                    self.lowstocktable.item(row, col).setForeground(QColor("#b71c1c"))
                row += 1

        if row == 0:
            self.lowstocktable.insertRow(0) #index 0 and 1 yani row 1 coloumn 2
            self.lowstocktable.setItem(0, 1, QTableWidgetItem("✅ Sab products ka stock theek hai!"))


# ═══════════════════════════════════════
# SELL PRODUCT WINDOW
# ═══════════════════════════════════════
class SellProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("sell.ui", self)
        self.sellBtn.clicked.connect(self.sell_product)
        self.backBtn.clicked.connect(self.close)
        self.quantityinput.textChanged.connect(self.calculate_total)
        self.nameinput.textChanged.connect(self.calculate_total)

    def calculate_total(self):
        name = self.nameinput.text().strip().lower()
        quantity = self.quantityinput.text().strip()
        if name in inventory and quantity.isdigit():
            total = int(quantity) * inventory[name]["price"]
            self.totallabel.setText(f"Rs.{total}")
        else:
            self.totallabel.setText("Rs.0")

    def sell_product(self):
        name = self.nameinput.text().strip().lower()
        customer = self.inputnamecustomer.text().strip()
        quantity = self.quantityinput.text().strip()

        if name == "" or customer == "" or quantity == "":
            QMessageBox.warning(self, "Error", "Sab fields bharein!")
            return
        if not is_valid_name(name):
            QMessageBox.warning(self, "Error",
                                "Product name mein sirf numbers nahi ho sakte!\nKam az kam ek letter zaroor ho.")
            return
        if not is_valid_name(customer):
            QMessageBox.warning(self, "Error",
                                "Customer name mein sirf numbers nahi ho sakte!\nKam az kam ek letter zaroor ho.")
            return
        if name not in inventory:
            QMessageBox.warning(self, "Error", f"'{name}' nahi mila!")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "Error", "Quantity sirf number!")
            return

        current_qty = inventory[name]["quantity"]
        if quantity > current_qty:
            QMessageBox.warning(self, "Error", f"Sirf {current_qty} units available!")
            return

        inventory[name]["quantity"] -= quantity
        total = quantity * inventory[name]["price"]
        now = datetime.now().strftime("%d-%m-%Y %H:%M")

        sale_history.append({
            "customer": customer,
            "product": name,
            "quantity": quantity,
            "total": total,
            "datetime": now
        })
        save_data()

        QMessageBox.information(self, "Sold!",
                                f"✅ Sale Complete!\n"
                                f"Customer: {customer}\n"
                                f"Product: {name}\n"
                                f"Qty: {quantity}\n"
                                f"Total: Rs {total}\n"
                                f"Remaining: {inventory[name]['quantity']} units")

        self.nameinput.clear()
        self.inputnamecustomer.clear()
        self.quantityinput.clear()
        self.totallabel.setText("Rs.0")


# ═══════════════════════════════════════
# UPDATE STOCK WINDOW
# ═══════════════════════════════════════
class UpdateStockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("update.ui", self)
        self.updateBtn.clicked.connect(self.update_stock)
        self.deleteBtn.clicked.connect(self.delete_product)
        self.backBtn.clicked.connect(self.close)

    def update_stock(self):
        name = self.nameinput.text().strip().lower()
        quantity = self.quantityinput.text().strip()
        price = self.priceinput.text().strip()

        if name == "":
            QMessageBox.warning(self, "Error", "Product name likho!")
            return
        if not is_valid_name(name):
            QMessageBox.warning(self, "Error",
                                "Product name mein sirf numbers nahi ho sakte!\nKam az kam ek letter zaroor ho.")
            return
        if name not in inventory:
            QMessageBox.warning(self, "Error", " product name nhi mila")
            return
        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            QMessageBox.warning(self, "Error", "price and quantity me sirf numbers likhen and sub fields barein")
            return


        inventory[name]["quantity"] = quantity
        inventory[name]["price"] = price
        save_data()
        QMessageBox.information(self, "Updated!", f"✅ '{name}' update ho gaya!\nQty: {quantity}\nPrice: Rs {price}")
        self.nameinput.clear()
        self.quantityinput.clear()
        self.priceinput.clear()

    def delete_product(self):
        name = self.nameinput.text().strip().lower()
        if name == "":
            QMessageBox.warning(self, "Error", "Product name likho!")
            return
        if not is_valid_name(name):
            QMessageBox.warning(self, "Error",
                                "Product name mein sirf numbers nahi ho sakte!\nKam az kam ek letter zaroor ho.")
            return
        if name not in inventory:
            QMessageBox.warning(self, "Error", f"'{name}' nahi mila!")
            return
        reply = QMessageBox.question(self, "Delete",
                                     f"'{name}' delete karna chahte hain?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            del inventory[name]
            save_data()
            QMessageBox.information(self, "Deleted!", f"🗑️ '{name}' delete ho gaya!")
            self.nameinput.clear()
            self.quantityinput.clear()
            self.priceinput.clear()


# ═══════════════════════════════════════
# VIEW PRODUCTS WINDOW
# ═══════════════════════════════════════
class ViewProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view.ui", self)
        self.load_table()
        self.backBtn.clicked.connect(self.close)

    def load_table(self):
        self.ProductTable.setRowCount(0)
        self.ProductTable.setColumnCount(4)
        self.ProductTable.setHorizontalHeaderLabels(["#", "Product Name", "Quantity", "Price (Rs)"])
        self.ProductTable.verticalHeader().setVisible(False)
        self.ProductTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ProductTable.horizontalHeader().setStretchLastSection(True)

        for row, (name, details) in enumerate(inventory.items()):
            self.ProductTable.insertRow(row)
            self.ProductTable.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.ProductTable.setItem(row, 1, QTableWidgetItem(name))
            self.ProductTable.setItem(row, 2, QTableWidgetItem(str(details["quantity"])))
            self.ProductTable.setItem(row, 3, QTableWidgetItem(str(details["price"])))


# ═══════════════════════════════════════
# ADD PRODUCT WINDOW
# ═══════════════════════════════════════
class AddProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("add.ui", self)
        self.addProductBtn.clicked.connect(self.add_product)
        self.backBtn.clicked.connect(self.close)

    def add_product(self):
        name = self.nameInput.text().strip().lower()
        quantity = self.quantityInput.text().strip()
        selling_price = self.sellinginput.text().strip()
        buying_price = self.buyinginput.text().strip()

        if name == "" or quantity == "" or selling_price == "" or buying_price == "":
            QMessageBox.warning(self, "Error", "Sab fields bharein!")
            return
        if not is_valid_name(name):
            QMessageBox.warning(self, "Error",
                                "Product name mein sirf numbers nahi ho sakte!\nKam az kam ek letter zaroor ho (jaise: Spray2, DAP, Product1)")
            return
        try:
            quantity = int(quantity)
            selling_price = float(selling_price)
            buying_price = float(buying_price)
        except ValueError:
            QMessageBox.warning(self, "Error", "Quantity aur Prices sirf numbers!")
            return
        if name in inventory:
            QMessageBox.warning(self, "Error", f"'{name}' pehle se exist karta hai!")
            return

        inventory[name] = {
            "quantity": quantity,
            "selling_price": selling_price,
            "buying_price": buying_price,
            "price": selling_price  # sell form ke liye
        }
        save_data()
        QMessageBox.information(self, "Success", f"✅ '{name}' add ho gaya!")
        self.nameInput.clear() #ab dobara naya enter kerne kaliye
        self.quantityInput.clear()
        self.sellinginput.clear()
        self.buyinginput.clear()


# ═══════════════════════════════════════
# MENU WINDOW
# ═══════════════════════════════════════
class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu.ui", self)
        self.addBtn.clicked.connect(self.open_add)
        self.viewbtn.clicked.connect(self.open_view)
        self.updateBtn.clicked.connect(self.open_update)
        self.sellBtn.clicked.connect(self.open_sell)
        self.lowstockBtn.clicked.connect(self.open_lowstock)
        self.salehistoryBtn.clicked.connect(self.open_history)
        self.exitBtn.clicked.connect(self.exit_app)

        self.profitBtn.clicked.connect(self.open_profit)

    def open_profit(self):
        self.profit_window = ProfitLossWindow()
        self.profit_window.show()

    def open_add(self):
        self.add_window = AddProductWindow()
        self.add_window.show()

    def open_view(self):
        self.view_window = ViewProductWindow()
        self.view_window.show()

    def open_update(self):
        self.update_window = UpdateStockWindow()
        self.update_window.show()

    def open_sell(self):
        self.sell_window = SellProductWindow()
        self.sell_window.show()

    def open_lowstock(self):
        self.lowstock_window = LowStockWindow()
        self.lowstock_window.show()

    def open_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def exit_app(self):
        reply = QMessageBox.question(self, "Exit",
                                     "Kya aap exit karna chahte hain?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()


# ═══════════════════════════════════════
# LOGIN WINDOW
# ═══════════════════════════════════════
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.pininput.setEchoMode(self.pininput.Password)
        self.loginbtw.clicked.connect(self.check_login)

    def check_login(self):
        entered_pin = self.pininput.text()
        if entered_pin == CORRECT_PIN:
            self.menu = MenuWindow()
            self.menu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "❌ Wrong PIN! Try again.")
            self.pininput.clear()


# ═══════════════════════════════════════
# APP START
# ═══════════════════════════════════════
load_data()
app = QApplication(sys.argv)
login = LoginWindow()
login.show()
sys.exit(app.exec_())
