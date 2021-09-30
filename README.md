# GCP-Mini-App-Engine
App Engine Project created to study for the Google Associate Cloud Engineer certification. 

There are two different types of environments for app engine: flexible and standard. From [GCP documentation](https://cloud.google.com/appengine/docs/flexible/go/flexible-for-standard-users#:~:text=In%20the%20standard%20environment%2C%20your,what%20your%20application%20can%20do.&text=In%20contrast%2C%20the%20flexible%20environment,)%2C%20which%20have%20fewer%20restrictions.):

In the **standard** environment, your application runs on a lightweight instance inside of a sandbox. This sandbox restricts what your application can do. For example, the sandbox only allows your app to use a limited set of binary libraries, and your app cannot write to disk. The standard environment also limits the CPU and memory options available to your application. Because of these restrictions, most App Engine standard applications tend to be stateless web applications that respond to HTTP requests quickly.

In contrast, the **flexible** environment runs your application in Docker containers on Google Compute Engine virtual machines (VMs), which have fewer restrictions. For example, you can use any programming language of your choice, write to disk, use any library you'd like, and even run multiple processes. The flexible environment also allows you to choose any Compute Engine machine type for your instances so that your application has access to more memory and CPU.

Essentially, standard environments should be sufficient for most applications. Flexible environment is meant to be complementary to standard environment, in other words, if a part of your application needs more CPU, you can define a microservice for that particular part that runs in the standard environment. See the bottom of the documentation linked above for more information.

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
Note: you can also split traffic in the console and make sure that both of your versions of the app are have status "serving" (not stopped). 
There are two different types of splitting options, by IP (which is not as precise) or cookie (which is more precise). IP splitting doesn't work if both of your instances have the same target url so it is probably safest to use cookie splitting. 

I was not able to get the above working but made a post about this and still need to try this option -> https://stackoverflow.com/questions/69246432/why-is-my-gcp-app-engine-not-splitting-traffic-correctly

### Migrate Traffic
You can migrate traffic to a version either immediately or gradually and can do so through the gcloud tool or console. 

### Scaling
In your app.yaml file yoou can specify the scaling parameters (i.e. max number of instances to attach to an application to limit costs and min number - which if you set to 0, when your app is not serving requests you will save money because there will be no instances attached). There are many more parameters you can specify in automatic scaling but there is also a basic and manual scaling option as well. See this document for more details:

https://cloud.google.com/appengine/docs/standard/python3/config/appref#automatic_scaling

## [Django Applications](https://cloud.google.com/python/django/appengine#macos-64-bit)
**Note the following instructions are for a standard AppEngine**
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

Tip: Make sure you follow the steps in the "Run the app on your local computer" section CAREFULLY. Open new terminals as suggested and run the app migrations etc. in the terminal you use to create the database etc. 

### Make Django App Production Ready
1. Make sure DEBUG is set to False in mysite/settings.py (so that detailed error messages are not shown)
2. Limit the database user privleges 

### Avoiding charges
1. All versions of an application are billable so make sure to delete versions you no longer want
