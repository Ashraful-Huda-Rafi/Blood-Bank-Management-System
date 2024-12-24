import csv
import os
from add_donor import add_donor
from remove_donor import remove_donor
from update_donor_info import update_donor_info
from view_all_donor import view_all_donors
from check_blood_inventory import check_blood_inventory


BLOOD_BANK_DATA_FILE = "blood_bank_data.csv"

def load_data():
    blood_bank_data = {}
    if os.path.isfile(BLOOD_BANK_DATA_FILE):
        with open(BLOOD_BANK_DATA_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                donor_id = row["Donor ID"]
                blood_bank_data[donor_id] = {
                    "Name": row["Name"],
                    "Blood Group": row["Blood Group"]
                }
    return blood_bank_data

def save_data(blood_bank_data):
    with open(BLOOD_BANK_DATA_FILE, "w", newline="") as file:
        fieldnames = ["Donor ID", "Name", "Blood Group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for donor_id, donor_info in blood_bank_data.items():
            writer.writerow({"Donor ID": donor_id, "Name": donor_info["Name"], "Blood Group": donor_info["Blood Group"]})

def main():
    blood_bank_data = load_data()
    while True:
        print("\nBlood Bank Management System")
        print("1. Add Donor")
        print("2. Remove Donor")
        print("3. Update Donor Information")
        print("4. View All Donors")
        print("5. Check Blood Inventory")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            donor_id = input("Enter Donor ID (must be unique and an integer): ")
            name = input("Enter Donor Name: ")
            blood_group = input("Enter Donor Blood Group: ")
            add_donor(blood_bank_data, donor_id, name, blood_group)
            save_data(blood_bank_data)
        elif choice == "2":
            donor_id = input("Enter Donor ID to remove: ")
            remove_donor(blood_bank_data, donor_id)
            save_data(blood_bank_data)
        elif choice == "3":
            donor_id = input("Enter Donor ID to update: ")
            name = input("Enter New Name: ")
            blood_group = input("Enter New Blood Group: ")
            update_donor_info(blood_bank_data, donor_id, name, blood_group)
            save_data(blood_bank_data)
        elif choice == "4":
            view_all_donors(blood_bank_data)
        elif choice == "5":
            check_blood_inventory(blood_bank_data)
        elif choice == "6":
            print("Exiting................................................")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()