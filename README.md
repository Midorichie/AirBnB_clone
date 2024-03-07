Airbnb Clone - The console


Table of Content
#Background Context
#The console
#Installation
#Execution
#Usage
#Authors
#Background-Context
#Welcome to the AirBnB clone project!.

This project represents a significant milestone as it marks the first step towards building a full web application – the AirBnB clone. This initial phase is crucial because it lays the foundation for the entire project, including HTML/CSS templating, database storage, API, and front-end integration.

- The console
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Installation
Git clone the repository https://github.com/Midorichie/AirBnB_clone.git

Navigate to the cloned repository

- Execution
The console works like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
- Usage
Type the help command to see how to use to navigate the console.

(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of all instances based or not on the class name.

(hbnb)

- Authors
Hammed Yakub hamsohood@gmail.com
Oluwatobiloba Otun bamidurooluwatobiloba@gmail.com 
