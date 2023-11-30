# cognixus_todo
Build for cognixus job assessment

This is assessment project build with Python Django, with following requirement:

1. Sign in using google oauth2 authentication
2. Add a TODO item.
3. Delete a TODO item.
4. List all TODO items.
5. Mark a TODO item as completed.

This application is dockerize, the application can be bring up by execute <code>docker compose up</code> in root directory. 

The application is set to run at http://localhost:8000/ .

<h1>Admin Site</h1>
Django Admin Site can be access via http://localhost:8000/admin/ , with 

username: admin

password: admin

<h1>Test Case</h1>

1. User need to access to http://localhost:8000/auth/login/google-oauth2/ to perform google oauth2 login
2. Login with any email
3. Upon success login will load a page, showing your Authorization token and all the API curl command accordingly.
4. Keep in mind to replace any variable bounded with <>.

<h1>Database/Model Scheme</h1>
# TodoItem Model

## Fields

- **id**: `IntegerField`
  - *Description*: Primary key for the TodoItem.

- **taskName**: `CharField`
  - *Description*: The name of the task.
  - *Constraints*: Maximum length of 255 characters.

- **taskDescription**: `TextField`
  - *Description*: Detailed description of the task.

- **completed**: `BooleanField`
  - *Description*: Indicates whether the task is completed or not.

