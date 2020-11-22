# OWCA
HCI Course Project: Team [OWCA](https://phineasandferb.fandom.com/wiki/Organization_Without_a_Cool_Acronym)

<hr/>

#### Deploying on Heroku

* Remember to set environment flags:

`heroku config:set FLASK_APP=backend`


### On windows (PowerShell)

`$env:FLASK_APP = "backend"`
`$env:FLASK_ENV = "development"`
`flask run`

<br/>

### For mail server

`python mail_server.py` from inside `flask_app` directory

<hr/>

### To get password hash for a given name

`python make_password.py <NAME>` 
