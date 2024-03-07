# InsightEduBack
Backend for the project InsightEdu (AP5 project)


# How to start Project

Install all packages
Create VENV
pip install -r requirements=.txt
activate : .\env\Scripts\activate

Then install packahes -> requirement.t


API CRUD pour l'application Flask
=============================

Cette documentation décrit les différentes routes et méthodes HTTP disponibles pour interagir avec l'API CRUD de l'application Flask.

Routes
------

### Récupérer tous les utilisateurs

**Méthode HTTP:** GET

**URL:** `/utilisateurs`

**Description:** Renvoie la liste de tous les utilisateurs.

**Réponse:**

* **Code de statut:** 200 OK
* **Contenu:** Liste d'objets JSON représentant les utilisateurs. Chaque objet contient les propriétés suivantes:
	+ `id`: identifiant unique de l'utilisateur
	+ `nom`: nom de l'utilisateur
	+ `prenom`: prénom de l'utilisateur
	+ `email`: adresse e-mail de l'utilisateur
	+ `userType`: type de l'utilisateur

**Exemple de réponse:**
```css
[    {        "id": 1,        "nom": "Dupont",        "prenom": "Jean",        "email": "jean.dupont@example.com",        "userType": "admin"    },    {        "id": 2,        "nom": "Durand",        "prenom": "Pierre",        "email": "pierre.durand@example.com",        "userType": "user"    }]
```
### Récupérer un utilisateur par son ID

**Méthode HTTP:** GET

**URL:** `/utilisateurs/<int:user_id>`

**Description:** Renvoie l'utilisateur correspondant à l'identifiant spécifié.

**Paramètres:**

* `user_id`: identifiant unique de l'utilisateur à récupérer.

**Réponse:**

* **Code de statut:** 200 OK
* **Contenu:** Objet JSON représentant l'utilisateur. L'objet contient les propriétés suivantes:
	+ `id`: identifiant unique de l'utilisateur
	+ `nom`: nom de l'utilisateur
	+ `prenom`: prénom de l'utilisateur
	+ `email`: adresse e-mail de l'utilisateur
	+ `userType`: type de l'utilisateur

**Exemple de réponse:**
```json
{
    "id": 1,
    "nom": "Dupont",
    "prenom": "Jean",
    "email": "jean.dupont@example.com",
    "userType": "admin"
}
```
### Ajouter un nouvel utilisateur

**Méthode HTTP:** POST

**URL:** `/utilisateurs`

**Description:** Ajoute un nouvel utilisateur à la base de données.

**Paramètres:**

* Les données de l'utilisateur doivent être envoyées dans le corps de la requête au format JSON avec les propriétés suivantes:
	+ `nom`: nom de l'utilisateur (requis)
	+ `prenom`: prénom de l'utilisateur (requis)
	+ `email`: adresse e-mail de l'utilisateur (requis)
	+ `password`: mot de passe de l'utilisateur (requis)
	+ `userType`: type de l'utilisateur (requis)

**Réponse:**

* **Code de statut:** 201 Created
* **Contenu:** Objet JSON contenant un message de confirmation.

**Exemple de réponse:**
```json
{
    "message": "Nouvel utilisateur ajouté"
}
```
### Mettre à jour un utilisateur

**Méthode HTTP:** PUT

**URL:** `/utilisateurs/<int:user_id>`

**Description:** Met à jour les informations de l'utilisateur correspondant à l'identifiant spécifié.

**Paramètres:**

* `user_id`: identifiant unique de l'utilisateur à mettre à jour.
* Les données de l'utilisateur doivent être envoyées dans le corps de la requête au format JSON avec les propriétés suivantes:
	+ `nom`: nom de l'utilisateur (requis)
	+ `prenom`: prénom de l'utilisateur (requis)
	+ `email`: adresse e-mail de l'utilisateur (requis)
	+ `password`: mot de passe de l'utilisateur (requis)
	+ `userType`: type de l'utilisateur (requis)

**Réponse:**

* **Code de statut:** 200 OK
* **Contenu:** Objet JSON contenant un message de confirmation.

**Exemple de réponse:**
```json
{
    "message": "Utilisateur mis à jour"
}
```
### Supprimer un utilisateur

**Méthode HTTP:** DELETE

**URL:** `/utilisateurs/<int:user_id>`

**Description:** Supprime l'utilisateur correspondant à l'identifiant spécifié.

**Paramètres:**

* `user_id`: identifiant unique de l'utilisateur à supprimer.

**Réponse:**

* **Code de statut:** 200 OK
* **Contenu:** Objet JSON contenant un message de confirmation.

**Exemple de réponse:**
```json
{
    "message": "Utilisateur supprimé"
}
```
Erreurs
-------

### Utilisateur non trouvé

**Code de statut:** 404 Not Found

**Contenu:** Objet JSON contenant un message d'erreur.

**Exemple de réponse:**
```json
{
    "message": "Utilisateur non trouvé"
}
```
### Erreur d'authentification

**Code de statut:** 401 Unauthorized

**Contenu:** Objet JSON contenant un message d'erreur.

**Exemple de réponse:**
```json
{
    "message": "Erreur d'authentification"
}
```
### Erreur d'autorisation

**Code de statut:** 403 Forbidden

**Contenu:** Objet JSON contenant un message d'erreur.

**Exemple de réponse:**
```json
{
    "message": "Erreur d'autorisation"
}
```
### Erreur interne du serveur

**Code de statut:** 500 Internal Server Error

**Contenu:** Objet JSON contenant un message d'erreur.

**Exemple de réponse:**
```json
{
    "message": "Erreur interne du serveur"
}
```


