PROMPT: str = "Hey there! What do you want to hear? Type 'joke' if you're in the mood to laugh: "

JOKE: str = (
    "Here is a joke for you!\n"
    "Sophia is heading out to the grocery store.\n"
    "A programmer tells her: get a liter of milk, and if they have eggs, get 12.\n"
    "Sophia returns with 13 liters of milk.\n"
    "The programmer asks why, and Sophia replies: 'Because they had eggs.' 🤓"
)

SORRY: str = "Sorry, I only tell jokes. Try typing 'joke' next time. 😅"

def main():
    user_input = input(PROMPT).strip().lower()

    if "joke" in user_input:
        print("\n" + JOKE)
    else:
        print("\n" + SORRY)

if __name__ == "__main__":
    main()
