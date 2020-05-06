# help macguyver to escape
little game create with pygame in python 3.

third project of openclassrooms in cours developtment in python.

## Development
### Requirements
* python 3.7 (suggest using
  [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
* [SocketLabs Server](https://www.socketlabs.com/signup/)

### Install and Run the Site Locally
1. Clone and change to the directory:

    ```sh
    git clone git@github.com:mozilla/fx-private-relay.git
    cd fx-private-relay
    ```

2. Create and activate a virtual environment:

    ```sh
    virtualenv env
    source env/bin/activate
    ```

3. Install requirements:

    ```sh
    pip install -r requirements.txt
    ```

4. Copy `.env` file for
   [`decouple`](https://pypi.python.org/pypi/python-decouple) config:

    ```sh
    cp .env-dist .env
    ```

5. Add a `SECRET_KEY` value to `.env`:

    ```ini
    SECRET_KEY=secret-key-should-be-different-for-every-install
    ```

6. Migrate DB:

    ```sh
    python manage.py migrate
    ```

7. Create superuser:

    ```sh
    python manage.py createsuperuser
    ```

8. Run it:

    ```sh
    python manage.py runserver
    ```
