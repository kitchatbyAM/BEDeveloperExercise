# BEDeveloperExercise
Check the environment for Python, Nginx and Docker Installations before proceeding.
Create a folder on Desktop named Assignment and clone the project in that folder.
Change the Directory locations and replace the name akanksha with your ubuntu machine username in the following files:
 a. Assignment-> docker-compose.yml
 b. Assignment-> BEproject-> Dockerfile
 c. Assignment-> nginx-> nginx.conf
 
Once above steps are done:

cd to the Assignment folder where you have cloned the project.

Create a virtual env in the Assignment folder and activate it.:

  $ python3.8 -m venv env
  $ source env/bin/activate  

Run the following commands in the given order:

$ docker-compose -f docker-compose.prod.yml up -d --build

$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

username: "beprojectuser"
pass: "1234pass"
//leave email blank for now.

After the above steps are done, you can the website at http://localhost:1337  , 
Admin is available at http://localhost:1337/admin  ,
The list of tasks will be available at http://localhost:1337/tasks/   ,
Login on the page using the superuser credentials.

To test using the python script:

Back to cmd, in the Assignment folder run:

python3 script1.py

It should show all the operations with the results.....



 
