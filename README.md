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
**Create object**

    (hbnb) create BaseModel
    d69473b5-d3c6-41ec-abaf-5c13230c3828
When we create an object, will be printed the object's id

**Show the object created:**

    (hbnb) show BaseModel d69473b5-d3c6-41ec-abaf-5c13230c3828
    [BaseModel] (d69473b5-d3c6-41ec-abaf-5c13230c3828) {'id': 'd69473b5-d3c6-41ec-abaf-5c13230c3828',
    'created_at': datetime.datetime(2022, 10, 16, 17, 14, 42, 725158),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 14, 42, 725158)}

**Destroy the object:**

    (hbnb) destroy BaseModel d69473b5-d3c6-41ec-abaf-5c13230c3828
**Print all objects**

    (hbnb) all
    ["[BaseModel] (0135da68-c890-4c15-914a-93b76227a136) {'id': '0135da68-c890-4c15-914a-93b76227a136',
    'created_at': datetime.datetime(2022, 10, 16, 17, 25, 40, 174903),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 25, 40, 174903)}",
    "[BaseModel] (f9c8b49f-4519-4b94-8d01-d1859af88431) {'id': 'f9c8b49f-4519-4b94-8d01-d1859af88431',
    'created_at': datetime.datetime(2022, 10, 16, 17, 25, 45, 369075),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 25, 45, 369075)}"]

    (hbnb) all BaseModel
    ["[BaseModel] (0135da68-c890-4c15-914a-93b76227a136) {'id': '0135da68-c890-4c15-914a-93b76227a136',
    'created_at': datetime.datetime(2022, 10, 16, 17, 25, 40, 174903),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 25, 40, 174903)}",
    "[BaseModel] (f9c8b49f-4519-4b94-8d01-d1859af88431) {'id': 'f9c8b49f-4519-4b94-8d01-d1859af88431',
    'created_at': datetime.datetime(2022, 10, 16, 17, 25, 45, 369075),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 25, 45, 369075)}"]

**Update an object**

    -   `update <class name> <id> <attribute name> "<attribute value>"`

    (hbnb) update BaseModel 0135da68-c890-4c15-914a-93b76227a136 email "aibnb@mail.com"
    (hbnb) show BaseModel 0135da68-c890-4c15-914a-93b76227a136
    [BaseModel] (0135da68-c890-4c15-914a-93b76227a136) {'id': '0135da68-c890-4c15-914a-93b76227a136',
    'created_at': datetime.datetime(2022, 10, 16, 17, 25, 40, 174903),
    'updated_at': datetime.datetime(2022, 10, 16, 17, 25, 40, 174903),
    'email': '"aibnb@mail.com"'}

