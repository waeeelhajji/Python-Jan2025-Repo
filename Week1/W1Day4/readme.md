# Introduction to Flask Web Development

## Table of Contents
- [Introduction to Flask Web Development](#introduction-to-flask-web-development)
  - [Table of Contents](#table-of-contents)
  - [What is a Full Stack App?](#what-is-a-full-stack-app)
  - [Server-Side Rendering vs Client-Side Rendering](#server-side-rendering-vs-client-side-rendering)
    - [**Server-Side Rendering (SSR):**](#server-side-rendering-ssr)
    - [**Client-Side Rendering (CSR):**](#client-side-rendering-csr)
  - [What is a Framework?](#what-is-a-framework)
    - [Flask Framework:](#flask-framework)
  - [Topics Covered First Flask App](#topics-covered-first-flask-app)
    - [1 - Virtual Environments](#1---virtual-environments)
    - [2 - Routing](#2---routing)
    - [3 - Rendering Templates](#3---rendering-templates)
    - [4 - Path Variables](#4---path-variables)
    - [5 - Static Files](#5---static-files)

---

## What is a Full Stack App?

A **Full Stack Application** combines:
- **Frontend (Client-side)**: User-facing part of the application.
- **Backend (Server-side)**: Handles logic, database operations, and server interactions.
- **Database**: Stores and retrieves data.

---

## Server-Side Rendering vs Client-Side Rendering

### **Server-Side Rendering (SSR):**
- The server processes the request, executes necessary code, and renders the final HTML.

### **Client-Side Rendering (CSR):**
- The browser downloads JavaScript and uses it to render HTML, often by fetching additional data through APIs.

---

## What is a Framework?

A **framework** is a collection of pre-written code that provides a structure and set of tools for building software applications.

### Flask Framework:
- Flask is a lightweight and flexible **web development framework for Python**.
- Often referred to as a **micro-framework** because it provides only essential tools to build web applications.

---

## Topics Covered First Flask App

### 1 - Virtual Environments
- **What are virtual environments?**
  - Isolated environments to manage dependencies for projects.
  - Use **pipenv** for creating and managing virtual environments.
- **Why are virtual environments important?**
  - Prevent dependency conflicts.
  - Ensure isolated environments for larger projects.
- **Creating a virtual environment with `pipenv`:**
  ```bash
  pip install pipenv
  pipenv install flask
  ```
- **Activating the virtual environment:**
  ```bash
  pipenv shell
  ```
- **Running the server file**:
  - Create a file called `server.py`:
    ```python
    from flask import Flask
    app = Flask(__name__)

    if __name__ == "__main__":
        app.run(debug=True)
    ```
  - Run the file:
    ```bash
    python server.py
    ```
  - Visit `http://127.0.0.1:5000` in your browser to see your application in action.
---

### 2 - Routing
- **Why?** Routing allows you to define endpoints that respond to specific URLs.
- **HTTP Request/Response Cycle**:
  - A journey of a request from the client to the server and back as a response.
    - Client (browser) sends a request to the server.
    - Flask (server) processes the request and returns a response.
  - Example: **Restaurant analogy**.
- **Routing in Flask**:
  - Use decorators like `@app.route` to listen for endpoints.
  - Each route is linked to a function to return content (HTML/text) to the browser.
**Example**:
```python
@app.route('/')
def welcome():
    return "Welcome to Flask!"
```
---

### 3 - Rendering Templates

**Why?** Templates allow you to dynamically generate HTML content.

- **Rendering HTML Templates**:
  - Create a folder named `templates` and add an HTML file (e.g., `index.html`).
  - Use `render_template` function to serve HTML files.
    ```python
    from flask import render_template

    @app.route('/')
    def home():
        return render_template('index.html')
    ```

- **Jinja2**:
  - Flask's templating engine for rendering HTML. It enables dynamic content in HTML.
  - Features:
    - **Conditions** and **Looping**.
    - Separation of logic (Python) from presentation (HTML).
- **Passing data from server to template**:
  ```python
  @app.route('/users')
  def get_users():
    users = [
          {"id": 1, "username": "Alice"},
          {"id": 2, "username": "Bob"},
          {"id": 3, "username": "Charlie"},
          {"id": 4, "username": "Diana"}
      ]
      return render_template('users.html', all_users=users)
  ```
- **Looping with Jinja and displaying information**:
  ```html
  <h1>List of Users</h1>
  <ul>
      {% for one_user in all_users %}
      <li>{{ one_user.username }}</li>
      {% endfor %}
  </ul>
  ```
---

### 4 - Path Variables

**Why?** Path variables allow dynamic content by extracting data from URLs.

- **Dynamic Routing**:
  - Accept variables in the URL using dynamic routes.
  - Example: `/user/<username>`.
- **Handling Different Data Types**:
  - Convert variables in routes.
- **Security Concerns**:
  - Validate input to avoid potential vulnerabilities.
- **Setting up routes to accept path variables**:
  ```python
  @app.route('/greet/<name>')
  def greet(name):
      return render_template("greet.html", name = name)
  ```
  ```html
  <h1>Hello {{ name }}</h1>
  ```
- **Sending variables from the browser**:
  - Enter `/greet/YourName` in the browser.
- **Converting path variables into data types**:
  - Specify data types in the route:
    ```python
    @app.route('/numbers/<int:num>')
    def numbers(num):
        return render_template("numbers.html", num = num)
    ```
    ```html
    <h1>
      {% if num % 2 == 0 %}
        This {{ num }} is even.
      {% else %}
        This {{ num }} is odd.
      {% endif %}
    </h1>
    ```
---

### 5 - Static Files

- **Linking Static Files**:
  - Flask serves static files (CSS, images) from the `static` folder.
  - Example: Linking a CSS file to an HTML template.
- **Project Structure**:
  - Use separate folders for `static` files and `templates` for better organization.
- **Setting up static files**:
  - Create a folder named `static` and add your CSS, images, and JavaScript files.
- **Linking the static files into templates**:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  <img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
  ```
