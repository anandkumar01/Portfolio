## Run these Commands
### Step 1 : Clone the Repository
     git clone <repository>

### Step 2 : Create and Activate a Virtual Environment
     python -m venv venv

### Step 3 : Install Project Dependencies
     pip install -r requirements.txt

### Step 4 : Set Up the Database
     python manage.py migrate
     
### Step 5 : Create a Superuser
     python manage.py createsuperuser
        
### Step 6 : Run the Development Server
     python manage.py runserver
