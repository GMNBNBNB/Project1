# Product Management API with Flask

This is a simple product management system built with Flask that allows you to create, retrieve, update, and delete products using product names as unique identifiers. The project features an in-memory database, HTML forms for interaction, and a table to display all products on the frontend.

## Features

- **Create Product**: Add new products with a unique name, description, and price.
- **Get Product**: Retrieve product details by entering the product name.
- **Update Product**: Modify the product's description and price using the product name.
- **Delete Product**: Remove a product from the system using the product name.
- **View All Products**: Displays all products in a table on the homepage.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML + CSS
- **In-Memory Data Store**: Python dictionary for storing product information (no external database)

## Project Structure

```bash
your_project/
├── app.py             # Main Flask application
└── templates/
    └── index.html     # HTML file containing the UI
```

## Setup Instructions

### Prerequisites
- **Python 3.x** installed on your system.
- **pip** (Python package installer) for managing dependencies.

### Installation

1. Clone the repository (or download the project files):

    ```bash
    git clone https://github.com/GMNBNBNB/Project1.git
    cd Project1
    ```

2. Install Flask:

    ```bash
    pip install Flask
    ```

## Running the Application

1. Start the Flask app:

    ```bash
    python main.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to interact with the application.

## How to Use

### Creating a Product
1. Enter the product name, description, and price in the "Create Product" form.
2. Click the "Create Product" button.
3. The product will be added to the in-memory data store and will appear in the product table below.

### Getting a Product
1. Enter the product name in the "Get Product" form.
2. Click the "Get Product" button.
3. The product details will be displayed on the page.

### Updating a Product
1. Enter the product name and the new description and/or new price in the "Update Product" form.
2. Click the "Update Product" button.
3. The product's information will be updated in the in-memory data store.

### Deleting a Product
1. Enter the product name in the "Delete Product" form.
2. Click the "Delete Product" button.
3. The product will be removed from the in-memory data store and the product table.

## Known Limitations
- The data is stored in memory (a Python dictionary), so it will be lost when the server is restarted. For persistent storage, a database would be required.
- Product names must be unique; duplicate names are not allowed.
