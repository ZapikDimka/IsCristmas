IsCristmas Project
This project is designed to check whether today is Christmas and implements a "Secret Santa" game using the Django framework.

 Description
1. **Is it Christmas?** — A simple page that shows if today's date is December 25th.
2. **Secret Santa** — An app where users can add participants and generate pairs for the "Secret Santa" game. Each participant is assigned to give a gift to another, ensuring no one gives a gift to themselves.

 Requirements
Before starting, ensure you have the following installed:
- Python 3.10+
- Django 4.2.15
- Virtual environment (recommended to use `venv`)

 Setup and Run Instructions
1. Clone the repository
Clone this project to your local machine using the following command:
```bash
git clone https://github.com/yourusername/IsCristmas.git
cd IsCristmas
    Create a virtual environment
It is recommended to use a virtual environment to isolate the project dependencies. You can create one using venv:
python -m venv .venv
    Activate the virtual environment
Activate the virtual environment using the following command: For Windows:
.venv\Scripts\activate
For macOS/Linux:
source .venv/bin/activate
Install dependencies
Once the virtual environment is activated, install the dependencies using the following command:
pip install -r requirements.txt
    Apply database migrations
After installing the dependencies, apply the database migrations to create the required tables:
python manage.py migrate
    Run the development server
Run the Django development server using the following command:
python manage.py runserver
Now open your browser and go to: http://127.0.0.1:8000/.
Accessing the pages
    Is it Christmas?: Go to the homepage at http://127.0.0.1:8000/ to see if today is Christmas.
    Secret Santa Game: Navigate to http://127.0.0.1:8000/secret_santa/ to add participants and generate pairs for the game.
Project Files
    hello/views.py — Main logic for date checking and the "Secret Santa" game.
    hello/templates/hello/ — HTML templates for page rendering.
    static/css/styles.css — Basic styles for the pages.
