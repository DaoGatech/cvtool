# Project: Sample Flask/React App

### Install

This project requires **Python 2.7** and the following libraries installed:

- [Nodejs](https://nodejs.org/en/) for frontend development and package management
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) for deployment

In a terminal or command window, navigate to the top-level project directory(that contains this README) and run the following commands:

```bash
pip install -r requirements
npm install
```  

### Build 

Now we can build the static assets with gulp:

```bash
gulp
```  

Rerun gulp when you change the frontend code. Make sure to clear the browser cache.

### Run

Run locally with :

```bash
python app.py
``` 

### Deploy:

You can create a new Heroku app and set it as the remote with git.
The Heorku git url can be found under the settings tab.
Once the remote is set, you can deploy the app.
Create a second heroku app also, to test the heroku staging if you want.

```bash
git remote add heroku <your_herkoku_app_url>
git remote add heroku-staging <your_staging_app_url>
``` 

Push the app to the Heroku remote:

```bash
git push heroku master:master
``` 

If you have a staging branch you can push the staging branch to your staging 
app with the following:

```bash
git push heroku-staging staging:master
``` 


