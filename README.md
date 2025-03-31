## Bookstore API

This is a simple bookstore backend built with FastAPI that provides endpoints to retrieve books, get a specific book by ID, and create new books.

### Features

* Get a list of all books

* Retrieve a specific book by ID

* Create a new book entry

### Installation

1. Clone the repoitory

    https://github.com/DeepeshP04/bookstore_fastapi.git

2. Create a virtual environment and activate it:

    python -m venv venv
    venv\Scripts\activate

3. Install dependencies:

    pip install -r requirements.txt

4. Running the Server

    Start the FastAPI server using Uvicorn:
    uvicorn main:app --reload