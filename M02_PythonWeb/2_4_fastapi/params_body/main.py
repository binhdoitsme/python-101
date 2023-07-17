"""
Handling request parameters & body

Previously, we have succeeded in creating simple FastAPI endpoints with GET and POST.
Sometimes, parameter-less may not be enough to create highly usable APIs.
Therefore, web frameworks allow the usage of paramters in several ways:
- As a `query parameter`, e.g.: GET /students?id=1&name=MrA
- As a `path variable`, e.g.: GET /students/:studentId as spec and GET /students/1 as the actual request
- Inside `request body`. There are several types of request body:
  - JSON
  - form-data
  - ... and many more, but these two are the most commonplace
- Request body DOES NOT SUPPORT GET method

Among these types:
- `Path variables` mostly allow for retrieval of or operation on one item based on its ID
- `Query parameters` allow the search for multiple items that satisfy a **small** set of conditions
- `Request body`, when used for searching, allow search for multiple items that satisfy a more **complex** set of conditions
- `Request body` may also be used for updating and creating items

First of all we will look at the usage of these parameters in building an item searching API endpoint.
"""

from typing import Optional
import fastapi
import uvicorn

# initialize a web application based on FastAPI
app = fastapi.FastAPI()

"""Our code comes between the declaration of `app` and the call to `uvicorn`"""

# Assume we have a list of students
students = [
    {"id": 1, "name": "Student A", "dob": "2002-01-01", "hometown": "Ha Noi"},
    {"id": 2, "name": "Student B", "dob": "2002-05-01", "hometown": "HCM"},
    {"id": 3, "name": "Student C", "dob": "2002-05-17", "hometown": "Nam Dinh"},
    {"id": 4, "name": "Student D", "dob": "2002-03-12", "hometown": "Ha Nam"},
]


# We can return all students
@app.get("/all_students")
def get_students():
    return students


# Let's use path variable to find student by ID
@app.get(
    "/students/{id}"  # <----- notice this `id`, you can replace `id` with any other name
)
def get_student_by_id(
    id: int,  # <----- notice the variable name, it must match the declaration of the path on the prev line
):
    for student in students:
        if student["id"] == id:
            return student  # if found, return the student with the given ID
    # what if we are unable to find any student with that ID?
    # ---> here comes `404 NOT FOUND`
    return fastapi.Response(
        status_code=fastapi.status.HTTP_404_NOT_FOUND, content="Not Found"
    )


# if we need to find student by other criteria, it is possible to use query parameters
@app.get("/students")
def find_students(
    # Below are the query parameters.
    # we can call the API: GET /students?name=Student%20A&hometown=Ha%20Noi
    name: Optional[
        str
    ] = None,  # Optional[] means it may be omitted when calling the endpoint
    hometown: Optional[str] = None,
):
    print(f"finding students matching hometown={hometown} and name={name}")
    results = []
    for s in students:
        # if parameter is omitted we will match all items
        matches_name = s["name"] == name or name is None
        matches_hometown = s["hometown"] == hometown or hometown is None
        if matches_hometown and matches_name:
            results.append(s)
    return results


# Optional[str] = str | None = Optional<String> (java)

"""-------------------------------------------------------------------------"""

# call uvicorn so that we can run this file directly
if __name__ == "__main__":  # if called from `python main.py`
    uvicorn.run("main:app", reload=True)
