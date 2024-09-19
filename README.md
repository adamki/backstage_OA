# General

### Requirements
[X] You should use Python3.6+ and Django.

[X] I should be able to install your service by doing: pip install -r requirements.txt. Please include a README with instructions for launching it.

[X] I should be able to query your service at the following (or similar) endpoint:

[X] localhost:8000/difference?number=n where n is any integer greater than 0 and less than or equal to 100.

[X] Your service should emit a JSON object(omitted)

[X] [OPTIONAL]Type Hinting

[X] [OPTIONAL]Unit tests

---

# Setup:

### 1. Clone the Repository

To get started, clone this repository:

```bash
git clone git@github.com:adamki/backstage_OA.git
cd backstage_OA
```


### 2. Ensure Python version of 3.6 or higher

### 3. Create a Virtual Environment (Recommended)

```
python3 -m venv <dir>

source <dir>/bin/activate #Unix
<dir>\Scripts\activate    #Windows
```

### 4. Upgrade and install requirements.txt

```
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Build Migrations/Migrate the Database

```
python3 manage.py makemigrations
python3 manage.py Migrate
```

### 6. Run the Development Server

```
python manage.py runserver
```

Your app is running at `http://localhost:8000/`


### 7. Other commands

Run tests

```
pytest
```

Auto-Format

```
black8 .
```

---


## API Endpoint/Usage

- **Route**: `{BASE_URL}/difference`
- **Params**: "n" is valid and required
- **Example Usage**: `http://localhost:8000/difference?n=100`

### Sample API Response

**GET** `/difference?n=<n>`

```json
{
    "datetime": "2024-09-19T03:56:14.110Z",
    "value": 4,
    "number": 2,
    "occurrences": 12,
    "last_datetime": "2024-09-19T03:56:14.108Z"
}
```
