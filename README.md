# AirBnB Console
This project is about to create a command interpreter to manage AirBnB objects. This is the first step to build our AirBnB clone.
## Console
**What is a command interpreter?**
	It's a program where the user can type commands to manage the objects of the project.
In the console, we can, for example:
 - Create a new object (ex: new User or a new Place)
 - Retrieve an object from a file, a database, etc.
 - Do operation on objects (count, compute stats, etc)
 - Update attributes of an object
 - Destroy an object

## Install
To install in your terminal:

    git clone https://github.com/gallit0/holbertonschool-AirBnB_clone

To execute:

    ./console.py

## How to use
First we have to create an object, for example:

    (hbnb) create BaseModel
    d69473b5-d3c6-41ec-abaf-5c13230c3828
When we create an object, will be printed the object's id

Then we can show the object created:

    (hbnb) show BaseModel d69473b5-d3c6-41ec-abaf-5c13230c3828
    [BaseModel] (d69473b5-d3c6-41ec-abaf-5c13230c3828) {'id': 'd69473b5-d3c6-41ec-abaf-5c13230c3828',
    'created_at': datetime.datetime(2022, 10, 16, 17, 14, 42, 725158),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 14, 42, 725158)}

Destroy the object:

    (hbnb) destroy BaseModel d69473b5-d3c6-41ec-abaf-5c13230c3828
