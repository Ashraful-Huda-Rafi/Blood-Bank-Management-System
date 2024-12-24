def update_donor_info(blood_bank_data, donor_id, name, blood_group):
    if donor_id.isnumeric() and donor_id in blood_bank_data:
        if name and blood_group:
            blood_bank_data[donor_id]["Name"] = name
            blood_bank_data[donor_id]["Blood Group"] = blood_group
            print("Donor information updated successfully")
        else:
            print("Name and Blood Group cannot be empty.")
            print("Donor information not updated")
    else:
        print("Invalid donor ID or donor ID not found.")
        print("Donor information not updated")