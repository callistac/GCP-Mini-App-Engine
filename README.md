# GCP-Mini-App-Engine
App Engine Project created to study for the Google Associate Cloud Engineer certification. 

There are two different types of environments for app engine: flexible and standard. Please see this [documentation](https://cloud.google.com/appengine/docs/the-appengine-environments) for their differences.

# [GCP App Engine Documentation](https://cloud.google.com/python/django/appengine)
Each GCP project can be associated with one App Engine project. Make sure app engine is initalized by running `gcloud app create` (which will require you to select your preferred region).

Once created, in the root folder of the app (the same directory as the manage.py file), create an app.yaml file which acts as the configuration file 
for AppEngine. For a list of all the parameters the app.yaml file could have, view the GCP documentation [here](https://cloud.google.com/appengine/docs/standard/python3/config/appref?authuser=2).

### Deploying app
Run the following command in the root of your application:
```
gcloud app deploy
```
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

