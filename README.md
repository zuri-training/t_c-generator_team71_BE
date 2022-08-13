# Overview
This is the backend repo for team 71's terms and conditions and privacy policy generator.
This project makes use of the REST Architecture using Django Rest Framework
## Dependencies
- Python - ideally any version from 3.6 [Get Python](https://www.python.org/)
- Django
- You should have knowledge of django rest framework, API creation, serialization etc
## Environment Variables
The Major environment variables include:
- EMAIL - for all django email processes - Kindly retrieve the email details from team71's team lead
- EMAIL_PASSWORD - password for the email
- SECRET_KEY - django secret key
- POSTGRES_USER - the user created for the postgres database
- POSTGRES_PASSWORD - the password created for the postgres database
## Folder Structure
+--+
| |+p_p This folder/app contains all the logic for generating privacy policies
+--+
| |+staticfiles This folder contains all the staticfiles
| |+t_c This folder/app contains all the logic for generating terms and conditions
+--+
| |+terms_gen_home This is the main project folder that contains project settings, urls and configurations
+--+
| |+users This folder/app contains all the logic for the accounts/authorizations/permissions.
## Starting the project
- Fork and clone the repo
- create and activate virtual environment [Guide](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).
- Install requirements - `pip install -r requirements.txt `
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py runserver to run the server`

## Testing the endpoints
- /api/ to test with the swagger ui doc or / 
### Testing with a frontend client
- Go to the [settings.py](/terms_gen_home/settings.py)
- Add your frontend url to the 'CORS_ALLOWED_ORIGINS' list
- The project makes use of jwt authentication, make sure you are familiar with how to handle jwt authentication
## app descriptions
- **p_p** module holds the privacy policy application and all endpoints and work required for the privacy policy should only be done in there
- **t_c** module holds the terms and conditions application and all endpoints and work required for the terms and conditions should only be done in there
- **users** module holds the users/auth application and all endpoints and work required for the users should only be done in there