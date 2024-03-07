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