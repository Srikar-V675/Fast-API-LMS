# Commands

## Poetry - Python Package Manager
### **Steps**
> step 1: go to directory of your wish
<br>
step 2: terminal `poetry new <project name>`
<br>
step 3: set poetry to create env in project dir -> terminal `poetry config virtualenv.in_project true`
<br>
step 4: terminal `poetry install` -> creates env in project folder and activates env
<br>
step 5: to install required packages -> terminal `poetry add <package name>`

### **Commands**
>`poetry add -D <package name>` -> install dev dependencies

## Alembic - DB Migrations Manager
### **Steps**
> step 1: terminal `alembic init <folder name>` -> <folder name> name of folder inside project dir
<br>
step 2: go to `alembic.ini` file and update line -> `sqlalchemy.url = <your DB URL>`
<br>
step 3: got to `env.py` file inside the alembic folder -> <br> 
add lines: `from db.db_setup import Base` <br> 
modify line: `target_metadata = Base.metadata`
<br>
step 4: terminal `alembic revision --autogenerate` -> code will be generated if not add lines, if incorrect please modify

### **Commands**

`alembic upgrade head` -> to upgrade migrations or changes made, for first time initialises the DB
<br>
`alembic downgrade base` -> to downgrade to previous versions/migrations
<br>
`alembic revision --autogenerate -m "<message>"` -> to autogenerate migration command after changes in models of DB

