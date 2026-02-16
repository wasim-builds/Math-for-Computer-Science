# Math Web Application

This is a Flask-based web application that provides interactive tools and content for the Math for Computer Science repository.

## 🌟 Features
*   **Topic Reader**: Read all the markdown notes (Calculus, Probability, etc.) directly in the browser.
*   **RSA Encryption Tool**: Generate keys, encrypt, and decrypt secret messages.
*   **Limit Calculator**: Calculate limits of functions.
*   **Derivative Calculator**: Find symbolic derivatives.
*   **Distribution Plotter**: Visualize the Normal Distribution.

## 🚀 How to Run

1.  **Navigate to the web_app directory:**
    ```bash
    cd web_app
    ```

2.  **Install dependencies (if not already installed):**
    ```bash
    pip install flask sympy numpy matplotlib markdown
    ```

3.  **Run the Flask App:**
    ```bash
    python3 app.py
    ```

4.  **Open in Browser:**
    Go to `http://127.0.0.1:5000/`

## 📂 Structure
*   `app.py`: The main Flask application (Backend).
*   `templates/`: HTML templates using Bootstrap 5 (Frontend).
*   `static/`: CSS and JS files.
