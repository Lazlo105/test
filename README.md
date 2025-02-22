# Profile Page with Flask

## Description
This project is a simple personal profile page built with HTML and CSS, served using the Flask framework in Python. The application supports static file serving and dynamic rendering using `render_template`. It also includes a redirect from the default route (`/`) to `/profile`.

## Features
- **Frontend:** A static profile page with an image, contact details, education, skills, work experience, and achievements.
- **Backend:** Flask-based web application to serve the profile page.
- **Static File Serving:** Images and CSS files are served as static resources.
- **Redirection:** The root URL (`/`) redirects to `/profile`.

## Project Structure
```
project/
│── static/
│   ├── css/
│   │   ├── main.css
│   ├── imgs/
│   │   ├── Ee5ojPVfTis.jpg
│── templates/
│   ├── index.html
│── app.py
│── README.md
```

## Installation and Setup
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd project
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install flask
   ```
4. Run the application:
   ```sh
   python app.py
   ```
5. Open a browser and go to:
   ```
   http://127.0.0.1:5000/profile
   ```

## Profile Page (index.html)
- Displays the user's name, profile picture, contact info, education, skills, work experience, and achievements.
- Uses a structured layout with a sidebar and main content area.

## Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** Python, Flask

## Deployment
The profile page is available at: [https://lazlo105.github.io/](https://lazlo105.github.io/)

## Validation
The page has successfully passed validation using "Markup Validation Service".

## Author
**Aleksandr Chumakov**
- Contact: sasha.chumakov.2002@gmail.com

## License
This project is open-source and available for modification and redistribution.


