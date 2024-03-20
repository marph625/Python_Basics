# Lv 3 Project Tip Calculator

# TODO 0. Erstellen Sie für die folgende Projektaufgabe einen PAP.
# TODO 0. Schreiben Sie den Code zusätzlich auch als Pseudocode nieder.

# TODO 1. Erstellen Sie eine Begrüßung für Ihr Programm.

# TODO 2. Fragen Sie den Benutzenden wie hoch die komplette Rechnung ist.

# TODO 3. Fragen Sie den Benutzenden wie viel Trinkgeld (in %) gegeben werden soll.

# TODO 4. Fragen Sie anschließend auf wie viele Personen die Rechnung aufgeteilt werden soll.

# TODO 5. Das Programm soll nun den zu zahlenden Betrag für jede einzelne Person inklusive des Trinkgeldes berechnen.

# Beispiel
# Wenn die Rechnung beispielsweise einen Betrag von 150€ hatte, diese auf 5 
# Personen aufgeteilt werden soll und dabei ein Trinkgeld von 10 % gegeben wird,
# dann sollte jede Person (150.00 / 5) * 1,1 zahlen

# Runden Sie das Ergebnis auf zwei dezimale Kommastellen

# Input

print("Hello. Welcome to my tip calculation program.\nEnter your bill in € and tip in %")
raw_bill = int(input("How much is your bill?\n"))
tip_percent = int(input("How much is the tip?\n"))
participants = int(input("How many people were eating?\n"))

# Calculation

def tip_calculator(raw_bill, tip_percent, participants):
    return (raw_bill / participants) * tip_percent / 100

# Output

print("Bill:", raw_bill, "€","\nTip:", tip_percent, "%","\nParticipants:", participants)
print("The total price for every participant is:", raw_bill / participants + round(tip_calculator(raw_bill, tip_percent, participants), 2), "€")