---

# Personality-Quiz-Assignment

## Table of Contents

1. [About](#about)
2. [Development Tools](#development-tools)
3. [Code](#code)
4. [Requirement Engineering](#requirement-engineering)
5. [Prerequisites](#prerequisites)
6. [UML](#uml)
7. [DDD](#ddd)
8. [Metrics](#metrics)
9. [Clean Code](#clean-code)
10. [Functional Programming](functional-programming)
11. [Unit Test](#unit-test)
12. [Build Management](build-management)
13. [Usage](#usage)
   - [Personality Quiz](#personality-quiz)
   - [Web App Implementation](#web-app-implementation)
14. [IDE and Shortcuts](#ide-and-shortcuts)
15. [Analysis](#analysis)    
16. [Conclusion](#conclusion)
17. [License](#license)

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

The Python code file for the personality quiz is attached here [Personality Quiz](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/project_outline_program_.py)

---

## Requirement Engineering

Requirement engineering for my project involves gathering, analyzing, documenting, and managing the needs and constraints of the system's users and stakeholders. It's a crucial phase where clear and complete specifications are defined to guide the software development process. This includes understanding user expectations, functional and non-functional requirements, and potential risks. Effective requirement engineering ensures that the final software product meets user expectations and operates smoothly within the specified constraints, leading to a successful and satisfying outcome for both developers and users.


**Professional variant**

[JIRA](https://gernikhilgadekar.atlassian.net/jira/software/projects/PQ/boards/2)

![Jira](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/4a3fcb21-0b13-478e-aa9d-ed4fdbecc593)


**Self-Use variant**

[Trello](https://trello.com/b/lCjqUhXa/personality-quiz)

![Trello](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/cce056d1-f72a-4d53-b287-6356908a55c4)


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

## Component Diagram

[Component Diagram](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Component%20diagram.png)


---

## DDD

**DDD**: *Navigating Complexity with Precision*

Domain-Driven Design (DDD) is our guiding philosophy. By placing a strong emphasis on understanding and solving complex business problems, we ensure that our software is not just functional but aligns seamlessly with real-world scenarios and requirements, this area is still under - process and will be uploaded soon!!

**Core domain**

A core domain chart, also known as a domain model, illustrates the main entities, their attributes, and the relationships between them as per the below chart:

[Core domain](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Core_Domains.png)


This core domain chart reflects the key entities in the project. 

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

--

**Relation of Domains**

In my project, various domains collaborate to create a seamless experience. User Management oversees user interactions, while Quiz Configuration manages quiz settings. Results Presentation and User Feedback work together to deliver and collect user insights. The Scoring Algorithm analyzes answers, connecting them with Personality Types to provide accurate results.

[Domain Relations](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/relation.png)

---

## Metrics

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Nick9695_Personality-Quiz-Assignment&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Nick9695_Personality-Quiz-Assignment)

**Screenshot**

The Badge screenshot if in the future the links for batch gets expired.


![Screenshot 2024-01-19 151758](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/ad04552a-e4a4-4e91-9fde-6dbec31e0030)


---

## Clean Code

Clean Code Development is writing code that is easy to read, understand, and maintain. It involves using meaningful names, consistent formatting, and avoiding unnecessary complexity. Clean code follows principles like Single Responsibility and aims for simplicity, making it more efficient for collaboration and long-term software development.
Find below the Clean code for the Personality quiz: 

[Clean Code](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Clean%20Code%20Development.pdf)


## Functional Programming

Functional programming is a coding paradigm that treats computation as the evaluation of mathematical functions. It emphasizes immutability, where data doesn't change after creation. Functions are first-class citizens, meaning they can be assigned to variables, passed as arguments, and returned as results. This approach simplifies reasoning about code and encourages concise, modular, and predictable programs.

[functional Programming](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/7abc6626dba7837f71560bb1508be0f8da1abb93/functional_programming_.py#L13)

[final data structure](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/7abc6626dba7837f71560bb1508be0f8da1abb93/functional_programming_.py#L13)

[Side-effect free functions](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/b5ba9c4c59a6d50ad33f37d4290a258eaa9c0eba/functional_programming_.py#L24)

[Higher order fuction](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/b5ba9c4c59a6d50ad33f37d4290a258eaa9c0eba/functional_programming_.py#L28)

[Functions parameters and return values](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/b5ba9c4c59a6d50ad33f37d4290a258eaa9c0eba/functional_programming_.py#L32)

[Use of closures/anonymous functions](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/b5ba9c4c59a6d50ad33f37d4290a258eaa9c0eba/functional_programming_.py#L40)

[Immutable data structures](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/b5ba9c4c59a6d50ad33f37d4290a258eaa9c0eba/functional_programming_.py#L46)

[Recursion](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/b5ba9c4c59a6d50ad33f37d4290a258eaa9c0eba/functional_programming_.py#L49C6-L49C15)

---

## Unit Test

The unit tests simulate user input to check if the personality quiz functions correctly. Each test represents a user scenario, such as an Adventurer, Conscientious, or Explorer personality type. The tests ensure that the program responds appropriately to input and provides accurate personality type descriptions, validating the quiz's functionality.

**Test Code**

[Unit test](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/Unit%20test/Test_code.py)


**Test Score** 

![Result](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/2e1629e7-768e-4794-ba73-2e861600e84c)


---

## Build Management

I have used Py Builder for the build management to run the project successfully. And merge my files with Pybuilder find below screenshot 

[Command Prompt](https://github.com/Nick9695/Personality-Quiz-Assignment/blob/main/commandprompt.txt)

![Build_Successful](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/9cc5c854-4846-4638-ba9b-8fc714574bbe)

---

## Usage

### Personality Quiz

**Peek into the Soul through Scenarios**

The Personality Quiz is the heart of our application. Users navigate a carefully crafted set of scenario-based questions, providing responses that become the palette for determining their unique personality profile.

### Web App Implementation

**Crafting Experiences with Flask and HTML**

Our web application comes to life with the dynamic duo of Python's Flask framework and HTML. Flask provides a robust foundation for web development, while HTML shapes the user interface, creating an immersive and intuitive experience.

---

## IDE and Shortcuts

**IDE :** 
  Choosing an IDE depends on personal preference and the programming language So for me as Python user it was either of these Pycharm, VSCode, Google Colab.

**Shortcuts :**
 The best shortcuts depend on what you need and want to do, but here are some of the ones I use all the time and are easy to remember. 

 **PyCharm:**

Key Shortcuts:

Ctrl + Space: Auto-complete code.

Ctrl + Alt + L (Windows/Linux) or Cmd + Alt + L (Mac): Reformat code.

Ctrl + Shift + A (Windows/Linux) or Cmd + Shift + A (Mac): Find actions and commands.

Ctrl + E (Windows/Linux) or Cmd + E (Mac): Recent files.

Ctrl + Shift + F10 (Windows/Linux) or Shift + Cmd + F10 (Mac): Run the script.


**VSCode:**

Key Shortcuts:

Ctrl + Space: Auto-complete code.

Alt + Shift + F: Reformat code.

Ctrl + P: Quick file navigation.

Ctrl + `: Open the integrated terminal.

F5: Run the script.

---

## Analysis 

Analysis for my project involves studying requirements, understanding user needs, and defining system functionalities. It aims to identify problems, determine project scope, and create a foundation for development. This process ensures a clear understanding of goals, facilitating effective design and implementation decisions throughout the project lifecycle.


1. [Analysis Checklist](https://sixth-hose-3a1.notion.site/Checklist-for-the-Personality-Quiz-Project-38518afcda924306af65cb91e8236115?pvs=4)
2. [Analysis Documents](https://sixth-hose-3a1.notion.site/Analysis-of-the-Personality-Quiz-Project-1e7d14ea63a4448fbdfb7495e3e2cfe1?pvs=4)
3. [Analysis for semester Project](https://sixth-hose-3a1.notion.site/Semester-Project-Analysis-119884e6dc1341e6b46d2b1bcc62d2ae?pvs=4)

---


## Conclusion 
This is a sneak peek of my project, which is a web-based quiz game. I'm still working on the details, so feel free to point out any errors or bugs. Right now, I only have the Python code for the quiz logic, but I plan to create a web page for the user interface. Here is a rough sketch of how the quiz will work in Python code.


---

## License

This project is privately owned by Nikhil Raju Gadekar, a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science with a specialization in Big Data and Artificial Intelligence.


**Contact Information:**
- ![Screenshot 2023-12-11 224350](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/3c82c2b7-876d-447d-b149-dcd2fddedf23)
Nikhil Raju Gadekar
-  [![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gernikhilgadekar@gmail.com)
---
