🌍 [Leia em Português](README.pt-BR.md)

# Crud

Crud for manipulations in oracle database with methods of inserting, updating, capturing and removing data. using the `requests` library in python.

# Technologies Used

- `requests` - Communication with api.
- `pytest` - Testing.
- `oracledb` - Connect with oracle database.
- `python-dotenv` - Load environment variables.
- `flask` - Development of api.
- `flask_cors` - Api CORS configuration.

# Features

- Manipulation of data from a database: Methods of inserting, updating, creating, and removing data using requests.
- Simple and intuitive interface: Simple and entuitive command-line interface for handling a database.
- Dynamic interface, being able to manipulate the table you want!

## Steps to install and run

1. Clone the Repository:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
```

2. Entre no diretório:

```bash
cd palindrometro
```

3. Create `Virtual Environment`:

```bash
python -m venv .venv
```

4. Enable `Virtual Environment` by running the `.bat` file in `.venv/Scripts/activate.bat`.

5. Install dependencies:

```bash
pip install - r requirements.txt
```

6. Run api server:

```bash
python src/api/server.py
```

7. Run the application:

```bash
python src/main.py
```

8. Interact with the menu interface and perform the desired manipulation in the database.

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
