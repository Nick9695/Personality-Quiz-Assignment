---

# Personality-Quiz-Assignment

## Table of Contents

1. [About](#about)
2. [Development Tools](#development-tools)
3. [Code](#code)
4. [Prerequisites](#prerequisites)
5. [UML](#uml)
6. [DDD](#ddd)
7. [Usage](#usage)
   - [Personality Quiz](#personality-quiz)
   - [Web App Implementation](#web-app-implementation)
8. [Conclusion](#conclusion)
9. [License](#license)

---

## About

The Personality-Quiz-Assignment is a Project made for educational purposes. This Quiz is played by answering a series of scenarios-based questions, developed using Python, Flask, and HTML, and aims to decipher user personality through friendly interactions.

---

## Development Tools

**Crafting with Precision**

In the development of this project, we utilize a suite of tools to ensure efficiency and excellence:

- **Python**:The programming language that forms the backbone of our project.
- **Flask**: A powerful web framework in Python, facilitating seamless web application development.
- **HTML**: Building the user interface with the standard language for web content.

---

## Code

The Python code file for the personality quiz is attached here [Code](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/project_outline_program_.py)

---

## Prerequisites

Prerequisites for your Personality Quiz project would include various components and tools that are essential for its development, deployment, and maintenance. Here's a list of potential prerequisites:

1. **Python:**
   - Ensure that Python is installed on your system. You can download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Flask:**
   - If you're using Flask for the web application, make sure Flask is installed. You can install Flask using the following command:
     ```
     pip install Flask
     ```

3. **HTML/CSS:**
   - Basic knowledge of HTML and CSS for designing and styling web pages.

4. **Web Browser:**
   - A web browser to test and view your web application.
     
5. **Understanding of HTTP and Web Development Basics:**
    - Have a basic understanding of how HTTP works and fundamental concepts in web development.

---

## UML

**UML**: *Visualizing Software Excellence*



Unified Modeling Language (UML) is a tool of choice for modeling and visualizing the intricate components of the software system. Find the below diagram for a better understanding of the project.

## Class Diagram to show the flow


[Class Diagram](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Class%20Diagram(flow%20of%20code).png)


 **Class diagram** :

The `User` class represents the person taking the personality quiz. It stores their name, date of birth, and calculated age.

The `PersonalityQuizManager` class manages the personality quiz process. It holds a reference to the `User` object, a list of `Question` objects, and provides methods for initializing the questions, calculating the personality scores, determining the personality type, and providing a personality explanation.

The `Question` class represents a single question in the personality quiz. It stores the question text and a list of possible answer choices.

The `PersonalityType` class represents the different personality types that can be identified from the quiz results. It contains the five personality types: Adventurer, Conscientious, Diplomat, Analyst, and Explorer.

The UML class diagram shows the relationships between the classes:

* The `PersonalityQuizManager` class has a reference to the `User` object.
* The `PersonalityQuizManager` class has a list of `Question` objects.
* The `Question` class has no references to other classes.

## Activity Diagram 

[Activity Diagram](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Activity%20Diagram.png)


**Explanation of each step in the flowchart:**

* **Get User's Name:** The flowchart starts by asking the user for their name. This information can be used to greet the user and to personalize the experience.
* **Valid Name?** The flowchart then checks if the user's name is valid. This means checking that the name is not empty and that it does not contain any special characters.
* **Get User's Date of Birth:** If the user's name is valid, the flowchart asks the user for their date of birth. This information can be used to calculate the user's age and to greet them based on their age.
* **Valid DOB Format?** The flowchart then checks if the user's date of birth is in a valid format. This means checking that the date is in a format that can be understood by the system.
* **Greet User Based on Age:** If the user's date of birth is in a valid format, the flowchart greets the user based on their age. For example, the flowchart might greet a user who is under 18 years old with "Hello, [user name]! How can I help you today?" and greet a user who is over 18 years old with "Welcome to our website, [user name]!"
* **Initialize Variables:** The flowchart then initializes some variables. These variables will be used to store the user's personality scores and other information about the user.
* **Ask Scenario-Based Questions:** The flowchart then asks the user a series of scenario-based questions. These questions are designed to assess the user's personality. For example, the flowchart might ask the user "What would you do if you saw someone lost and alone?" or                                        "What is your favorite way to spend a rainy day?"
* **Update Personality Scores:** The flowchart uses the user's answers to the scenario-based questions to update their personality scores. These scores will be used to determine the user's personality type.
* **Questions Remaining?** The flowchart then checks if any questions are remaining. If there are, the flowchart asks the user to answer the next question. If no questions are remaining, the flowchart displays the user's personality results.
* **Display Result:** The flowchart displays the user's personality results. These results might include the user's personality type, their personality strengths and weaknesses, and some tips on how to improve their personality.
* **Ask to Understand Personality?** The flowchart then asks the user if they want to understand their personality better. If they do, the flowchart displays an explanation of their personality results. The explanation might include information about what the user's personality type means, how it can impact their behavior, and how to develop their personality.


## Component Diagram

[Component Diagram](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Component%20diagram.png)

**Explanation of each step in the Component Chart:**

The User class represents a user of the personality quiz. The Personality Quiz Manager class is responsible for managing the personality quiz, including asking the user questions and calculating their personality type. The Question class represents a question in the personality quiz. The Personality Type class represents a personality type.

The diagram shows that the User class has a one-to-many relationship with the Question class. This means that a User can answer many Questions, but a Question can only be answered by one User.

The diagram also shows that the Personality Quiz Manager class has a one-to-many relationship with the Question class. This means that a Personality Quiz Manager can manage many Questions, but a Question can only be managed by one Personality Quiz Manager.

Finally, the diagram shows that the Personality Quiz Manager class has a one-to-many relationship with the Personality Type class. This means that a Personality Quiz Manager can calculate many Personality Types, but a Personality Type can only be calculated by one Personality Quiz Manager.


* **User:** The User class represents a user of the personality quiz. It contains the user's name, date of birth, and personality type.
* **Personality Quiz Manager:** The PersonalityQuizManager class is responsible for managing the personality quiz, including asking the user questions and calculating their personality type. It contains a list of Questions and a list of personality types.
* **The Question class:** represents a question in the personality quiz. It contains the question text and a list of possible answers.
* **Personality Type:** The PersonalityType class represents a personality type. It contains the name of the personality type, a description of the personality type, and a list of the personality type's strengths and weaknesses.


---

## DDD

**DDD**: *Navigating Complexity with Precision*

Domain-Driven Design (DDD) is our guiding philosophy. By placing a strong emphasis on understanding and solving complex business problems, we ensure that our software is not just functional but aligns seamlessly with real-world scenarios and requirements, this area is still under - process and will be uploaded soon!!

**Core domain**

A core domain chart, also known as a domain model, illustrates the main entities, their attributes, and the relationships between them as per the below chart:

[Core domain](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Core%20domain.png)


This core domain chart reflects the key entities and their relationships in the project. 

Some points to note:

**User**: 
Represents the user participating in the quiz.

**Question**: 
Represents a scenario-based question with choices.

**Answer**: 
Represents a user's response to a specific question.

**Personality Type**: 
Represents a specific personality type.

**Personality Scores**: 
Manages the scores for each personality type.

**Personality Quiz**: 
Aggregates user, questions, answers, personality scores, and orchestrates the quiz flow.

**Quiz Configuration**: 
Interface for obtaining quiz questions.

**UserProfile**:
Interface for validating user details.

---

## Usage

### Personality Quiz

**Peek into the Soul through Scenarios**

The Personality Quiz is the heart of our application. Users navigate a carefully crafted set of scenario-based questions, providing responses that become the palette for determining their unique personality profile.

### Web App Implementation

**Crafting Experiences with Flask and HTML**

Our web application comes to life with the dynamic duo of Python's Flask framework and HTML. Flask provides a robust foundation for web development, while HTML shapes the user interface, creating an immersive and intuitive experience.

---

## Conclusion 
This is a sneak peek of my project, which is a web-based quiz game. I'm still working on the details, so feel free to point out any errors or bugs. Right now, I only have the Python code for the quiz logic, but I plan to create a web page for the user interface. Here is a rough sketch of how the quiz will work in Python code.

---

## License

This project is privately owned by Nikhil Raju Gadekar, a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science with a specialization in Big Data and Artificial Intelligence.

**Contact Information:**
- **Name**: Nikhil Raju Gadekar
- **Email**: gernikhilgadekar@gmail.com

---
