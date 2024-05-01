from fastapi import FastAPI

from DB.db_setup import engine
from DB.Models import user, course

user.Base.metadata.create_all(bind = engine)
course.Base.metadata.create_all(bind = engine)

from API import users, courses, sections

app = FastAPI(
    title="Fast API LMS",
    description="API for managing students and courses in a LMS",
    version="0.1.0",
    contact={
        "name": "Srikar",
        "email": "srikar@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)