# GCP-Mini-App-Engine
App Engine Project created to study for the Google Associate Cloud Engineer certification. 

There are two different types of environments for app engine: flexible and standard. Please see this [documentation](https://cloud.google.com/appengine/docs/the-appengine-environments) for their differences.

# [GCP App Engine Documentation](https://cloud.google.com/python/django/appengine)
Each GCP project can be associated with one App Engine project. You can have multiple services for a given project (each service will have an app.yaml file which configures your app engine settings). Make sure app engine is initalized by running `gcloud app create` (which will require you to select your preferred region).

Once created, in the root folder of the app (the same directory as the manage.py file), create an app.yaml file which acts as the configuration file 
for AppEngine. For a list of all the parameters the app.yaml file could have, view the GCP documentation [here](https://cloud.google.com/appengine/docs/standard/python3/config/appref?authuser=2).
## General AppEngine Tips
### Deploying app
Run the following command in the root of your application:
```
gcloud app deploy --version 1
```
If you do not want this version of the app to be the default version, add the `--no-promote` flag


### Accessing your app
You can open the deployed app by typing:
```
gcloud app browse
```

### Making changes to app
Make edits to your code and then run the `gcloud app deploy` command again which will create a new version of your app and promotes it to the default version. All versions of the app are stored and are billable (so delete non-default versions of app to reduce costs).

### Splitting Traffic
To split traffic for your app (i.e. you can split traffic between different versions of your app for A/B testing), run:
```
gcloud app services set-traffic [MY_SERVICE] --splits [MY_VERSION1]=[VERSION1_WEIGHT],[MY_VERSION2]=[VERSION2_WEIGHT] --split-by [IP_OR_COOKIE]
```
Note: make sure that both of your versions of the app are have status "serving" (not stopped). 
There are two different types of splitting options, by IP (which is easier but not as precise) or cookie (which is more precise but more difficult).

I was not able to get the above working but made a post about this and still need to try this option -> https://stackoverflow.com/questions/69246432/why-is-my-gcp-app-engine-not-splitting-traffic-correctly

### Migrate Traffic
You can migrate traffic to a version either immediately or gradually and can do so through the gcloud tool or console. 

## Django Applications
Django applications use a backend SQL database to store GET requests made to your application (i.e. a user entering their name in a form etc.). When deploying a Django app using AppEngine, you will also need to create a Cloud SQL instance. You also need to allow Django to have information on your database credentials (username / password) and so instead of hardcoding that info in your Django app, you can use Secret Manager.

Perform the following steps:
1. Create a SQL database (preferably PostgreSQL because Django supports it the most)
2. Create a database within your PostgreSQL instance
3. Create a user within the database (including username / password)
4. Use Secret Manager to store your username / password so that AppEngine / Django have access
5. Run your Django app locally `gcloud app deploy`
6. Deploy the app to AppEngine
7. Access the app using `gcloud app browse or through` the console
8. To make changes, edit the source code and then run `gcloud app deploy` again 

https://cloud.google.com/python/django/appengine#macos-64-bit
For some reason when I try to deploy the app (one of the final steps) it does not woork for me... I get an error:	
```
could not connect to server: Connection refused
	Is the server running locally and accepting
	connections on Unix domain socket "/cloudsql/luminous-bazaar-326123:us-central:db-instance/.s.PGSQL.5432"?`
```
I think what happened is that I wasn't running the server locally anymore so check to see if this is the problem! 
