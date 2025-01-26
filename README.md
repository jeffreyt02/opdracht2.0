# opdracht2.0
 

# Fietsverhuur App
Dit project is een dashboard voor een fietsverhuurservice, waarmee verschillende gebruikers (service, eigenaar, fietsenmaker) kunnen inloggen en specifieke functionaliteiten kunnen gebruiken.

## Functionaliteiten

- **Service Dashboard**: Beheer van verhuurde fietsen, nieuwe afspraken maken, en filteren van afspraken.
- **Eigenaar Dashboard**: Weergave van statistieken zoals het aantal verhuurde fietsen en de totale omzet per maand.
- **Fietsenmaker Dashboard**: Overzicht van alle verhuurde fietsen en hun details.

## Vereisten
- Python 3.x
- Tkinter
- Pandas
- Matplotlib
- Tkcalendar
- OS
- csv
  
## Installatie

1. Clone de repository:

   ```
   git clone <repository-url>
   ```

2. Navigeer naar de projectdirectory:


1. **Clone de repository**:
    cd opdracht2.0

2. **Installeer de vereiste pakketten**:
        pip install -r requirements.txt
  

1. **Start de applicatie**:
    python main.py


2. **Log in met de volgende gebruikersnamen**:
    - Service: `service` wachtwoord:password
    - Eigenaar: `eigenaar `wachtwoord:password
    - Fietsenmaker: `fietsenmaker` wachtwoord:password

## Projectstructuur
    plaintext
fietsverhuur-app/
│
├── gegevens/
│   ├── verhuurde_fietsen.csv
│   └── andere_bestanden.csv
│
├── .venv/
│   └── (virtuele omgeving bestanden)
│
├── main.py
├── servicedesk.py
├── eigenaar_dasboard.py
├── fietsen_maker.py
├── README.md
└── requirements.txt
