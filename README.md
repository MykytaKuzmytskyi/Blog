# Blog
Virtual blog, for creating articles, and the possibility of commenting on them with cascading display.

## Running the program locally

1. Clone the source code:

```bash
git clone https://github.com/MykytaKuzmytskyi/Blog.git
cd Blog
```

2. Install modules and dependencies:

```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

3. `.env_sample` 
This is a sample .env file for use in local development.
Duplicate this file as .env in the root of the project
and update the environment variables to match your
desired config. You can use [djecrety.ir](https://djecrety.ir/)

4. Use the command to configure the database and tables:

```bash
python manage.py migrate
```

5. Start the app:

```bash
python manage.py runserver
```

Use the following command to load prepared data from fixture to test and debug code:

```bash
python manage.py loaddata fixture_data.json
```
Use the following command to load prepared data from fixture to test and debug your code:

- You can use following superuser (or create another one by yourself using the admin page):
    - Login: `admin.user`
    - Password: `Us2ddTX7`

### Run with docker

Docker should be installed

```commandline
docker-compose up --build
```

### Getting access

- You can use following superuser (or create another one by yourself):
    - Login: `admin.user`
    - Password: `Us2ddTX7`
- get access token via /api/token/
