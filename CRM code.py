import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class Customer:
    """Customer class to represent customer data"""
    def __init__(self, customer_id: str, name: str, age: int, mobile: str):
        self.id = customer_id
        self.name = name
        self.age = age
        self.mobile = mobile
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'mobile': self.mobile,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Customer':
        customer = cls(data['id'], data['name'], data['age'], data['mobile'])
        customer.created_at = data.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return customer

class CRMSystem:
    """Customer Relationship Management System"""
    
    def __init__(self, data_file: str = "customers.json"):
        self.data_file = data_file
        self.customers: Dict[str, Customer] = {}
        self.load_data()
    
    def load_data(self) -> None:
        """Load customer data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for customer_data in data:
                        customer = Customer.from_dict(customer_data)
                        self.customers[customer.id] = customer
                print(f"Loaded {len(self.customers)} customers from file.")
            except Exception as e:
                print(f"Error loading data: {e}")
    
    def save_data(self) -> None:
        """Save customer data to file"""
        try:
            data = [customer.to_dict() for customer in self.customers.values()]
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_customer(self, customer_id: str, name: str, age: int, mobile: str) -> bool:
        """Add a new customer"""
        if customer_id in self.customers:
            print("❌ Error: Customer ID already exists!")
            return False
        
        if not self._validate_input(customer_id, name, age, mobile):
            return False
        
        try:
            customer = Customer(customer_id, name, age, mobile)
            self.customers[customer_id] = customer
            print("✅ Customer added successfully!")
            return True
        except Exception as e:
            print(f"❌ Error adding customer: {e}")
            return False
    
    def search_customer(self, customer_id: str) -> Optional[Customer]:
        """Search for a customer by ID"""
        if customer_id in self.customers:
            return self.customers[customer_id]
        return None
    
    def delete_customer(self, customer_id: str) -> bool:
        """Delete a customer by ID"""
        if customer_id not in self.customers:
            print("❌ Error: Customer not found!")
            return False
        
        try:
            del self.customers[customer_id]
            print("✅ Customer deleted successfully!")
            return True
        except Exception as e:
            print(f"❌ Error deleting customer: {e}")
            return False
    
    def modify_customer(self, customer_id: str, name: str, age: int, mobile: str) -> bool:
        """Modify an existing customer"""
        if customer_id not in self.customers:
            print("❌ Error: Customer not found!")
            return False
        
        if not self._validate_input(customer_id, name, age, mobile):
            return False
        
        try:
            customer = self.customers[customer_id]
            customer.name = name
            customer.age = age
            customer.mobile = mobile
            print("✅ Customer modified successfully!")
            return True
        except Exception as e:
            print(f"❌ Error modifying customer: {e}")
            return False
    
    def display_customer(self, customer: Customer) -> None:
        """Display customer information"""
        print("\n" + "="*50)
        print(f"Customer ID: {customer.id}")
        print(f"Name: {customer.name}")
        print(f"Age: {customer.age}")
        print(f"Mobile: {customer.mobile}")
        print(f"Created: {customer.created_at}")
        print("="*50)
    
    def display_all_customers(self) -> None:
        """Display all customers"""
        if not self.customers:
            print("📭 No customers found!")
            return
        
        print(f"\n📋 Total Customers: {len(self.customers)}")
        print("="*60)
        for customer in self.customers.values():
            self.display_customer(customer)
    
    def _validate_input(self, customer_id: str, name: str, age: int, mobile: str) -> bool:
        """Validate input data"""
        if not customer_id.strip():
            print("❌ Error: Customer ID cannot be empty!")
            return False
        
        if not name.strip():
            print("❌ Error: Name cannot be empty!")
            return False
        
        if not isinstance(age, int) or age < 0 or age > 150:
            print("❌ Error: Age must be a valid number between 0 and 150!")
            return False
        
        if not mobile.strip() or len(mobile) < 10:
            print("❌ Error: Mobile number must be at least 10 digits!")
            return False
        
        return True
    
    def get_unique_id(self) -> str:
        """Get a unique customer ID from user input"""
        while True:
            customer_id = input("Enter Customer ID: ").strip()
            if not customer_id:
                print("❌ Customer ID cannot be empty!")
                continue
            if customer_id in self.customers:
                print("❌ Warning: Customer ID already exists!")
                continue
            return customer_id

def display_menu() -> None:
    """Display the main menu"""
    print("\n" + "="*60)
    print("🏢 Aryan's Customer Management System")
    print("="*60)
    print("1. ➕ Add Customer")
    print("2. 🔍 Search Customer")
    print("3. 🗑️  Delete Customer")
    print("4. ✏️  Modify Customer")
    print("5. 📋 Display All Customers")
    print("6. 💾 Save Data")
    print("7. 🚪 Exit")
    print("="*60)

def get_customer_input() -> tuple:
    """Get customer input from user"""
    name = input("Enter Customer Name: ").strip()
    
    while True:
        try:
            age = int(input("Enter Customer Age: "))
            break
        except ValueError:
            print("❌ Please enter a valid number for age!")
    
    mobile = input("Enter Customer Mobile: ").strip()
    
    return name, age, mobile

def main():
    """Main function to run the CRM system"""
    crm = CRMSystem()
    
    print("🎉 Welcome to Aryan's Customer Management System!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":  # Add Customer
            print("\n➕ ADD CUSTOMER")
            print("-" * 30)
            customer_id = crm.get_unique_id()
            name, age, mobile = get_customer_input()
            crm.add_customer(customer_id, name, age, mobile)
        
        elif choice == "2":  # Search Customer
            print("\n🔍 SEARCH CUSTOMER")
            print("-" * 30)
            customer_id = input("Enter Customer ID to search: ").strip()
            customer = crm.search_customer(customer_id)
            if customer:
                crm.display_customer(customer)
            else:
                print("❌ Customer not found!")
        
        elif choice == "3":  # Delete Customer
            print("\n🗑️ DELETE CUSTOMER")
            print("-" * 30)
            customer_id = input("Enter Customer ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete customer {customer_id}? (y/n): ").lower()
            if confirm == 'y':
                crm.delete_customer(customer_id)
            else:
                print("❌ Deletion cancelled.")
        
        elif choice == "4":  # Modify Customer
            print("\n✏️ MODIFY CUSTOMER")
            print("-" * 30)
            customer_id = input("Enter Customer ID to modify: ").strip()
            if customer_id in crm.customers:
                print("Enter new details:")
                name, age, mobile = get_customer_input()
                crm.modify_customer(customer_id, name, age, mobile)
            else:
                print("❌ Customer not found!")
        
        elif choice == "5":  # Display All Customers
            print("\n📋 ALL CUSTOMERS")
            print("-" * 30)
            crm.display_all_customers()
        
        elif choice == "6":  # Save Data
            print("\n💾 SAVING DATA")
            print("-" * 30)
            crm.save_data()
        
        elif choice == "7":  # Exit
            print("\n💾 Saving data before exit...")
            crm.save_data()
            print("👋 Thank you for using Aryan's CRM System!")
            print("Goodbye! 🚀")
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
