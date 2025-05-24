import random

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "Why was the computer cold? Because it forgot to close Windows!",
        "Why don’t programmers like nature? It has too many bugs.",
        "Why did the student eat his homework? Because the teacher told him it was a piece of cake!",
        "Parallel lines have so much in common… it’s a shame they’ll never meet.",
        "I asked my computer for a joke, and it said: 404 Joke Not Found.",
        "I told my Wi-Fi it was too clingy... now I'm disconnected.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the bicycle fall over? Because it was two tired!",
        "Why did the tomato turn red? Because it saw the salad tomato and got jealous!",
        "Why did the coffee file a police report? It got mugged!",
        "Why did the picture go to jail? Because it was framed!",
        "Knock, knock. Who's there? Letter. Letter who? Let her in, I'm stuck in the envelope!",
        "Knock, knock. Who's there? Tank. Tank who? You're welcome!",
        "Why don’t eggs tell jokes? They’d crack each other up!",
        "What do you call fake spaghetti? An impasta!",
        "How does a penguin build its house? Igloos it together!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why can’t your nose be 12 inches long? Because then it would be a foot!"
    ]
    while True:
        print("\n🃏 Joke of the Moment:")
        print(random.choice(jokes))
        again = input("\nType 'change' to go back or press Enter for another joke: ").strip().lower()
        if again == 'change' or again == 'change topic':
            break

def pickup_line():
    lines = [
        "Are you a keyboard? Because you’re just my type.",
        "Do you have a map? I keep getting lost in your code.",
        "Are you Wi-Fi? Because I’m feeling a connection.",
        "Are you Python? Because you’ve got class.",
        "You're like semicolon — essential and underrated.",
        "Are you made of copper and tellurium? Because you're Cu-Te!",
        "Even if there were no gravity on Earth, I'd still fall for you.",
        "You must be a loop because you keep running through my mind.",
        "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a name, or can I call you mine?",
        "Are you a time traveler? Because I see you in my future.",
        "Are you a beaver? Because daaaaaaaam.",
        "Are you a cat? Because you are purrfect.",
        "Are you a charger? Because I’m dying without you.",
        "Are you Google? Because you have everything I’ve been searching for.",
        "If you were a fruit, you’d be a fineapple.",
        "Are you from space? Because your beauty is out of this world.",
        "Do you like coding? Because I see us compiling perfectly."
    ]
    while True:
        print("\n💘 Pickup Line for You:")
        print(random.choice(lines))
        again = input("\nType 'change' to go back or press Enter for another pickup line: ").strip().lower()
        if again == 'change' or again == 'change topic':
            break

def quiz():
    questions = {
        **{f"What is {i} + {j}? ": str(i + j) for i in range(1, 21) for j in range(1, 6)},
        **{f"What is {i} * {j}? ": str(i * j) for i in range(1, 11) for j in range(1, 2)},
        "What is the capital of France? ": "Paris",
        "What programming language is this code written in? ": "Python",
        "Which planet is known as the Red Planet? ": "Mars",
        "What does CPU stand for? ": "Central Processing Unit",
        "Who wrote 'Romeo and Juliet'? ": "Shakespeare",
        "Which animal is known as the King of the Jungle? ": "Lion",
        "Which continent is the Sahara Desert located in? ": "Africa",
        "Who was the first President of the USA? ": "George Washington",
        "What is the boiling point of water? ": "100",
        "What is the largest ocean on Earth? ": "Pacific",
        "What is the chemical symbol for gold? ": "Au",
        "Which gas do plants absorb from the atmosphere? ": "Carbon dioxide",
        "How many continents are there? ": "7",
        "What is the smallest prime number? ": "2",
        "Which planet has rings? ": "Saturn",
        "What year did World War II end? ": "1945",
        "How many days are there in a leap year? ": "366",
        "What is the hardest natural substance on Earth? ": "Diamond",
        "What language is primarily spoken in Brazil? ": "Portuguese",
        "Which is the longest river in the world? ": "Nile",
        "What is the square root of 144? ": "12",
        "What is H2O commonly known as? ": "Water",
        "What color do you get when you mix red and white? ": "Pink",
        "Which metal is heavier: silver or gold? ": "Gold",
        "How many legs does a spider have? ": "8",
        "Which planet is closest to the sun? ": "Mercury",
        "What is 9 squared? ": "81"
    }
    while True:
        score = 0
        selected = random.sample(list(questions.items()), 3)
        print("\n🧠 Quick Fun Quiz!")
        for q, ans in selected:
            user_ans = input(q)
            if user_ans.strip().lower() == ans.lower():
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Oops! The correct answer is {ans}.\n")
        print(f"🎯 Your score: {score}/3")
        again = input("\nType 'change' to go back or press Enter to try another quiz: ").strip().lower()
        if again == 'change' or again == 'change topic':
            break

def main():
    print("\n🎉 Welcome to the Stress Burster App! 🎉")
    while True:
        print("\nWhat would you like to do?")
        print("1. Hear a joke 😄")
        print("2. Get a pickup line 💌")
        print("3. Take a quick general knowledge quiz 🧠")
        print("4. Exit ❌")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            tell_joke()
        elif choice == '2':
            pickup_line()
        elif choice == '3':
            quiz()
        elif choice == '4':
            print("\n🌟 Stay positive! Study smart. Take breaks. You’ve got this! 🌟 See you next time cutie!\n")
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()