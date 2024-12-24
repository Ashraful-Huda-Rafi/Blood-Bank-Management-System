def view_all_donors(blood_bank_data):
    print("Donor Information:")
    for donor_id, donor_info in blood_bank_data.items():
        print(f"Donor ID: {donor_id}, Name: {donor_info['Name']}, Blood Group: {donor_info['Blood Group']}")