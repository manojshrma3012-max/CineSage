# LangChain Structured Outputs

This project is part of my LangChain learning journey.

## What I am learning

* Prompt Templates
* ChatPromptTemplate
* Pydantic models
* Structured outputs
* `with_structured_output()`
* LangChain chains
* Basic Streamlit integration
* Using Gemini with LangChain
* Managing dependencies with uv

## Project

This application takes a paragraph about a movie and extracts structured JSON information from it.

The movie information is represented using a Pydantic model containing:
* Title
* Release year
* Genre
* Director
* Plot

The basic flow is:

Movie paragraph → Prompt Template → Gemini → Structured Output → Pydantic Object → JSON

## Folder Structure

```text
Lang-Tutorial/
│
├── app.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Running the project

Install dependencies :

```bash
uv sync
```

Run the Streamlit application:

```bash
uv run streamlit run app.py
```

The `.env` file contains the API key and should not be committed to GitHub.

This repository is mainly for learning and experimenting with LangChain concepts.
