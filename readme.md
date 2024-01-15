
STEPS TO RUN

1) copy the .env file in the email to the root folder of project
2) open cmd prompt
3) docker-compose up --build
4) project should be running at http://0.0.0.0:8000
5) Use the register endpoint to register a new user
6) login using the login api using the credentials provided in previous step
7) copy the access token from the previous response
8) on top of the page find a Authorize Button and click on it
9) it opens a text box 
10) Bearer < paste your access token from step 7>
11) you are now authenticated
12) you can use all the API's
13) if the token gets expired
    - copy the refresh token from the login api
    - use token/refresh api to generate new access token and replace the token in the above authorize button