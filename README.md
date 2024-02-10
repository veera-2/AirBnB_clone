AirBnB Clone

Description of the project:
The goal of the project is to deploy on your server a simple copy of the AirBnB website using my server. 

The final version of this project will have:

A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
A website (front-end) with static and dynamic functionalities
A comprehensive database to manage the backend functionalities
An API that provides a communication interface between the front and backend of the system.

General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function


What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object


Description of the command interpreter

Commands                  Description

quit                     Quits the console
Ctrl+D                   Quits the console
help or help <command>	Displays all commands or Displays instructions for a specific command
create <class>	Creates an object of type , saves it to a JSON file, and prints the objects ID
show <class> <ID>	Shows string representation of an object
destroy <class> <ID>	Deletes an objects
all or all <class>	Prints all string representations of all objects or Prints all string representations
                        of all objects of a specific class
update <class> <id>     Updates an object with a certain attribute (new or existing)
<attribute name> "
<attribute value>"
<class>.all()	        Same as all <class>
<class>.count()	        Retrieves the number of objects of a certain class
<class>.show(<ID>)	Same as show <class> <ID>
<class>.destroy(<ID>)	Same as destroy <class> <ID>
<class>.update(<ID>,    Same as update <class> <ID> <attribute name> <attribute value>
<attribute name>,
<attribute value>

<class>.update(<ID>,   Updates an objects based on a dictionary representation of attribute names and values
<dictionary representation>)



A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.
