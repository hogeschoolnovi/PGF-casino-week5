# Week 5: Casino de Gouden Driehoek: spelersprofielen en unieke spellen

[//]: # (TODO: herschrijven)
[//]: # (Wat weg mag uit main: check_age, calculate_Age, determine_salutation, show_account)


## Inleiding
Vorige week heb je blackjack toegevoegd en werkte het casino nog met één actieve speler. Deze week ga je de spelersadministratie uitbreiden met profielen voor meerdere spelers.

## Opdracht beschrijving
Breid accountmenu van het casino uit zodat je er spelersprofielen kunt: 
- bekijken
- toevoegen
- wisselen
- verwijderen

Elke speler heeft een profiel in een dictionary met de gegevens:
- naam
- geboortedatum
- gender
- saldo
- gespeelde spellen

Al deze profielen worden opgeslagen in een `players` dictionary, als een "naam:profiel"-paar.

Naast `players` dictionary, hou je ook een `current_player` variabele bij. Deze variabelen en de vier functionaliteiten hierboven, implementeer je in `profiles.py`. De twee variabelen zijn "globale variabelen". Vergeet dus niet het `global` keyword te gebruiken in functies waar je deze variabelen wilt gebruiken.


### Initialisatie

De speler begint de applicatie door een naam in te voeren. Zo ging het voorheen ook al, maar nu verplaats je dit naar `profiles.py`. 

Als die speler al bestaat, haal je die speler uit de `players` dictionary op. Je laat ook een kort "welkom terug" bericht zien en het huidige saldo van de speler.

Als de speler nog niet bestaat, vraag je om de geboortedatum, het geslacht en het startbudget en voeg je het profiel toe aan de `players` dictionary. Laat vervolgens het welkomstbericht zien zoals je die vorige week ook gebruikte, met startbudget, vaste kosten, saldo en de conclusie of de gebruiker genoeg geld heeft meegenomen. 

Dit betekent dat je de functionaliteit van het welkomstbericht (en alle helper functies die daarbij horen) mag verplaatsen van `main.py` naar `profiles.py`. 

### Saldo

Het saldo wordt gebruikt in het spellen-submenu. Nu je dit saldo in het profiel van de actuele gebruiker gaat opslaan, moet je dit ook in het spellen-submenu aanpassen. Je kunt geen variabele, zoals `current_player`, exporteren, dus je moet twee functies maken. Eén functie die het saldo van de huidige speler teruggeeft en één functie waarmee je het saldo van de huidige speler kunt updaten.

In het spellen-menu van `main.py` moet je ervoor zorgen dat het saldo van de huidige speler na elk gespeeld spel geupdate wordt.

### Gespeelde spellen

Je gaat voor elke gebruiker bijhouden welke spellen deze heeft gespeeld en hoe vaak deze gebruiker elk spel speelt. Dit doe je in het `gespeelde_spellen` attribuut van de profiel dictionary. 

Net als bij het saldo, is het ook hier handig om een functie te maken om de gespeelde spellen op te halen en om een spel aan de gespeelde spellen toe te voegen. 

Voor het toevoegen moet je opletten dat je met een lege dictionary begint. Als je een spel toevoegt, moet je dus ook eerst die key toevoegen. Als je dit de eerste keer doet, zet je de waarde van die key op 1. Als je dit de tweede (of meer) keer doet, gebruik je `+= 1` voor die key. Als je ook de eerste keer `+=` zou gebruiken, krijg je een error.

In het spellen-menu in `main.py` moet je ervoor zorgen dat het `gespeelde_spellen` attribuut van de huidige speler na elk gespeeld spel wordt geupdate.

### Nieuw profiel

Er zijn nu twee momenten waar je een nieuw profiel kunt maken. Dat is bij de initialisatie van de applicatie, of in het account submenu. Zorg er in beide gevallen voor dat je nieuwe profiel in de `players` dict wordt opgeslagen. Zorg er ook voor dat je een leeftijdscheck uitvoert in beide gevallen. We willen immers geen problemen met de kansspelautoriteit.

### Switch profiel

Van profiel wisselen doe je door de `current_player` te veranderen naar een ander profiel uit de `player` dict. Vraag de gebruiker om een gebruikersnaam van het profiel waar deze naar wil wisselen. Als deze gebruikersnaam niet bekend is in de `player` dict, laat je de gebruiker middels een print weten dat dit profiel niet bestaat. 

### Toon profiel

Er zijn hier twee varianten van. Je kunt een enkel profiel laten zien, maar je kunt ook alle beschikbare profielen laten zien. De eerste optie wordt standaard getoond wanneer de gebruiker het account submenu opent. De tweede wordt pas getoond wanneer de gebruiker de "toon alle profielen" optie kiest in het submenu.

Voor het tonen van een enkel profiel, gebruik je de `current_player`. Laat in ieder geval de naam, saldo en de gespeelde spellen zien in een goed vormgegeven printout. Laat optioneel ook de namen van alle andere spelers zien.

Voor het tonen van alle profielen, laat je alleen de naam en het saldo zien van de profielen. Gebruik een for-loop om door de items van de `players` dictionary te loopen.

### Verwijder profiel

Voor het verwijderen van een profiel gebruik je het `del` keyword om het juiste profiel uit de `players` dictionary te verwijderen. Vraag aan de gebruiker welk profiel verwijderd moet worden.

**Let op:** als er maar één profiel in de `players` dictionary staat, kan die niet verwijderd worden.  
**Let ook op:** als de speler het huidige profiel wil verwijderen, moet je zorgen dat je een ander profiel als huidig profiel neerzet. Anders is er geen huidig profiel meer en zal je applicatie crashen wanneer je het account menu opent (bijvoorbeeld het eerste profiel in de `players` dict). 

### Standaard gebruikers
Zorg dat er bij het opstarten van de applicatie al 3 of 4 "voor-geïnitialiseerde" profielen in de `players` dict staan, waarmee je alvast kunt inloggen.


## Output
Je kunt de output bijvoorbeeld zo opbouwen:

```text
Casino de Gouden Driehoek - account
----------------------------------
Huidige speler: Nora
Saldo: € 50.00
Favoriete spel: blackjack

Unieke spellen deze sessie: ['blackjack', 'fruitmachine', 'roulette']
Beschikbare spelers: ['Nora', 'Milan', 'Sofie']
```

## Randvoorwaarden
- Je gebruikt minimaal 2 dictionaries.
- Je gebruikt minimaal 1 keer `get()` of de blokhaken notatie.
- Je gebruikt minimaal 1 keer `update()` of de blokhaken notatie.
- Je gebruikt minimaal 1 keer `keys()`, `values()` en/of `items()`.
- Je controleert minimaal 1 keer met `in` of een speler of spel al bestaat.
- Je hoofdmenu heeft een submenu voor het toevoegen, wisselen, tonen of verwijderen van een profiel.
- Je zet alle functies die met de profiel functionaliteit te maken hebben, in een apart bestand `profiles.py`.
- Je gebruik het `global` keyword.

## Stappenplan

1. Breid de "account" optie in het hoofdmenu uit met een submenu. Schrijf een `show_account_menu()` functie die de opties (Toon alle accounts, Nieuw account, Wissel account, Verwijder account) laat zien. Gebruik `input` om de gebruiker om diens keuze te vragen en maak een if/else of match statement om de juiste functie aan te roepen op basis van de input. Je mag alvast een functie-naam bedenken (en die later maken), maar je mag voor nu ook `pass` gebruiken.
2. De functies gaan we maken in `profiles.py`. Maak dat bestand aan. Zet bovenaan de `players` (dit mag je als een lege dict initialiseren) en `current_player` (dit mag je als None initialiseren).
3. Voordat we de nieuwe functies maken, laten we eerst de oude functies uit `main` halen. Verplaats `determine_salutation`, `calculate_Age` en `check_age` naar `profiles.py`. Hierbij heb je ook de `MIN_AGE` constante nodig, verplaats die dus ook.
4. De laatste functie die naar `profiles.py` verplaatst moet worden is `show_welcome_message`. Je gaat deze functie echter `initialize_player(total_cost)` noemen, want we gaan er ook de initialisatie logica in zetten door daar de `create_account(total_cost, name=None)` functie aan te roepen. 
5. De `initialize_player(total_cost)` functie ontvangt de `TOTAL_COST` constante als argument, omdat we die in `main.py` definiëren en we die niet opnieuw in `profiles.py` willen zetten. Nu wordt de profiel initialisatie nog gedaan in de `main` functie, maar al die variabelen (`name`, `birthdate`, `gender`, `startbudget`, `salutation` en `balance`) zet je nu in de `create_account` functie. De `initialize_player` functie ziet er als volgt uit:
    ```python
    def initialize_player(total_cost): 
        global players
        global current_player
    
        players = create_start_players() # Deze functie is bonus
        name = input("Wat is je naam? ").capitalize() # Vraag eerst de naam
        current_player = name # De current_player variabele is globaal en staat dus boven aan profiles.py. Deze bevat als waarde altijd de naam van de huidige speler.
    
        if name in players:
            profile = players[current_player]
            salutation = determine_salutation(current_player, profile["gender"])
            balance = profile["saldo"]
            # print de naam van het casino, welkom terug (met salutation) en het huidige saldo. Dit lijkt op de print uit "show_welcome_message", maar zonder "start_budget" en "vaste_kosten"
        else:
            create_account(total_cost, name) # deze functie wordt verderop besproken en zet een nieuw account in de `players` dict
    
            profile = players[current_player] # haal het huidige profiel uit de `players` dict
            balance = profile["saldo"] # haal het saldo uit het huidige profiel
            start_balance = balance + total_cost  # Het startbudget wordt opnieuw berekend omdat create_account alleen het saldo na de vaste kosten opslaat. Total_cost is een parameter van deze functie
            salutation = determine_salutation(current_player, profile["gender"])
            # Hier komt de inhoud van "show_welcome_message" uit week 4
    ```
6. De `create_account(total_cost, name=None)` functie ontvangt dezelfde `total_cost` als `initialize_player`, maar ook een optionele `name` parameter, zodat we een profiel kunnen maken met een reeds bestaande naam of door de naam via `input` op te vragen. De reden is dat je deze functie op 2 plekken wilt gebruiken. Tijdens de initialisatie en voor het maken van een nieuw account via het account menu. In het eerste geval heb je een naam, maar in het tweede geval moet je die naam nog vragen aan de gebruiker. Dit doe je als volgt: 
    ```python
    if name is None: # De default waarde van de name parameter is None. In "initialize+_player" wordt de naam meegegeven als parameter. Daarom wordt deze logica dan niet uitgevoerd. Voor het aanmaken van een nieuwe gebruiker via het menu, wordt deze logica wel uitgevoerd.
        name = input("Naam voor het nieuwe account: ").capitalize()
        if name in players: # elke gebruikersnaam moet uniek zijn. In `initialize_players` hebben we al gecontroleerd of de naam al bestaat. Voor de "menu optie"-route hebben we dat nog niet.
            print("Dit account bestaat al. Gebruik wissel account om het te openen.")
            return
    ```
7. Wanneer je de `name` hebt afgehandeld in `create_account`, ga je verder door de `birthdate`, `gender` en `start_balance` te vragen aan de gebruiker en bereken je de `balance` (start_balance - total_cost).
8. Als laatste moet je er voor zorgen dat er een profiel gemaakt wordt en dat deze in `players` gezet wordt. Zorg ook dat `current_player` de naam van het zojuist gemaakte account bevat. Een profiel kun je het makkelijkst in een `create_profile(name, birthdate, gender, balance)` functie maken, maar je kunt ook een dict maken. Zo'n profiel dict ziet er als volgt uit:
    ```python
    {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {},
    }
    ```
9. De profiel dict zet je in de `players` dict onder de key `name`, dus `players[name] = ...`. Vergeet ook niet om `name` in `current_player` te zetten.
10. Nu heb je de initialisatie en het maken van een nieuw account al geïmplementeerd. Je mag in `main.py` dan ook vast de aanroep `create_account(TOTAL_COST)` invullen in het account submenu bij de optie voor het maken van een nieuw account. Merk op dat je dit zonder een "name" argument doet, dus daar wordt dan de default `None` voor gebruikt.
11. Wanneer de gebruiker het account submenu opent, moet deze direct al diens account gegevens te zien krijgen. Dit implementeer je in de `show_account` functie.
12. In `show_account` haal je als eerst het huidige account uit de players dict. Vervolgens laat je de naam, saldo en gespeelde spellen zien, maar ook de andere beschikbare spelers. Dit laatste doe je met behulp van `list(players.keys())`
13. Het account submenu heeft ook een optie om alle gebruikers te laten zien. Dit implementeer je in de `show_all_players` functie. Dit kun je doen door met een for-loop door de players dict te loopen en dan de naam en het saldo van elk profiel te printen. Doe dat wel in een mooie format, zoals "- Henk: saldo € 123,00".
14. Het wisselen van een account doe je in de `switch_account` functie. Vraag als eerst aan de gebruiker naar welke account-naam deze wil wisselen. Gebruik daar `input` voor. Check vervolgens of die gebruiker al bestaat in `players`. Als dat zo is, dan zet je `current_player` op die naam. Als de naam niet bestaat, print je dat het account niet bestaat en sluit je de functie af met return.
15. De laatste functionaliteit uit het account submenu is het verwijderen van een account. Dit implementeer je in de `remove_account` functie. 
    - Vraag als eerst welk account de gebruiker wil verwijderen.
    - Check of dit account bestaat in de `players` dict. Als dat niet zo is, print je dit in een berichtje en sluit je de functie af met `return`.
    - Als het account wel bestaat, check je als eerst of dit niet het laatste account is (len == 1). Als dat namelijk zo is, dan print je dat het laatste account niet verwijderd mag worden en sluit je de functie af met `return`.
    - Als dit niet het laatste account is, dan verwijder je dit account uit de `players` dict met het `del` keyword.
    - Check als laatst nog wel even of het account dat je zojuist verwijderd hebt niet toevallig het `current_player` account was. Als dat zo is, dan moet je zorgen dat er een ander account als `current_player` wordt geselecteerd, bijvoorbeeld `list(players.keys())[0]`
16. Naast het account menu, is er ook in het spellen menu nog wat te updaten. Namelijk de balance van de huidige spellen en de gespeelde spellen van de huidige speler.
17. Voor het updaten van het saldo is het makkelijk om een `get_current_balance()` helper functie en een `update_current_balance(balance)` helper functie te maken die het "saldo" attribuut van de `current_player` in de `players` dict aanspreken.
18. Voor het registreren van een gespeeld spel, maak je de `register_played_game(game_name)` functie. Als de "game_name" al in de `gespeelde_spellen` dict van de huidige gebruiker staat, dan doe je `played_games[game_name] += 1`. Als de "game_name" nog niet in de `gespeelde_spellen` dict van de huidige gebruiker staat, dan doe je `played_games[game_name] = 1`.
19. Als laatste stap mag je een aantal voorbeeld gebruikers in de `players` dictionary zetten. Dit kun je doen door in de eerste regel van `initialize_player` de `players` variabele te initialiseren met een gevulde dictionary met 3 "naam:profiel" paren erin. Een profiel was op zich ook al een dictionary, dus je hebt dan een dictionary met dictionaries er in.


## Bonus
1. Geef elke gebruiker een wachtwoord, zodat je bij een profiel wissel en bij een initialisatie met een bestaand profiel, dat wachtwoord kunt vragen om te verifiëren dat de gebruiker ook echt die gebruiker is. Dit hoeft niet met een moeilijke cryptografische versleuteling, maar mag gewoon "plain tekst".
2. Wanneer de gebruiker diens eigen profiel (het huidige, actieve profiel) wil verwijderen, zorg er dan voor dat de gebruiker "uitgelogd" wordt, in plaats van een willekeurig ander profiel te selecteren. Start het initialisatieproces opnieuw, zodat de gebruiker kan kiezen om een reeds bestaande gebruiker te selecteren als actief profiel, of om een nieuw profiel te maken. 