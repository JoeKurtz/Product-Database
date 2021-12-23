'''
Joe Kurtz (Done with Stanley Cohen)
Introduction to Computer Programming
11/29/21
Assignment Ten - Part 1a and Part 1b
'''
import random
import math

valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

pokemon = dict()

f = open("pokemon.txt","r")



l = f.readline()
while(l):
    arr = l.split(":")
    l = f.readline()

    name = arr[0]
    quantity = int(arr[2][0:arr[2].find(",")].strip())
    fee = float(arr[3][0:arr[3].find(",")].strip())
    powers = arr[4][arr[4].find("[")+2:arr[4].find("]")-1].split(",")
    for i in range(len(powers)):
        powers[i] = powers[i].replace("'","").strip()
    

    pokemon[name] = {
        'quantity': quantity,
        'fee': fee,
        'powers': powers
        }


f.close()






'''
"pokemon" DICTIONARY:
(i) KEYS: Name of Pokemon (EX: "charmander")
(ii) VALUES: Dictionary (KEYS: "quantity", "fee", "powers")
'''

while True:
    print("Welcome to the Pokemon Center!")

    action = str.upper(input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: "))

    while action not in "ARESTLQ":
        print("Invalid Command, Try Again")
        print()
        action = str.upper(input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: "))

            
    if action == "Q":
        print("See you next time!")
        break

    elif action == "L":
        format_name = format("Name", "<10s")
        format_amount = format("Amount Available", ">18s")
        format_fee = format("Adoption Fee", ">15s")
        format_type = format("Type(s)",">10s")

        print(format_name, format_amount, format_fee, format_type)


        for keys in sorted(pokemon.keys()):
            format_key = format(keys,"<10s")
            format_q = format(pokemon[keys]["quantity"],">18d")
            format_f = format(pokemon[keys]["fee"],">15,.2f")
            
            print(str.capitalize(format_key), format_q, format_f, "  ", end = "")

            types = ""
            for i in range(len(pokemon[keys]["powers"])):
                types += (" " + str.capitalize(pokemon[keys]["powers"][i]))

            print(types)

        print()
    
    elif action == "S":
        search = str.lower(input("Name of Pokemon to search for: "))
        print()

        if search not in pokemon:
            print(f"Sorry, there are no {search} here!")
        else:
            pokemon_s = str.capitalize(search)
            print(f"We have {pokemon[search]['quantity']} {pokemon_s} at the Pokemon Center")
            print(f"It will cost ${pokemon[search]['fee']:,.2f} to adopt this Pokemon")

            types = ""
            for i in range(len(pokemon[search]["powers"])):
                types += (str.capitalize(pokemon[search]["powers"][i])+ " ")
            print(f"{pokemon_s} has the following types: {types}")

        print()

    elif action == "A":
        new_pokemon = input("Enter name of new pokemon: ")


        if new_pokemon in pokemon:
            print("Duplicate name, add operation cancelled")
            print()
            break

        else:
            amount = int(input("How many of these Pokemon are you adding? "))
            while amount < 1 or amount > 100:
                print("Invalid, please try again")
                print()
                amount = int(input("How many of these Pokemon are you adding? "))

            fee = float(input("What is the adoption fee for this Pokemon? "))
            while fee <= 0:
                print("Invalid, please try again")
                print()
                fee = float(input("What is the adoption fee for this Pokemon? "))
            print()
            print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type")

            type_p = []
            while True:
                types = input("What type of Pokemon is this? ")

                if str.upper(types) == "END":
                    print("Pokemon added!")
                    print()
                    break

                elif str.upper(types) == "HELP":
                    for types in valid_pokemon_types:
                        print(str.capitalize(types))
                    print()

                else:

                    if types in valid_pokemon_types:
                        print(f"Type {types} applied!")
                        type_p += [types]
                    else:
                        print("Invalid Type, Try Again!")
                        print()

                    pokemon[new_pokemon] = {
                        "quantity":amount,
                        "fee":fee,
                        "powers":type_p
                        }

                    file_object = open("pokemon.txt","r")
                    data = file_object.read()


                    lines = data.split("\n")

                    '''
                    found = False
                    for c in lines:
                        ind_lines = c.split(":")
                        if ind_lines[0] == new_pokemon:
                            found = True
                    '''

                    #if found == False:
                    file_object = open("pokemon.txt","a")
                    file_object.write("\n")
                    file_object.write(new_pokemon + ":")
                    file_object.write(str(pokemon[new_pokemon]))
                    file_object.close()
                    
                                                                
                    print()

    elif action == "R":
        remove = str.lower(input("Enter name of Pokemon to remove: "))

        if remove in pokemon:
            del pokemon[remove]

            file_object = open("pokemon.txt","w")
            file_object.write()
            file_object.write(str(pokemon))
            print("Pokemon Removed")
            print()
        else:
            print("Pokemon not found, cannot remove")
            print()

    elif action == "E":
        total = 0
        high = 0
        low = math.inf
        
        for keys in pokemon:
            total += pokemon[keys]["fee"]

            if pokemon[keys]["fee"] > high:
                high = pokemon[keys]["fee"]
                high_key = str.capitalize(keys)

            elif pokemon[keys]["fee"] < low:
                low = pokemon[keys]["fee"]
                low_key = str.capitalize(keys)

        print(f"Highest priced Pokemon: {high_key} @ ${high:,.2f} per Pokemon")
        print(f"Lowest priced Pokemon: {low_key} @ ${low:,.2f} per Pokemon")
        print(f"Total cost to adopt all Pokemon in the Center: ${total:,.2f}")
        print()

    elif action == "T":
        type_search = str.lower(input("Enter Pokemon Type: "))

        pok_found = []
        
        for k in pokemon:
            if(type_search in pokemon[k]["powers"]):

                pok_found += [k]
                
        # if any pokemon found, print headers
        if(len(pok_found) > 0):
            
            format_name = format("Name", "<10s")
            format_amount = format("Amount Available", ">18s")
            format_fee = format("Adoption Fee", ">15s")
            format_type = format("Type(s)",">10s")

            print(format_name, format_amount, format_fee, format_type)

        else:
            print("We do not have that Type Here")
            
        for k in pok_found:

            pok = pokemon[k]
            
            format_key = format(k,"<10s")
            format_q = format(pok["quantity"],">18d")
            format_f = format(pok["fee"],">15,.2f")
                        
            print(str.capitalize(format_key), format_q, format_f, "  ", end = "")

            types = ""
            for i in range(len(pok["powers"])):
                types += (" " + str.capitalize(pok["powers"][i]))

            print(types)
 

        print()


        



'''
THINGS TO DO - PER SECTION! :
"L" --> LIST


"A" --> ADD NEW POKEMON
(1) Add New Pokemon to Dictionary Dataset

"S" --> SEARCH POKEMON

"T" --> TYPE SEARCH
(1) Add in "TYPE" Search Feature
'''
            

                       
        
        
    
