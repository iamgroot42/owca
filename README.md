# hci_crx
HCI Course Project


### Deploying on Heroku

* Remember to set environment flags:

`heroku config:set FLASK_APP=backend`


## On windows (PowerShell)

`$env:FLASK_APP = "backend"`
`$env:FLASK_ENV = "development"`
`flask run`

=====================

# For mail server

`python mail_server.py` from inside `flask_app` directory


=====================

# To get password hash for a given name

`python make_password.py <NAME>` 
