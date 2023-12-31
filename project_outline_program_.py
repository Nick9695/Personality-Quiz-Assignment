import datetime

def calculate_age(dob):
    today = datetime.datetime.today()
    birth_date = datetime.datetime.strptime(dob, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def personality_quiz():
    # Greet the user and ask for their name
    user_name = input("Welcome to the Personality Quiz! What's your name? ")

    # Validate user name to ensure it doesn't contain numbers
    while True:
        if not user_name.isalpha():
            print("Please enter a valid name without any numbers.")
            user_name = input("Enter your name: ")
        else:
            break

    print(f"Nice to meet you, {user_name}!\n")

    # Ask for the user's date of birth repeatedly until it's entered correctly
    while True:
        try:
            dob = input("Before we start, please enter your date of birth (YYYY-MM-DD): ").strip()
            age = calculate_age(dob)
            break
        except ValueError:
            print("Please enter your date of birth in the correct format (YYYY-MM-DD).")

    # Provide a personalized greeting based on age
    if age < 18:
        print("Wow, you're quite young! Let's dive into the quiz and explore your personality.")
    elif 18 <= age <= 30:
        print("You're at a great age! Let's uncover the layers of your personality.")
    else:
        print("Age is just a number! Your life experiences will surely reflect in your personality.")

    # Initialize variables
    personality_scores = {
        "Adventurer": 0,
        "Conscientious": 0,
        "Diplomat": 0,
        "Analyst": 0,
        "Explorer": 0,
    }

    # Define questions and answer choices
    questions = [
        ("You are walking down the street and you see a homeless person begging for money. What do you do?",
         ["Give them some money", "Ignore them", "Offer to buy them a meal"]),
        ("You are working on a group project and one of your teammates is not pulling their weight. What do you do?",
         ["Confront them directly", "Take on their responsibilities yourself", "Talk to the professor about the situation"]),
        ("Your friends are planning a vacation and ask for your choice?",
         ["Relaxing beach trip", "Adventurous mountain climbing trip","Netflix and chill in the room"]),
        ("You are at a party and you see someone you know being bullied. What do you do?",
         ["Intervene and defend the person", "Ignore the situation", "Talk to the bully privately"]),
        ("You are working on a difficult problem and you come across a dead end. What do you do?",
         ["Give up and move on", "Keep trying to find a solution", "Ask for help from a colleague"]),
        ("You are walking in the woods and you come across a lost animal. What do you do?",
         ["Try to find the animal's owner", "Leave the animal alone", "Take the animal home with you"]),
        ("You are at a restaurant and you are not satisfied with your meal. What do you do?",
         ["Complain to the waiter", "Eat the meal anyway", "Leave without paying"]),
        ("You are walking down the street and you see a shop window that has been smashed. What do you do?",
         ["Call the police", "Ignore it", "Try to fix the window"]),
        ("You are working on a team project and you disagree with one of your teammates. How do you resolve the conflict?",
         ["Try to see things from your teammate's perspective", "Stick to your own opinion", "Avoid talking to your teammate about it"]),
        ("You are at a party and you are not having a good time. What do you do?",
         ["Leave the party", "Try to find someone to talk to", "Stay at the party and try to make the best of it"])
    ]

    # Ask the questions and update the personality scores
    for question, answer_choices in questions:
        print(question)
        for i, answer_choice in enumerate(answer_choices):
            print(f"{i + 1}. {answer_choice}")

        while True:
            try:
                answer = int(input("Enter your choice (1-3): "))
                if 1 <= answer <= 3:
                    break
                else:
                    print("Please enter a valid choice (1-3).")
            except ValueError:
                print("Please enter a valid numeric choice.")

        # Update personality scores based on the user's answer
        if answer == 1:
            personality_scores["Adventurer"] += 1
            personality_scores["Diplomat"] += 1
        elif answer == 2:
            personality_scores["Analyst"] += 1
            personality_scores["Conscientious"] += 1
        elif answer == 3:
            personality_scores["Explorer"] += 1

    # Check if the user answered all questions
    if sum(personality_scores.values()) == 0:
        print("You missed answering some questions. Please answer all questions to understand your personality.")
        return

    # Greet the user based on their quiz performance
    print("\nGreat job! Let's see what your personality reveals...\n")

    # Calculate the highest personality score and determine the personality type
    highest_score = max(personality_scores.values())
    personality_type = ""
    for personality, score in personality_scores.items():
        if score == highest_score:
            personality_type = personality

    # Display the personality type with explanation
    print(f"Drumroll, please!!! Your personality type is: {personality_type}")

    if personality_type == "Adventurer":
        print("\nAs an Adventurer, you're spontaneous and love taking risks. Embrace new challenges and explore the unknown!")
    elif personality_type == "Conscientious":
        print("\nAs a Conscientious person, you're organized and detail-oriented. You ensure tasks are completed with precision and care.")
    elif personality_type == "Diplomat":
        print("\nDiplomats are empathetic and cooperative. They seek harmony in their relationships and are excellent communicators.")
    elif personality_type == "Analyst":
        print("\nAnalysts are logical and objective thinkers. They enjoy solving complex problems and analyzing information thoroughly.")
    elif personality_type == "Explorer":
        print("\nExplorers are curious and adaptable. They love variety and spontaneity, thriving in situations that offer new experiences.")
    else:
        print("\nYour personality type is unique and cannot be categorized easily.")

    # Ask if the user wants to understand their personality
    understand_personality = input("What a great personality, Would you like to understand in more detail about your personality? (yes/no): ").lower()

    if understand_personality == "yes":
        # Provide a brief explanation of the user's personality
        print("\nIn a nutshell:")
        if personality_type == "Adventurer":
            print("Adventurers are spontaneous and adventurous individuals who are always seeking out new experiences and challenges. They are typically outgoing, energetic, and enthusiastic, and they thrive in fast-paced environments. Adventurers are often risk-takers, and they are not afraid to step outside of their comfort zones. They are also highly adaptable and resourceful, and they can thrive in a variety of situations.")
        elif personality_type == "Conscientious":
            print("Conscientious individuals are organized, detail-oriented, and reliable. They take pride in their work, and they are always striving to do things right. Conscientious people are also responsible and dependable, and they can always be counted on to follow through on their commitments. They are also efficient and productive, and they can get things done without wasting time or resources.")
        elif personality_type == "Diplomat":
            print("Diplomats are empathetic and cooperative individuals who seek harmony in relationships. They are excellent communicators, and they can see things from different perspectives. Diplomats are also skilled at resolving conflict, and they can build consensus among others. They are also patient and understanding, and they can connect with people from all walks of life.")
        elif personality_type == "Analyst":
            print("Analysts are logical and objective individuals who enjoy solving complex problems and analyzing information thoroughly. They are also detail-oriented and meticulous, and they can see patterns and connections that others might miss. Analysts are also independent and self-reliant, and they are not afraid to challenge the status quo. They are also open-minded and curious, and they are always seeking out new knowledge and information.")
        elif personality_type == "Explorer":
            print("Explorers are curious and adaptable individuals who thrive in situations that offer new experiences and variety. They are also open-minded and flexible, and they can adjust to new environments and challenges with ease. Explorers are also independent and resourceful, and they can find solutions to problems in unconventional ways. They are also creative and imaginative, and they are always coming up with new ideas.")
        else:
            print("Your personality type is unique and cannot be categorized easily.")
    else:
        print("Best of luck on your journey! If you ever want to explore your personality further, feel free to return.")

if __name__ == "__main__":
    personality_quiz()
