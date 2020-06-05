# Smart Campus
----------------
> Backend created with *django* and *django-rest-framework*

**Note:**
There are 4 types of request `["GET", "POST", "PUT", "DELETE"]`


`GET` : The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.

`POST` : The POST method is used to create new data into the database.

`PUT` : The PUT method is used to update existing user data.

`DELETE` : The DELETE method deletes the specified resource.

### API referance for this project
To create a new account as a teacher or student or staff ,
```
request_type = POST
url = http://localhost:8000/api/account/signup/
Content-Type = application/json
```
```json
post_data = {
   "first_name": "",
   "last_name": "",
   "i_am": "student/teacher/staff",
   "email": "",
   "password1": "",
   "password2": ""
}
```
