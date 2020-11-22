# OWCA
HCI Course Project: Team [OWCA](https://phineasandferb.fandom.com/wiki/Organization_Without_a_Cool_Acronym)

<hr/>

#### Deploying on Heroku

Remember to set environment flags:

`heroku config:set FLASK_APP=backend`

<hr/>

### On windows (PowerShell)

`$env:FLASK_ENV = "development"`
<br>
`python wsgi.py`

<hr/>

### For mail server

`python mail_server.py`

<hr/>

### To get password hash for a given name

`python make_password.py <NAME>` 
