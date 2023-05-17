Kick Funding API Using Django REST Framework (DRF)

## About the API:

Some Features Of The API For Users :

- Sign-up using addtional fields in model forms ( Such as phone number with validation, Birth date, Profile image and Country ).
- Sign-in using ( Email or Username ).
- Reset their password if they forgot it (They will get an email for resetting ).
- They will login only if they activate thier email ( Mail Activation Feature using sendgrid API ).
- User can also edit his profile ( F&L Name, Phone Number, Country, Profile Image and Birth Date ).
- Create charity and donate money to a specific charity.
- Donations using Stripe API ( Using Visa & Master Card ).
- Delete his charity and also admin can delete it.
- User can also see his last donations.
- Comment on charity.
- Report on charity or any comment for the admin.
- Show charity details and the rate of charity.
- All users can donate all charities and rate them.
- User can remove charity in case the donation of the charity less than 25% of the total.
- Prevent users for donate any charity that has hit its target amount of the money.
- Adding Schemas And Documentation With Swagger UI And Redoc.

## API Built With:

- [Django Framwork]
- [Django REST Framwork]
- [SQlite Database]

## Mobile App Built With:

- Flutter (Android & IOS)

## Installation

- First You Need To Have Python In Your OS
- Pip ( PIP is a package manager for Python packages, or modules if you like )

### Follow Then Next Step Carefully :

    1- Cloning The Repo In New Dir (Empty Dir):

```
[git clone](https://github.com/ahmedesmail07/kickfunding-api-using-rest_framework.git)

```

2- After Cloning The Repo Create Virtual Environment

```
python -m venv (Enter Your VirtualEnv Name)
```

3- Activate Virtual Environment

```
virtualenv name(Your Venv Name)
```

```
Linux : source name(Your Venv Name)/bin/activate
Windows : name(Your Venv Name)/Scripts/activate

```

4- Install Requirments

```

After setting up your vertualenv just use one command to install all this requirements using the following command :
```

        pip install -r requirements.txt

5- Migrate The Models ( Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema) Using The Following Command :

```
    python manage.py migrate
```

6-Run server in django_project dir (That Contains manage.py file)

```

    python manage.py runserver

```

- Don't Forget To Create A Super User

```

    python manage.py createsuperuser

```

- Don't Forget To Change My Specific Mail Provider (SendGrid Settings In settings.py)
- Note That gstmp feature causes some errors so be carefull while using it for prevent yourself from banned from google (if you use it with google) but it works successfully with sendgrid.
