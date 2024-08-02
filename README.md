# Protoman

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/GrepAutomation/protoman.git
    cd protoman
    ```

2. **Create a Virtual Environment and Activate It**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. **Open the Browser and Navigate to** `http://127.0.0.1:5000`

## Project Structure

- `templates/`: Contains the HTML template for file upload.
- `uploads/`: Directory to store uploaded PDF files.
- `refrigeration_systems.xlsx`: Excel file with refrigeration system mappings.
- `app.py`: Main application file.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Setup and usage instructions.
