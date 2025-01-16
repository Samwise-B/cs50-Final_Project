# Capture The Flag (CTF) Educational Hacking Game

This project is a **full-stack web application** designed as an educational Capture The Flag (CTF) hacking game, where players identify vulnerabilities to "capture" flags hidden within the system. This project demonstrates my abilities in **web development, security, and DevOps** by creating a controlled environment with realistic vulnerabilities for educational purposes.

## Project Overview

In this CTF game, the objective is to discover hidden "flags"—unique strings that serve as keys to advancing through three increasingly challenging stages. Each stage requires players to exploit a specific security vulnerability in the system, honing their understanding of **cybersecurity fundamentals** and **web application vulnerabilities**.

### Vulnerabilities Modeled
This application intentionally includes three common security vulnerabilities to teach players about the nature and risks of each exploit:
1. **Poor Access Control**: Players must bypass weak authentication mechanisms to access restricted areas.
2. **Local File Inclusion (LFI)**: By exploiting path traversal, players can view files that should be inaccessible.
3. **Remote Code Execution (RCE)**: In the final stage, players uncover and execute code remotely on the server.

## Technologies Used

This CTF game was developed using the following stack:
- **Flask**: A lightweight Python web framework for rapid development and prototyping of the application.
- **SQLite with SQLAlchemy**: A relational database via SQLAlchemy for easy data manipulation and user progress tracking.
- **Bootstrap**: A responsive, mobile-first CSS framework for clean, user-friendly UI design.

### Key Skills Demonstrated
1. **Full-Stack Web Development**: Designed and implemented both backend and frontend, creating a cohesive, interactive experience.
2. **Application Security**: Built a practical application with real security flaws, showcasing an understanding of web security, common vulnerabilities, and mitigations.
3. **Database Management**: Used SQLAlchemy to interact with SQLite, demonstrating competence in data storage, retrieval, and management within a secure environment.
4. **DevOps & Dependency Management**: Managed dependencies, installation, and deployment processes to ensure the game runs smoothly in a controlled virtual environment.

## Installation and Setup

To set up the game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ctf-hacking-game.git
   cd ctf-hacking-game
2. **Install Dependencies**: Use pip to install the required dependencies:
   ```
   python -m pip install -r requirements.txt
3. **Run the Application**: After installing the dependencies, start the application:
   ```
   python app.py
The application is best run in a virtual machine to ensure isolation and security, as it contains intentional vulnerabilities.

# Learning Objectives and Takeaways
This project showcases a range of skills relevant to full-stack web development, cybersecurity, and DevOps. By developing this CTF game, I demonstrated:
- Proficiency in Vulnerability Modeling: Created a realistic environment for learning and understanding common vulnerabilities, showcasing knowledge of exploit mechanisms and application security.
- Backend Development: Developed a secure backend structure using Flask, ensuring smooth interaction between the application and the database.
- User-Centric Frontend Design: Used Bootstrap to create an intuitive user interface that guides players through the CTF stages.
- Efficient Deployment Practices: Managed dependencies and environment isolation, which are crucial for setting up applications with deliberate vulnerabilities.
This project is a practical example of my abilities to design, develop, and deploy secure, interactive applications, especially suited for educational purposes in cybersecurity.
