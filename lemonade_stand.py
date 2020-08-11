import math
import os
import random
import time

import greetings
import save_games
import weather as w

def show_rules():
    rules_option  = input("would you like to learn the rules? ").lower().strip()
    if rules_option == "yes":
        print(f"make as much money as you can, don't go negative")
    time.sleep(2)
    os.system('cls')

def get_quantity(prompt, snark):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity < 0:
                print(snark)
            else:
                break   
        except ValueError:
            print(f"Try a number!")
    return quantity

def make_lemonade(cost, bank):
    while True:
        glasses = get_quantity(
            "How many glasses of lemonade would you like to make? ",
            "Remember to sell lemonade, not buy it!"
        )

        advertisements = get_quantity(
            "How many signs would you like to make? ",
            "Remember to promote your stand!"
        )
        total = (glasses*cost["glass"]) + (advertisements*cost["advertisement"])
        if total>bank:
            print(f"you are paying more than you have!")
        else:
            return (glasses, advertisements, total)

def sell_lemonade(glasses, advertisements, price, weather_factor):
    p9 = 10
    s2 = 30
    c9 = 0.5
    c2 = 1 
    if price >= p9:
        n1 = p9**2 * s2 / price**2
    else:
        n1 = (p9 - price) / p9 * 0.8 * s2 + s2

    capitalw = -advertisements * c9
    ad_bonus = 1 - (math.exp(capitalw) * c2)
    n2 = math.floor(weather_factor * n1 * (1 + ad_bonus))
    
    glasses_sold = min(n2, glasses)
    return glasses_sold

if __name__ == '__main__':
    cost = {
        "glass": 2,
        "advertisement": 15
    }
    bank = 200
    day = 0

    name = greetings.greet()
    load = input("Would you like to load a saved game? ").lower().strip()
    if load == "yes":
        (bank, cost, day) = save_games.load_game(name)
        print(f"After day {day}, you have {bank} cents in your bank!")
        
    show_rules()

    while True:
        day += 1
        (weather, weather_factor) = w.make_weather(day)
        print(f"-------Day {day}-------")
        print(f"The weather for today is {weather}!")
        (glasses, advertisements, total_cost) = make_lemonade(cost, bank)
            
        price = get_quantity(
            "How much would you like to sell lemonade for? (in cents) ",
            "Ah yes free lemonade!"
        )
        
        glasses_sold = sell_lemonade(glasses, advertisements, price, weather_factor)
        
        (random_event, glasses_sold) = w.random_events(weather, glasses_sold, glasses)

        glasses_cost = glasses*cost['glass']
        advertisements_cost = advertisements*cost['advertisement']
        revenue = glasses_sold*price

        bank += revenue - total_cost
        print(f"{random_event}")
        print(f"\n You made {advertisements} advertisements, costing {advertisements_cost}!")
        print(f"\n You made {glasses} glasses!, costing {glasses_cost}!")
        print(f"\n You sold {glasses_sold} glasses of lemonade!, earning {revenue} cents!")
        print(f"\n You spent {total_cost} cents!")
        print(f"\n Your profit is {revenue - total_cost} cents!")
        print(f"\n Your new bank total is {bank}!")

        if bank < cost["glass"]:
            print(f"You ended the game with {bank} cents!")
            break

        keep_playing = input(f"\n Would you like to continue the game? (yes or no) ").lower().strip()
        if keep_playing == "no":
            save = input(f"\n Would you like to save your game? (yes or no) ").lower().strip()
            if save == "yes":
                save_games.save_game(bank, cost, day, name)
            break
        
        os.system('cls')

