# Orange Website in Django Installation Guide

This guide provides step-by-step instructions to set up the Orange Website project, built using Django framework, on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (3.x recommended)
- Git
- pip package manager

## Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MD-Jafor-Sadek-Khan/Orange-Website-in-Django.git
   cd Orange-Website-in-Django
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   # Activate the virtual environment
   source venv/Scripts/activate   # For Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Website:**
   Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the Orange Website.

## Additional Steps (If Applicable)

- **Pillow Installation:**
  If you encounter errors related to Pillow during migrations, install Pillow using the following command:
  ```bash
  python -m pip install Pillow
  ```

- **Beautiful Soup Installation:**
  If you encounter errors related to Beautiful Soup during migrations, install Beautiful Soup using the following command:
  ```bash
  python -m pip install beautifulsoup4
  ```

## Usage

- To stop the development server, press `CTRL + BREAK`.
- Use `deactivate` command to exit the virtual environment when you're done.

## Support

If you encounter any issues or have questions, feel free to reach out to me at [rksadeck@gmail.com](mailto:rksadeck@gmail.com).
