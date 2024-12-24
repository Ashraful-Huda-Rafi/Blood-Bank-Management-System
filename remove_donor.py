def remove_donor(blood_bank_data, donor_id):
    if donor_id.isnumeric() and donor_id in blood_bank_data:
        del blood_bank_data[donor_id]
        print("Donor removed successfully")
    else:
        print("Invalid donor ID or donor ID not found.")
        print("Error!!! Donor not removed.")