# API Documentation pour les routes d'authentification

Cette documentation décrit les différentes routes et méthodes HTTP disponibles pour l'authentification de l'utilisateur dans l'application.

## Endpoints

### Login

`POST /login`

Cette route permet à l'utilisateur de se connecter à l'application en envoyant son email et son mot de passe dans le corps de la requête au format JSON.

#### Request

Le corps de la requête doit contenir les champs suivants :

| Champ | Type | Description |
| --- | --- | --- |
| email | string | L'email de l'utilisateur |
| password | string | Le mot de passe de l'utilisateur |

#### Response

Si la requête est valide et que l'utilisateur est authentifié avec succès, le serveur renvoie une réponse avec un code de statut 200 et un objet JSON contenant l'access token.

Exemple de réponse :
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDQ3NjA2MjYsImV4cCI6MTY0NDg0NzQyNiwiYXVkIjoiZXhhbXBsZS5jb20iLCJqdGkiOiI1NTk5ZjE5Mi1iYmRhLTQ2ZjYtYWY1MS0zYjE1Zjg2YWZiNmQiLCJpc3MiOiJodHRwczovL2xvZ2luLmNvbSIsInN1YiI6ImF1dGhvcjEyMy5jb20iLCJwcnYiOiIyM2UwYWYxZWY5ZmQzNTgxMmQwMWI0MDA4NzJkYjdmNTk3NzU0NzU0In0.28iDf6KZrQhZlKC24bJYj67Mf8k2EH4kJ9V-6r4554U"
}
```
Si la requête est invalide, le serveur renvoie une réponse avec un code de statut approprié et un message d'erreur.

Exemples de réponses d'erreur :

* Email manquant :
```vbnet
Email is missing
```
* Utilisateur non trouvé :
```vbnet
User not found
```
* Mot de passe incorrect :
```
incorrect Password
```
### Logout

`POST /logout`

Cette route permet à l'utilisateur de se déconnecter de l'application en révoquant l'access token.

#### Request

Le header de la requête doit contenir un access token valide.

#### Response

Si la requête est valide et que l'access token est révoqué avec succès, le serveur renvoie une réponse avec un code de statut 200 et un message de confirmation.

Exemple de réponse :
```json
{
  "msg": "Access token revoked"
}
```
Si la requête est invalide, le serveur renvoie une réponse avec un code de statut approprié et un message d'erreur.

### Signup

`GET /signup`

Cette route affiche la page d'inscription.

#### Response

Si la requête est valide, le serveur renvoie une réponse avec un code de statut 200 et le contenu de la page d'inscription.

Exemple de réponse :
```
signupPage
```
### Refresh expiring JWTs

Cette méthode est appelée après chaque requête pour vérifier si l'access token est sur le point d'expirer et de renvoyer un nouveau token si nécessaire.

#### Response

Si l'access token est sur le point d'expirer, le serveur renvoie une réponse avec un nouveau token dans l'objet JSON.

Exemple de réponse :
```json
{
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDQ3NjA2MjYsImV4cCI6MTY0NDg0NzQyNiwiYXVkIjoiZXhhbXBsZS5jb20iLCJqdGkiOiI1NTk5ZjE5Mi1iYmRhLTQ2ZjYtYWY1MS0zYjE1Zjg2YWZiNmQiLCJpc3MiOiJodHRwczovL2xvZ2luLmNvbSIsInN1YiI6ImF1dGhvcjEyMy5jb20iLCJwcnYiOiIyM2UwYWYxZWY5ZmQzNTgxMmQwMWI0MDA4NzJkYjdmNTk3NzU0NzU0In0.28iDf6KZrQhZlKC24bJYj67Mf8k2EH4kJ9V-6r4554U"
  }
}
```
Si l'access token n'est pas sur le point d'expirer, le serveur renvoie la réponse d'origine.


# SQL

La base de données utilisée pour cette application est MySQL. Voici les différentes tables utilisées dans l'application :

## Table `utilisateurs`

La table `utilisateurs` stocke les informations sur les utilisateurs de l'application. Voici la structure de la table :
```sql
CREATE TABLE `utilisateurs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(255) NOT NULL,
  `prenom` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `userType` VARCHAR(255) NOT NULL,
  `token` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
);
```
## Table `token_blocklist`

La table `token_blocklist` stocke les jetons d'authentification révoqués pour empêcher leur réutilisation. Voici la structure de la table :
```sql
CREATE TABLE `token_blocklist` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `jti` VARCHAR(36) NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jti` (`jti`)
);
```
## Table `competences`

La table `competences` stocke les informations sur les compétences disponibles dans l'application. Voici la structure de la table :
```sql
CREATE TABLE `competences` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nomCompetence` VARCHAR(255) NOT NULL,
  `idGroupeCompetences` INT DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```
## Table `competencesutilisateurs`

La table `competencesutilisateurs` stocke les informations sur les compétences associées à chaque utilisateur, ainsi que leur niveau d'avancement. Voici la structure de la table :
```sql
CREATE TABLE `competencesutilisateurs` (
  `idUtilisateur` INT NOT NULL,
  `idCompetence` INT NOT NULL,
  `avancementCompetences` INT NOT NULL,
  PRIMARY KEY (`idUtilisateur`, `idCompetence`),
  CONSTRAINT `fk_competencesutilisateurs_utilisateurs`
    FOREIGN KEY (`idUtilisateur`)
    REFERENCES `utilisateurs` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_competencesutilisateurs_competences`
    FOREIGN KEY (`idCompetence`)
    REFERENCES `competences` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
```