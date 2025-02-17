# Resume Parser API

## Overview

The Resume Parser API is a FastAPI-based application that provides functionalities for extracting ranking criteria from job descriptions and scoring resumes against specified criteria. It uses LLM(currently supports only Gemini) to analyze and evaluate resumes, providing a streamlined approach to the recruitment process.

## Features

- Extract ranking criteria from job descriptions
- Score multiple resumes against specified criteria
- Generate Excel reports with candidate scores

## Prerequisites

- Python 3.12.2
- pip

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/kailashsp/resume_parser.git
   cd resume_parser
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `example.env` to `.env`
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Running the Application

To start the API server:

```
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`

## Usage

### Extracting Ranking Criteria

POST `/extract-criteria`

Upload a job description file (PDF, DOCX, or TXT) to extract ranking criteria.

### Scoring Resumes

POST `/score-resumes`

Upload multiple resume files and provide criteria to score them against. The API will return an Excel file with the scores.

## Project Structure

```
resume_parser/
├── app/
│   ├── routers/
│   │   ├── ranking_criteria.py
│   │   └── resume_scoring.py
│   ├── utils/
│   │   ├── file_processing.py
│   │   ├── llm_integration.py
│   │   └── llm_processing.py
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── .gitignore
├── example.env
└── requirements.txt
```

## Contributing

Contributions to the Resume Parser API are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request

## License

[MIT License](LICENSE)

## Contact

For any queries or support, please open an issue in the GitHub repository.
