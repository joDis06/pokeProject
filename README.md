# pokeProject
The final project for Fall Semester of the 2023-2024 school year of Stuyvesant High School's 9th Period Software Development class.

Goal: To create a functional pokedex (a database of Pokemon (fictional creatures of the franchise of their namesake) which includes various information sourced from pokeapi.co, including such information such as statistics, appearance, and "types" (similar to elemental affinities)) including all Pokemon that have been introduced in the game so far (as of 11.01.2024, the latest update to the national Pokedex is "The Indigo Disk" DLC for Pokemon Scarlet and Violet), with filters to sort pokemon based on factors such as type and generation (definition: arbitrary periods of time categorizing when a given pokemon was introduced). 

The website has the ability to store "teams" of up to 6 pokemon of your choosing, from all of the pokemon currently contained in the Pokedex. 

Upon cloning, please set up your python environment using the provided requirements_env folder by typing "python -m venv env_3.11.5" and then pasting the following into the terminal:

pip install --upgrade pip-tools pip setuptools wheel
pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in
pip-sync requirements_env/main.txt requirements_env/dev.txt

After this, please update your secrets.json file located in pokedexPlus/pokedexPlus/ with your database name, username, password, and host.

Once the database is linked, please run "python manage.py makemigrations" and then "python manage.py migrate."
