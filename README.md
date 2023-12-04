---

# Personality-Quiz-Assignment

## Table of Contents

1. [About](#about)
2. [Development Tools](#development-tools)
3. [Code](#code)
4. [UML](#uml)
5. [DDD](#ddd)
6. [Usage](#usage)
   - [Personality Quiz](#personality-quiz)
   - [Web App Implementation](#web-app-implementation)
7. [License](#license)

---

## About

The Personality-Quiz-Assignment is a Project made for educational purposes. This Quiz is played by answering a series of scenarios-based questions, developed using Python, Flask, and HTML, and aims to decipher user personality through friendly interactions.

---

## Development Tools

**Crafting with Precision**

In the development of this project, we utilize a suite of tools to ensure efficiency and excellence:

- **Python**: The programming language that forms the backbone of our project.
- **Flask**: A powerful web framework in Python, facilitating seamless web application development.
- **HTML**: Building the user interface with the standard language for web content.

---

## Code

The Python code file for the personality quiz is attached here [Code](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/project_outline_program_.py)


---

## UML

**UML**: *Visualizing Software Excellence*



Unified Modeling Language (UML) is a tool of choice for modeling and visualizing the intricate components of the software system. Find the below diagram for a better understanding of the project.


![Class Diagram(flow of code)](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/8a63e836-d8e6-475d-b2d9-b35b52f6b7bc)



![chatuml-diagram](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/72ef836d-7664-4c58-9932-6db220e35831)


Class diagram for the personality quiz project:

The `User` class represents the person taking the personality quiz. It stores their name, date of birth, and calculated age.

The `PersonalityQuizManager` class manages the personality quiz process. It holds a reference to the `User` object, a list of `Question` objects, and provides methods for initializing the questions, calculating the personality scores, determining the personality type, and providing a personality explanation.

The `Question` class represents a single question in the personality quiz. It stores the question text and a list of possible answer choices.

The `PersonalityType` class represents the different personality types that can be identified from the quiz results. It contains the five personality types: Adventurer, Conscientious, Diplomat, Analyst, and Explorer.

The UML class diagram shows the relationships between the classes:

* The `PersonalityQuizManager` class has a reference to the `User` object.
* The `PersonalityQuizManager` class has a list of `Question` objects.
* The `Question` class has no references to other classes.


---

## DDD

**DDD**: *Navigating Complexity with Precision*

Domain-Driven Design (DDD) is our guiding philosophy. By placing a strong emphasis on understanding and solving complex business problems, we ensure that our software is not just functional but aligns seamlessly with real-world scenarios and requirements, this area is still under - process and will be uploaded soon!!

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
Currently, only Python code is made this is a web page-based project and I plan to make a web page so I have made an outline in Python code of how my Quiz will unfold.

---

## License

This project is privately owned by Nikhil Raju Gadekar, a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science with a specialization in Big Data and Artificial Intelligence.

**Contact Information:**
- **Name**: Nikhil Raju Gadekar
- **Email**: gernikhilgadekar@gmail.com

---
