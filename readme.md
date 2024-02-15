# FastAPI Tutorial

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It's easy to use, intuitive, and highly performant. This tutorial will guide you through setting up a virtual environment, installing FastAPI and Uvicorn, and getting started with building your first API.

## Setting Up a Virtual Environment

To create a virtual environment in Python, you can use the built-in `venv` module. Follow the steps below:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to create your virtual environment.

3. Run the following command:

    ```bash
    python -m venv venv
    ```

    This command creates a virtual environment named `venv` in the current directory. Replace `venv` with your preferred name if desired.

## Activating the Virtual Environment

Once the virtual environment is created, you need to activate it to start using it. 

### For Linux/Mac OS:

1. Run the following command:

    ```bash
    source venv/bin/activate
    ```

2. Your terminal prompt should now change to indicate that the virtual environment is active. For example:

    ```bash
    (venv) user@hostname:~/project-directory$
    ```

### For Windows:

1. Run the following command:

    ```cmd
    venv\Scripts\activate
    ```

2. Your command prompt should now change to indicate that the virtual environment is active. For example:

    ```cmd
    (venv) C:\Users\User\project-directory>
    ```

## Installing FastAPI and Uvicorn

Now that your virtual environment is active, you can install FastAPI and Uvicorn using pip:

```bash
pip install fastapi uvicorn
