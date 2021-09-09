# https://www.helloworld.cc - Heft 1 - Seite 52
# Scary cave game -- Original Version CC BY-NC-SA 3.0
# Diese modifizierte Version (C) 2021 Roland Härter r.haerter@wut.de

# So funktioniert das Spiel: Alle Räume sind in den Dictionaries.
# Diese Dictionaries 'north', 'south',... enthalten Schlüssel-Wert-Paare.
# Der Schlüssel ist der aktuelle Raum, der Wert der Raum, in den ich gelange.
# Ein Wert 'None' bedeutet, das ich in dieser Richtung nirgendwo hin komme.
# Mit den 'go'-Kommandos kann ich durch die Räume laufen
north = {'R0':None, 'R1':None, 'R2':'R0', 'R3':'R1'}
south = {'R0':'R2', 'R1':'R3', 'R2':None, 'R3':None}
east =  {'R0':'R1', 'R1':None, 'R2':None, 'R3':None}
west =  {'R0':None, 'R1':'R0', 'R2':None, 'R3':None}
down =  {'R0':'R4', 'R4':None, 'R2':None, 'R3':None}

# Alle Befehlswörter des Spiels müssen in 'allowed_commands' stehen
allowed_commands = ['go north', 'go south', 'go east', 'go west', 'help', 'quit','go down']
# 'compass' bildet die Richtungs-Befehle auf die Richtungs-Dictionaries ab
compass = { 'go north': north, 'go south': south, 'go east': east, 'go west': west, 'go down': down}
# Jeder Raum hat eine Beschreibung. Die Beschreibung macht viel vom Spiel aus.
description = {
              'R0': 'You are in the kitchen. Seems to be abandonned.',
              'R1': 'You are in the living room. An old armor sits in one corner.',
              'R2': 'You are in a pantry. It is cold in here.',
              'R3': 'Hallway. Here is the exit from this house.',
              'R4': 'You are in the basement. Game ends here',
            }

def hilfe():
    print('You may use the following commands: ',end='')
    for befehl in allowed_commands:
        print('`{}` '.format(befehl),end='')
    print('')

# Hier wird Start und Ziel festgelegt
current_room = 'R0'
final_room = 'R3'
# Begrüßung
print('	*** Welcome to Ravenswood Manor ***')
hilfe()
# Ab hier folgt der Code, um im Spiel zu agieren
command = ''
# Das Spiel läuft in einer Endlos-Schleife
while( current_room is not None ):
    # Die Beschreibung des aktuellen Raums ausgeben
    print ( description[current_room] )
    # Den Spieler nach seinem nächsten Kommando fragen
    command = input('What do you want to do? ').lower()
    # Alle unbekannten Eingaben ignorieren
    while command not in allowed_commands:
        command = input('No such command. What do you want to do? ').lower()
    # alle Nicht-Richtungen müssen zuerst abgefangen werden
    if command == 'help':
        hilfe()
    elif command == 'quit':
        current_room = None # Ohne Schmuck und ohne Sicherheitsfrage
    # Gibt es einen Weg in die gefragte Richtung?
    elif compass[command][current_room] is not None:
        # Wenn es einen Weg gibt, gehe dorthin
        current_room = compass[command][current_room]
        # Wurde das Spielziel erreicht?
        if current_room == final_room:
            print ( description[current_room] )
            print('You found the final room.')
            current_room = None # Die Abbruch-Bedingung für die Endlos-Schleife setzen
    else:
        print ('There is no path in that direction. ',end='')
