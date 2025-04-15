BANK_CODES = {
    "055": "Eghtesad Novin Bank",
    "054": "Parsian Bank",
    "057": "Pasargad Bank",
    "021": "Post Bank Iran",
    "018": "Tejarat Bank",
    "051": "Moasese Etebari Tose-e",
    "020": "Tose-e Saderat Bank",
    "013": "Refah Bank",
    "056": "Saman Bank",
    "015": "Sepah Bank",
    "058": "Sarmayeh Bank",
    "019": "Saderat Bank",
    "011": "Sanat va Madan Bank",
    "053": "Karafarin Bank",
    "016": "Keshavarzi Bank",
    "010": "Marakazi Bank",
    "014": "Maskan Bank",
    "012": "Mellat Bank",
    "017": "Bank Melli Iran"
}

while True:
    sheba = input("IR").strip().lower()

    if len(sheba) > 24:
        print("Sheba code can not be greater than 24")
        continue

    if len(sheba) < 5:
        print("Invalid Sheba code")
        continue

    bank_id = sheba[2:5]

    bank_name = BANK_CODES.get(bank_id)
    if bank_name:
        print(bank_name)
    else:
        print("Bank was not found")