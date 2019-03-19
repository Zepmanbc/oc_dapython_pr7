# Analyse Fonctionnelle

## User Stories

* **En tant que** utilisateur **je veux** poser une question **afin que** Papy Robot me réponde
* **En tant que** utilisateur **je veux** utiliser un langage courant **afin que** le dialogue semble le plus réaliste possible
* **En tant que** développeur **je veux** afficher une plan google map **afin que** la réponse soit visuelle
* **En tant que** développeur **je veux** afficher un message issue de Wikipedia **afin que** la réponse soit plus complète
* **En tant que** développeur **je veux** utiliser le TDD **afin de** pouvoir faire de l'intégration continue
* **En tant que** développeur **je veux** que les questions et les réponses se déroulent sans chargement de nouvelle page **afin que** l'expérience utilisateur soit la plus naturelle et agréable

## Règles fonctionnelles

L'application est dans un navigateur web. l'utilisateur utilise un formulaire pour poser sa question et valide avec la touche [Enter].

Sans recharger la page, les questions et les réponses s'enchainent à la maniére d'une messagerie instantanée.

La question est analysée à partir de mots clés afin de réaliser une recherche via l'API de Google Map afin de récuperer une adresse un plan et une autre recherche via l'API de Wikimedia afin de récupérer le 1er paragraphe correspondant à l'adresse trouvée.

Si la recherche ne donne pas de résultat concluant, un message indiquant que la demande n'est pas claire est renvoyée à l'utilisateur.

## Acteurs système

![Acteurs du système](img/01_actors.png)

## Décomposition du système

![Diagramme de pakages](img/02_packages.png)

## Cas d'utilisation

![Cas d'utilisation "question"](img/03_UC_question.png)

![Cas d'utilisation "answer"](img/03_UC_answer.png)

![Cas d'utilisation "information"](img/03_UC_information.png)

## Cycle de vie
![Diagramme d'activité"](img/04_activity.png)

## Description du domaine fonctionnel

![Diagramme de classes"](img/05_class.png)

## Description des composants du système

![Diagramme de composants](img/06_component.png)

## Déploiement

![Diagramme de déploiement](img/07_deployment.png)