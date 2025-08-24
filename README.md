
## Installation

To run this project, you'll need to follow these steps:

1. **Clone the Repository**: First, clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/ashish082003/virtual_assistant_chat.git
    ```

2. **Create a Python Virtual Environment**: Navigate to the project directory and create a Python virtual environment. You can do this using `virtualenv` or `venv` (built-in to Python 3):

    ```bash
    cd virtual_assistant_chat
    # Using virtualenv (if installed)
    virtualenv venv
    # or using venv
    python -m venv venv
    ```

3. **Activate the Virtual Environment**: Activate the virtual environment. The commands differ based on your operating system:

    - **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **Unix or MacOS**:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**: Once the virtual environment is activated, install the project dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Now that you have installed the project and its dependencies, you can run the virtual assitant chatbot:

```bash
python app.py
