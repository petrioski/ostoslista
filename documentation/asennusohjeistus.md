# Asennusohjeet

## Paikallinen asennus

1. Lataa sovellus githubista ja luo hakemistossa virtuaaliympäristö komennolla `python -m venv venv` ja aktivoi se komennolla `source venv/bin/activate`.

1. Päivitä tarvittaessa pip komennolla `pip install --upgrade pip` ja lataa virtuaaliympäristöön sovelluksen tarvitsemat riippuvuudet komennolla `pip install -r requirements.txt`.

1. Käynnistä lopuksi sovellus komennolla `python run.py`

1. Löydät nyt sovelluksen osoitteesta http://127.0.0.1:5000/

## Heroku-asennus

Suorita vaiheet 1 ja 2 kuten paikallisessa asennuksessa on kuvattu. Sovelluksessa on riippuvuuksissa mukana Herokun tarvitsemat komponentit, joten sinun tarvitsee vain luoda sovellukselle osoite ja ensimmäinen käyttäjä herokuun seuraavasti:

1. Jos sinulla ei ole vielä Herokun komentorivi-työkalua käytössäsi, niin lataa se [täältä](https://devcenter.heroku.com/articles/heroku-cli) löytyvien ohjeiden mukaan

1. Luo sovellukselle osoite `heroku create <sovelluksen-nimi>`

1. Lisää versionhallintaan tieto Herokusta `git remote add heroku https://git.heroku.com/<sovelluksen-nimi>.git`

1. Lisää ja kommittoi sovellus ensin gitiin `git add .` ja `git commit -m "Initial commit"` komennoilla ja pushaa sovellus nyt myös Herokuun komennolla `git push heroku master`

1. Luo sovelluksen käyttöön ympäristömuuttuja herokuun komennolla
`heroku config:set HEROKU=1`.

1. Luo Herokuun sovellukselle tietokanta komennolla `heroku addons:add heroku-postgresql:hobby-dev`

1. Luo Herokun tietokantaan ensimmäinen käyttäjä

    ```bash
    heroku pg:psql
    INSERT INTO account (name, username, password) VALUES ('hello world', 'hello', 'world');
    \q
    ```

1. Löydät sovelluksen nyt osoitteesta `https://<sovelluksen-nimi>.herokuapp.com/`
