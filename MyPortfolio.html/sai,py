import webbrowser

schemes = {
    "Health": [
        ("Ayushman Bharat Scheme", "https://pmjay.gov.in/"),
        ("National Health Mission", "https://nhm.gov.in/"),
        ("Covid Vaccination Portal", "https://cowin.gov.in/")
    ],
    "Education": [
        ("National Scholarship Portal", "https://Scholarships.gov.in"),
        ("AICTE Scholarship Schemes", "https://www.aicte-india.org/schemes/students-development-schemes"),
        ("PM eVidya Online Learning", "https://www.pmevidya.education.gov.in/")
    ],
    "Finance": [
        ("PM Jan Yojana", "https://pmjdy.gov.in/"),
        ("PM Mudra Loan", "https://www.mudra.gov.in/"),
        ("Digital India Portal", "https://www.digitalindia.gov.in/")
    ],
    "Agriculture": [
        ("PM Kisan Scheme", "https://pmkisan.gov.in/"),
        ("PM Fasal Bima Yojana", "https://pmfby.gov.in/"),
        ("Soil Health Card", "https://soilhealth.dac.gov.in/")
    ],
    "Women & Child": [
        ("Beti Bachao Beti Padhao", "https://wcd.nic.in/bbp-scheme/"),
        ("PM Matru Vandana Yojana", "https://pmmvy.nic.in/"),
        ("One Stop Women Support", "https://wcd.nic.in/")
    ],
    "Disabled": [
        ("Unique Disability ID (UDID) Scheme", "https://swavlambancard.gov.in/"),
        ("ADIP Scheme", "https://depwd.gov.in/"),
        ("APDASCAC Scheme", "https://apdasac.ap.gov.in/")
    ],
    "Senior Citizens": [
        ("Pradhan Mantri Vaya Vandana Yojana", "https://web.umang.gov.in/"),
        ("Rashtriya Vayoshri Yojana", "https://scw.dosje.gov.in/"),
        ("Atal Pension Yojana", "https://jansuraksha.gov.in/")
    ]
}

def browser(url):
    print("Opening Browser!!!!")
    try:
        webbrowser.open_new_tab(url)
    except:
        print("Copy link manually:", url)

def menu():
    print("\nAvailable Categories:")
    for index, category in enumerate(schemes.keys(), start=1):
        print(f"{index}. {category}")

def run_system():
    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Exiting system...")
                break
            category = list(schemes.keys())[choice-1]
            
            print(f"\nAvailable Policies in {category}:")
            for i, (name, _) in enumerate(schemes[category], start=1):
                print(f"{i}. {name}")
            
            policy_choice = int(input("Enter the policy number to open: "))
            if 1 <= policy_choice <= len(schemes[category]):
                url = schemes[category][policy_choice-1][1]
                browser(url)
            else:
                print("Invalid policy choice! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid number.")

# Run the system
run_system()


