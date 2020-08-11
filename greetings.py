greetings = {
    "bread": "oh you still exist",
    "uncle pete": "oh hello there",
    "eliana": "get away from me"
}

def greet():
    try:
        name = input(f"What is your name? ").lower().strip()
        greeting = greetings.get(name,'oh nice to meet you').capitalize()
        print(f"{greeting}, {name.title()}!")
    except KeyboardInterrupt:
        print(f"you scum bag!")
    except:
        print(f"Oops something went wrong")
    else:
        return name

if __name__ == '__main__':
    greet()
