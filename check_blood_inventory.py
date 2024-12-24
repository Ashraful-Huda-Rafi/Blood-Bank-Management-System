def check_blood_inventory(blood_bank_data):
    blood_inventory = {"A+": 0, "A-": 0, "B+": 0, "B-": 0, "AB+": 0, "AB-": 0, "O+": 0, "O-": 0}
    for donor_info in blood_bank_data.values():
        blood_group = donor_info["Blood Group"]
        blood_inventory[blood_group] += 1
    print("Blood Inventory:")
    for blood_group, quantity in blood_inventory.items():
        print(f"{blood_group}: {quantity} units")