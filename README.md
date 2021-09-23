# GCP-Mini-App-Engine
App Engine Project created to study for the Google Associate Cloud Engineer certification. 

There are two different types of environments for app engine: flexible and standard. Please see this [documentation](https://cloud.google.com/appengine/docs/the-appengine-environments) for their differences.

# [GCP App Engine Documentation](https://cloud.google.com/python/django/appengine)
Each GCP project can be associated with one App Engine project. You can have multiple services for a given project (each service will have an app.yaml file which configures your app engine settings). Make sure app engine is initalized by running `gcloud app create` (which will require you to select your preferred region).

Once created, in the root folder of the app (the same directory as the manage.py file), create an app.yaml file which acts as the configuration file 
for AppEngine. For a list of all the parameters the app.yaml file could have, view the GCP documentation [here](https://cloud.google.com/appengine/docs/standard/python3/config/appref?authuser=2).

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
You can migrate traffic to a version either immediately or gradually. 

