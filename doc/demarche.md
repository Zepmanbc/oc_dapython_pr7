# Créez GrandPy Bot, le papy-robot 🤖 👴

Github : https://github.com/Zepmanbc/oc_dapython_pr7

Trello : https://trello.com/b/Wh1dkH9n/ocdapythonpr7

Lien Heroku : https://bc-ocdapythonpr7.herokuapp.com/

[Analyse Fonctionnelle](analyse_fonctionelle.md)

# Démarche

## Front

Réalisation d'une maquette pour la version écran d'ordinateur et de smartphones.

![version ordinateur](front/version_ordi.png)

![version smartphone](front/version_mobile.png)

[version ordinateur format GIMP](front/version_ordi.xcf)

[version smartphone format GIMP](front/version_mobile.xcf)

## Déploiement sur Heroku

Création du fichier Procfile

Clonage du repo dans heroku

    heroku git:clone -a bc-ocdapythonpr7

pour pousser le projet vers heroku

    git push heroku master

## Flask et le TDD

définir une liste de phrases à tester:

* Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?
* où se trouve l'Arc de Triomphe?
* Quelle est l'adresse de la Tour Eiffel?
* Dis Papy, c'est quoi l'adresse de l'Elysée?
* Tu connais l'adresse de l'Opéra Garnier?


## API Google Map et Wikimedia

Création de l'identifiant sur https://console.cloud.google.com

Création de la variable d'environnement dans l'environnement virtuel

    pipenv shell
    echo "GMAPKEY=[PRIVATE_KEY]" >> .env
    echo $GMAPKEY

Création de la variable d'environnement dans Heroku

    heroku config:set GMAPKEY=[PRIVATE_KEY]