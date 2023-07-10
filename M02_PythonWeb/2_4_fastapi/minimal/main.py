import fastapi
import uvicorn

# initialize a web application based on FastAPI
app = fastapi.FastAPI()


# create a GET endpoint
@app.get("/")  # decorator: app.<request_method>
def hello():
    return {"message": "hello world"}


@app.post("/")  # not accessible from browser URL bar
def hello_post():
    return {"message": "hello world post"}


# Custom path. Must always start with forward slash (/)
@app.get("/users") # equal to http://127.0.0.1:8000/users
def get_all_users():
    return [
        {"id": 1, "name": "User 1"}
    ]

"""
Defining an endpoint:
```
@app.<request_method>("<path_start_with_fwd_slash>")
def <function_name>():
    ...
```

Running a FastAPI app:
```
uvicorn main:app --reload
```
"""

"""
Ex1: Create an endpoint:
* Path: /random
* Method: GET
* What it does: Generate and return a random number in a dictionary.
The response should look like the following:
```
{
  "number": 100
}
``` 
"""

"""
Ex2: Create an endpoint:
* Path: /counter
* Method: POST
* What it does: Given a global variable named `counter`;
each time this endpoint is called, increment the counter by 1.
Then return the counter in a dict like the following:
```
{
  "counter": 3
}
```
"""

if __name__ == "__main__":
    uvicorn.run("main:app")
