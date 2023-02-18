# Sample-Flask-API


This app.py is a simple Python script that can be used to create a basic web application. It uses the Flask framework to create a basic web server and provides some basic functionality such as routing and rendering HTML templates. This app.py can be used as a starting point for creating more complex web applications. 

To use this app.py, you will need to have Python installed on your computer, as well as the Flask framework. Once these requirements are met, you can run the script from the command line by typing `python app.py`. This will start up the web server and you can access it from your browser at http://localhost:5000/. 

The code in this app.py is commented to help explain what each part does, so feel free to explore and modify it to suit your needs.

# Explanation:
This code creates a Flask application with four routes. The first route is a GET request to '/users' which returns a list of users in JSON format. The second route is a GET request to '/users/<int:user_id>' which returns the details of a specific user in JSON format. The third route is a POST request to '/users' which creates a new user in JSON format. The fourth route is a PUT request to '/users/<int:user_id>' which updates an existing user in JSON format. Finally, the fifth route is a DELETE request to '/users/<int:user_id>' which deletes an existing user in JSON format.

# Documentaion:

This is a Flask application that provides routes for getting, creating, updating, and deleting users in JSON format. 

The `/users` route returns a list of users in JSON format. 

The `/users/<int:user_id>` route returns the details of a specific user in JSON format. 

The `/users` route with the POST method creates a new user in JSON format. 

The `/users/<int:user_id>` route with the PUT method updates an existing user in JSON format. 

The `/users/<int:user_id>` route with the DELETE method deletes an existing user in JSON format.
