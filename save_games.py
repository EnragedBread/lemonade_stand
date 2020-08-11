import os
import pickle

def load_game(name):
    file_name = f"{name}.pydata"
    here = os.path.dirname(os.path.abspath(__file__))
    save_file = os.path.join(here, file_name)
    try:
        file_object = open(save_file, 'rb')
        (bank, cost, day, _) = pickle.load(file_object)
        file_object.close()
    except Exception as e:
        print(e)
        print(f"Sorry I was unable to load the game!")

        bank = 200
        cost = {
            "glass": 2,
            "advertisement": 15
        }
        day = 0
    
    return (bank, cost, day)

def save_game(bank, cost, day, name):
    file_name = f"{name}.pydata"
    here = os.path.dirname(os.path.abspath(__file__))
    save_file = os.path.join(here, file_name)
    try:
        file_object = open(save_file, 'wb')
        pickle.dump((bank, cost, day, name), file_object)
        file_object.close()
    except Exception as e:
        print(e)
        print(f"Sorry I was unable to save the game!")
    