# Mergington High School Activities API

A simple FastAPI application that allows students to view and sign up for extracurricular activities. This project is part of the [GitHub Skills: Getting Started with GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot) tutorial.

## Features

- View all available extracurricular activities
- Sign up for activities
- Unregister from activities
- Web interface for easy interaction
- Interactive API documentation

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nvinod-net/skills-getting-started-with-github-copilot.git
   cd skills-getting-started-with-github-copilot
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the development server:

   ```bash
   python src/app.py
   ```

   Or use uvicorn directly:

   ```bash
   uvicorn src.app:app --reload --port 8000
   ```

2. Open your browser and access:
   - **Web Interface**: http://localhost:8000
   - **API Documentation (Swagger)**: http://localhost:8000/docs
   - **API Documentation (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                        |
| ------ | ----------------------------------------------------------------- | ---------------------------------- |
| GET    | `/`                                                               | Redirects to the web interface     |
| GET    | `/activities`                                                     | Get all activities and their data  |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up a student for an activity  |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister a student from an activity |

### Example API Usage

**Get all activities:**
```bash
curl http://localhost:8000/activities
```

**Sign up for an activity:**
```bash
curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=student@mergington.edu"
```

**Unregister from an activity:**
```bash
curl -X DELETE "http://localhost:8000/activities/Chess%20Club/unregister?email=student@mergington.edu"
```

## Data Model

The application uses a simple in-memory data model:

### Activities

Uses activity name as the identifier:

- **description**: String - Brief description of the activity
- **schedule**: String - When the activity takes place
- **max_participants**: Integer - Maximum number of students allowed
- **participants**: Array - List of student email addresses who are signed up

### Available Activities

The application comes pre-loaded with these activities:
- Chess Club
- Programming Class
- Gym Class
- Basketball Team
- Swimming Club
- Art Studio
- Drama Club
- Debate Team
- Science Olympiad

> **Note**: All data is stored in memory and will be reset when the server restarts.

## Testing

Run the test suite using pytest:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src tests/
```

Run a specific test file:

```bash
pytest tests/test_api.py
```

## Project Structure

```
.
├── src/
│   ├── app.py           # Main FastAPI application
│   ├── static/          # Static files (HTML, CSS, JS)
│   │   ├── index.html   # Web interface
│   │   ├── styles.css   # Styles
│   │   └── app.js       # Frontend JavaScript
│   └── README.md        # This file
├── tests/
│   ├── __init__.py
│   └── test_api.py      # API tests
├── requirements.txt     # Python dependencies
├── pytest.ini          # Pytest configuration
└── LICENSE             # MIT License
```

## Development

### Code Style

This project follows standard Python conventions. When contributing:

- Write clear, descriptive variable and function names
- Add docstrings to functions
- Follow PEP 8 style guidelines
- Write tests for new features

### Adding New Activities

To add new activities, modify the `activities` dictionary in `src/app.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Learning Resources

This project is designed for learning GitHub Copilot. For more information:

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Skills](https://skills.github.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
