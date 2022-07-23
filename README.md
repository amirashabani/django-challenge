# Django-Challenge

To run the program, first make sure you have Python 3.8+ installed on your machine:

```bash
python --version
3.8.13
```

Then, create a virtual environment and install the necessary requirements:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Then, navigate to the `src` directory and create a `.env` file:

```bash
cd src
touch .env
```

Then, populate this file with at least three variables:

```env
SECRET_KEY="your secret key"
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1
```

Then, make migrations and migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

And finally, run the server:

```bash
python manage.py runserver
```

## API endpoints

### Get users

Get a list of users:

```url
/api/get_user
```

Get a list of users, for the admin:

```url
/api/get_user?admin=true
```

Get a list of users and filter based on number of addresses:

```url
# greater than five
/api/get_user?admin=true&addr=gt_5

# greater than or equal to three
/api/get_user?admin=true&addr=gte_3

# less than ten
/api/get_user?admin=true&addr=lt_10

# equal to two
/api/get_user?admin=true&addr=eq_2

# not equal to six
/api/get_user?admin=true&addr=ne_6
```

### Add address

Add address for a specific user:

```url
/api/add_address
```

Example POST request to add an address:

```json
{
    "user": "uid",
    "title": "a new title",
    "latitude": 12.965843,
    "longitude": -120.546238
}
```

You can find the UIDs of users in the /admin page.
