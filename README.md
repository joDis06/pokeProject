# pokeProject
The final project for Fall Semester of the 2023-2024 school year of Stuyvesant High School's 9th Period Software Development class.

Goal: To create a functional pokedex (a database of Pokemon (fictional creatures of the franchise of their namesake) which includes various information sourced from pokeapi.co, including such information such as statistics, appearance, and "types" (similar to elemental affinities)) including all Pokemon that have been introduced in the game so far (as of 11.01.2024, the latest update to the national Pokedex is "The Indigo Disk" DLC for Pokemon Scarlet and Violet), with filters to sort pokemon based on factors such as type and generation (definition: arbitrary periods of time categorizing when a given pokemon was introduced). 

The website has the ability to store "teams" of up to 6 pokemon of your choosing, from all of the pokemon currently contained in the Pokedex. 

Upon cloning, please set up your python environment using the provided requirements_env folder by typing "python -m venv env_3.11.5" and then pasting the following into the terminal:

pip install --upgrade pip-tools pip setuptools wheel;
pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in;
pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in;
pip-sync requirements_env/main.txt requirements_env/dev.txt;

After this, please update your secrets.json file located in pokedexPlus/pokedexPlus/ with your database name, username, password, and host.

Once the database is linked, please run "python manage.py makemigrations" and then "python manage.py migrate."

To run the server, run "python manage.py runserver".

When you run the server you will first be sent to the homepage at "localhost:8000".

To use the applications "teamMaker" and "teamStats" properly, click on "pokedex" first and allow the site to load the pokemon. 
If you do not do this first and click teamMaker or teamStats prior to loading the pokemon, they will display a blank form and no buttons (on the two apps, respectively).

It will take around 5 minutes to load the pokemon, give or take with your computer & connection, but once the list of pokemon has loaded, you are free to use the other two apps as you wish, TeamMaker & teamStats.

For teamMaker:
You select up to 6 pokemon to make a team with the checkboxes to form a team, each with their own id.

For teamStats:
For each team that has been created, there will be a link to the team's url, as well as a button underneath to choose it for comparison. The teams you compare are chosen by the order of clicking the buttons-- 1st button clicked is the first team being compared, the 2nd button is the second team, regardless of the team's id. 

