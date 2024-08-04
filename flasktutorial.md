# Flask Tutorial

Flask is a lightweight Python framework that includes a development server. It's ideal for building web applications and APIs quickly and with minimal boilerplate code.
#Db 
## Setting Up Flask

To set up Flask and run your application:

1. **Install Flask:**
   - Create a virtual environment (optional but recommended):

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:

     ```bash
     # On Windows
     venv\Scripts\activate
     # On macOS/Linux
     source venv/bin/activate
     ```

   - Install Flask using pip:

     ```bash
     pip install flask
     ```

2. **Run Your Flask Application:**
   - In Windows, set the FLASK_APP environment variable to your main application file:

     ```bash
     set FLASK_APP=filename.py
     ```

   - Alternatively, on macOS/Linux:

     ```bash
     export FLASK_APP=filename.py
     ```

   - Start the Flask development server:

     ```bash
     flask run
     ```

3. **Development Mode:**
   - To enable debug mode (optional, for development):

     ```bash
     # On Windows
     set FLASK_DEBUG=1
     # On macOS/Linux
     export FLASK_DEBUG=1
     ```

   - This mode enables features like automatic reloading when code changes occur, making development faster and easier.
## Flask-WTF
For the frontend development and inbuilt forms, we use Flask-WTF. Flask-WTF is an extension that integrates Flask with WTForms, allowing for easy form creation and validation.

### Setting Up Flask-WTF

1. Install Flask-WTF:
    ```bash
    pip install flask-wtf
    ```

2. Use the `FlaskForm` class as the parent class for your form. Here is an example of a simple registration form using Flask-WTF:

## SQLAlchemy
ORM for different databases(Object Relational Mapper )
1. Install sqlAlchemy:
    ```bash
    pip install flask-sqlalchemy
    ```
## Summary

Flask provides a straightforward way to create web applications in Python. By following these steps, you can set up a Flask environment, run your application locally, and leverage debugging features to streamline your development process.

The module import issues discussed in -Miguel greenberg 2016 pycon scaling flask
https://www.youtube.com/watch?v=tdIIJuPh3SI&ab_channel=PyCon2016