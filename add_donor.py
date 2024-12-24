def add_donor(blood_bank_data, donor_id, name, blood_group):
    if donor_id.isnumeric() and donor_id not in blood_bank_data:
        if name and blood_group:
            blood_bank_data[donor_id] = {"Name": name, "Blood Group": blood_group}
            print("Donor added successfully")
        else:
            print("Name and Blood Group cannot be empty.")
            print("Error!!! Donor not added.")
    else:
        print("Invalid donor ID or donor ID already exists.")
        print("Error!!! Donor not added.")