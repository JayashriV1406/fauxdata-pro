from flask import Flask, render_template, request
from faker import Faker
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
fake = Faker()

# ✅ Define this first — before using it
def generate_bio(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []

    if request.method == 'POST':
        data_type = request.form.get('data_type')
        num_entries = int(request.form.get('count', 5))

        data_types = {
            "Name": fake.name,
            "Email": fake.email,
            "Address": fake.address,
            "Job": fake.job,
            "Phone Number": fake.phone_number,
            "Company": fake.company,
            "Date of Birth": fake.date_of_birth,
            "Credit Card": fake.credit_card_number,
            "City": fake.city,
            "Country": fake.country,
            "URL": fake.url,
            "Username": fake.user_name,
            "Text Snippet": fake.sentence,
            "AI-generated Bio": lambda: f"{fake.name()} is a software engineer at {fake.company()} who loves {fake.bs()}.",

        }

        if data_type in data_types:
            for _ in range(num_entries):
                data.append(data_types[data_type]())
        else:
            data.append("Unsupported type")

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
