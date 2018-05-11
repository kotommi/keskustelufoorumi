# Installation
```
git clone https://github.com/kotommi/keskustelufoorumi.git # Download the project
cd keskustelufoorumi
python3 -m venv venv # Create a new virtual environment
source venv/bin/activate # Activate the venv
pip install -r requirements.txt # Download the project dependencies
python3 run.py # Start the app locally. localhost:5000
(Optional) ./populate_db_local.sh # Add some test data to the app
```

Remember to remove the testadmin line from `__init__.py`.

## Heroku
Check out the Heroku dev center for instructions on how to migrate an existing app there. You need a Postgresql database from them too. The app is configured to work there without any modifications to the code.

 

