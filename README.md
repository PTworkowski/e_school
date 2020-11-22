<h1>E-dukacja</h1>

*A platform supporting students and teachers in online learning.*

# Index:
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [How to](#how-to)
5. [License](#license)




## Installation <a name="installation"></a> 
Use the package manager [git](https://git-scm.com/downloads) to download __E-dukacja__ project.
```sh
git clone https://github.com/PTworkowski/e_school.git
```
Create the virtual environment. At the beginning install it with [pip](https://pip.pypa.io/en/stable/).
```sh
pip install virtualenv
```
Create a new virtual environment _e-school-env_ (the name is arbitrary)
```sh
virtualenv e-school-env
```
Activate the virtual environment

Windows
```sh
.\venv\Scripts\activate.bat
```
or
```sh
.\venv\Scripts\activate
```
Linux & McOS
```sh
source e-school-env/bin/activate
```


Install __requirements.txt__ with python's library.
```sh
pip install -r requariments.txt
```

## Usage <a name="usage"></a> 

Make and run migrations, after that run the server.

Windows
```sh
python migrate.py makemigrations
python migrate.py migrate
python migrate.py runserver
```
Linux & McOS
```sh
python3 migrate.py makemigrations
python3 migrate.py migrate
python3 migrate.py runserver
```

## Contributing <a name="contributing"></a> 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## How to <a name="how-to"></a> 

The platform supports the following sections:
1. Teachers section
2. Students section
3. Administration section



To fully use the platform you must register as a student or a teacher. 
A new administration profile must be accepted by a superuser.

A new user chooses a profile __student__ or __teacher__.


To create a new profile you should provide:
- name
- e-mail
- password

A new user is accepted by the administration. After you are accepted, you can login to your account and update your personal data.

**Status of the platform**

The platform is still under development.

Legend:
- [x] completed functionality
- [ ] in development


***1. Teacher Account***
 - [x] Updating personal data
 - [ ] Accessing Teachers Courses (as a list of assigned groups)
 - [x] Accessing Library
 - [ ] Files browsing, posting into and downloading from the Library
 - [ ] Creating library for each course
 - [x] Adding the links to online classes
 - [ ] Creating tests
 - [ ] Posting and viewing homework content


***2. Student Account***
 - [x] Updating personal data
 - [x] Accessing Course Groups
 - [x] Accessing link to Group Course
 - [ ] Accessing Group’s Library
 - [ ] Viewing homework content
 
 
 ***3. Administration Account*** 
 - [x] Updating personal data
 - [ ] Accepting new users accounts (Teachers and Students)
 - [ ] Managing Payments for students
 - [x] Managing Subjects/Courses
 - [ ] Creating and deleting Subjects
 - [ ] Creating Group Courses
 - [ ] Managing Materials (in Library)
 
 ## License <a name="license"></a>
 [MIT](./LICENSE.rm)