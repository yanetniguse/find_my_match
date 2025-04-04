💞 Find My Match – Rule-Based Dating Compatibility System
A rule-based expert system to simulate human decision-making in relationship matchmaking.
Developed as a final project for APT 3020B Artificial Intelligence, USIU-Africa.

🧠 Overview
Find My Match is a web-based matchmaking system built using a knowledge-based approach. It analyzes user profile data—such as age, faith, interests, education, and values—to calculate a compatibility score between two people.

This project demonstrates how rule-based reasoning can be applied in matchmaking through a Knowledge-Based System (KBS).

🎯 Features
🔎 Rule-based compatibility engine

🧬 Custom profile attribute matching (age, faith, hobbies, etc.)

📋 Scoring system with weighted rules

🌐 Web interface built with Flask

🔥 Returns compatibility percentage instantly

🛠️ How It Works
Attributes Used for Matching
Age

Gender

Faith + Importance of Faith

Values

Education

Hobbies

Places of Interest

Relationship Goals

Height & Weight (optional)

Compatibility Scoring Rules
Attribute	Rule Description	Points
Age Gap	≤ 5 years: +10, >10 years: -5	Age Normalized
Shared Faith	Exact match: +10	High
Faith Importance	Both high: +5	Medium
Shared Values	Exact match: +10	High
Hobbies	Each match: +3	Medium
Places	Each match: +2	Low
Education Level	Match: +5	Medium
🧪 Sample Usage
User 1 and User 2 fill in a form with their profile data

System processes and calculates their match score

Result is rendered with the compatibility percentage

Example Output:

bash
Copy
Edit
User A & User B compatibility: 84%
Shared values, interests, and faith contribute to high compatibility.
💻 Tech Stack
Backend: Python (Flask)

Frontend: HTML + Jinja2 Templates

Logic Engine: Custom rule-based compatibility system

Data Handling: In-memory dictionaries (can be extended to DB)

📚 Academic Context
This project was built as part of the coursework for:

Course: APT 3020B – Artificial Intelligence
Instructor: Prof. Austin Odera
Based on Reference Text:
“Knowledge-Based Systems” by Rajendra Akerkar & P. Sajja

👨‍💻 Contributors
Name	GitHub Handle
James Otieno	@jayotieno
Yanet Niguse	@yanetniguse
Dhruv Pokhariyal	@P0lcahontas
Kwame Lucheveli	@luche3002
🚀 Try It Out
Clone this repo:

bash
Copy
Edit
git clone https://github.com/yanetniguse/find_my_match.git
cd find_my_match
python app.py
Access it in your browser:
http://localhost:5000
