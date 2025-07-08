# FauxData Pro 🧪📊

FauxData Pro is a smart synthetic data generator built using Python and Flask. It helps you quickly generate realistic fake data (like names, emails, addresses, companies, etc.) for testing AI models, applications, or data pipelines — without using real user data.

---

## 🚀 Features

- Generate synthetic data across various types:
  - Names, Emails, Addresses, Companies, Credit Cards, Cities, etc.
- Simple web interface built with Flask
- Choose number of entries to generate
- Safe for demos, testing, and academic use

---

## 🛠️ Built With

- Python
- Flask
- Faker
- HTML (Jinja templating)

---

## 📸 How to Run

```
pip install -r requirements.txt
python app.py

---
##Open in browser:
http://127.0.0.1:5000
```
📁 Folder Structure
fauxdata-pro/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

---
🧠 New Feature: AI-generated Bios with GenAI
You can now generate realistic fake bios using Generative AI!

How it works:
Select "AI-generated Bio" from the dropdown

Enter number of bios to generate

Click Generate – it uses the OpenAI API to create smart, human-like bios

Example:
“Samantha Blake is a software engineer at TechNova who loves leveraging cloud-based synergies.”
