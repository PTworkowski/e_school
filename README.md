<h1>E-dukacja</h1>

*E-Learning platform to organization online classes.*

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
Create virtual environment. In beginning install this with [pip](https://pip.pypa.io/en/stable/).
```sh
pip install virtualenv
```
Create new virtual environment _e-school-env_ (name is arbitrary)
```sh
virtualenv e-school-env
```
Activate virtual environment

Windows
```sh

```
Linux & McOS
```sh
source e-school-env/bin/activate
```


Install __requirements.txt__ with pythons library.
```sh
pip install -r requariments.txt
```

## Usage <a name="usage"></a> 

Create migrations of models data base and running the server

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

The platform support section of:
1. Teachers
2. Students
3. Administration



To full using the platform must you registration as student or teacher. 
New administration profile should be accepted by superuser.

New user chooses a profile __student__ or __teacher__.


To create new profile should you give:
- name
- e-mail
- password

New user is accepted by administration. After accepted you can login to you account and updating your personal data.


**Status of platform**

Platform in during developing process.


Legend:
- [x] completed functionality
- [ ] in developing


***1. Teacher Account***
- [x] Updating personal data
- [ ] Teachers Access to courses as list od assigned groups
- [x] Access to the library
- [ ] Files browsing, posting and downloading in the library
- [ ] Creating library for each course
- [x] Add the links to online classes
- [ ] Creating the tests
- [ ] Possibility to post and view homework content



***2. Student Account***
- [x] Updating personal data
- [x] Access to own course groups
- [x] Access to link on group course
- [ ] Access to group library
- [ ] Possibility to view homework content


***3. Administration Account***  
- [x] Updating personal data
- [ ] Accepted new users accounts (teachers and students)
- [ ] Payment Management of students
- [ ] Subjects management
- [ ] Create new Subjects and deleting Subjects
- [ ] Create new course groups
- [ ] Files Management




## License <a name="license"></a> 
[MIT](./LICENSE.rm)