# Test backend Cornershop

Rabbitmq was used like broker to send Async Slack messages

![Alt text](broker.png?raw=true "Cornershop test Rabbitmq")


Flow

![Alt text](flow.png?raw=true "Flow")


Webhooks Slack

![Alt text](webhook_slack.png?raw=true "Webhook Slack")

Message send by worker to Slack channel #almuerzo

![Alt text](mensajes_slack.png?raw=true "Mensajes Slack")


Documentations API
**Documentation url:** http://localhost:8000/swagger-docs/

![Alt text](swagger_documentation.png?raw=true "Swagger Documentation")

# API

## Menu

**Create Menu:** http://localhost:8000/api/v1/menu/create/{user_id}

* method: POST

* Request

https://localhost/menu/user/0

```json
{
    "date_menu":"2022-01-21",
    "options": [
        {
            "menu": 1,
            "option": 1,
            "description": "Tacos al pastor"
        },
        {
            "menu": 1,
            "option": 2,
            "description": "Alambre cubano"
        },
        {
            "menu": 1,
            "option": 3,
            "description": "Quesadillas"
        },
        {
            "menu": 1,
            "option": 4,
            "description": "Hamburguesa a la mexicana"
        }
    ]
}
```
* Response
```json
{
    "id": 51,
    "uuid": "7993c67c-8cfd-11ec-a446-705681b4b5a7",
    "date_menu": "2022-01-21"
}
```

**List Menu:** http://localhost:8000/api/v1/menu

* method: GET

* Request

http://localhost:8000/api/v1/menu

* Response
```json
[
    {
        "id": 1,
        "uuid": "37ed954c-8b84-11ec-be1a-705681b4b5a7",
        "date_menu": "2022-12-12"
    },
    {
        "id": 2,
        "uuid": "dd870bb4-8b84-11ec-9baf-705681b4b5a7",
        "date_menu": "2022-12-12"
    },
    {
        "id": 3,
        "uuid": "6e9915de-8b85-11ec-9862-705681b4b5a7",
        "date_menu": "2022-01-21"
    },
    {
        "id": 4,
        "uuid": "8881ce82-8bbc-11ec-9d22-705681b4b5a7",
        "date_menu": "2022-01-21"
    }
]
```

**Get Menu:** https://localhost/api/v1/menu/{uuid}

* method: GET

* Request

http://localhost:8000/api/v1/menu/8881ce82-8bbc-11ec-9d22-705681b4b5a7

* Response
```json
{
    "id": 51,
    "uuid": "7993c67c-8cfd-11ec-a446-705681b4b5a7",
    "menu_date": "2022-01-21",
    "options": [
        {
            "menu": 1,
            "option": 1,
            "description": "Tacos al pastor"
        },
        {
            "menu": 1,
            "option": 2,
            "description": "Alambre cubano"
        },
        {
            "menu": 1,
            "option": 3,
            "description": "Quesadillas"
        },
        {
            "menu": 1,
            "option": 4,
            "description": "Hamburguesa a la mexicana"
        }
    ]
}
```


## Option

**Create Option:** https://localhost/api/v1/menu/create/menuoptions/{user_id}

* method: POST

* Request

http://localhost:8000/api/v1/menu/create/menuoptions/0

```json
{
	"menu": 1,
	"option" : 1,
	"description": "Carne enchilada muuucho chileee"
}
```
* Response
```json
{
    "menu": 1,
    "option": 1,
    "description": "Carne enchilada muuucho chileee"
}
```

**Update Option:** http://localhost:8000/api/v1/menu/update/menuoptions/{user_id}

* method: PUT

* Request

http://localhost:8000/api/v1/menu/update/menuoptions/1

```json
{
	"menu": 1,
	"option" : 1,
	"description": "Pastel enchiladoo "
}
```
* Response
```json
{
    "menu": 1,
    "option": 1,
    "description": "Pastel enchiladoo"
}
```


## User

**Create User:** http://localhost:8000/api/v1/user/

* method: POST

* Request

http://localhost:8000/api/v1/user/

```json
{
    "id": 4,
    "name": "Pepe",
    "username": "psuarez",
    "email": "pepe@gmail.com"
}
```
* Response
```json
{
    "id": 7,
    "name": "Pepe",
    "username": "psuarez",
    "email": "pepe@gmail.com"
}
```

**Get User:** http://localhost:8000/api/v1/user/{user_id}

* method: GET

* Request

http://localhost:8000/api/v1/user/7

* Response
```json
{
    "id": 7,
    "name": "Pepe",
    "username": "psuarez",
    "email": "pepe@gmail.com"
}
```


## Order

**Create Order:** http://localhost:8000/api/v1/menuuser/{user_id}

* method: POST

* Request

http://localhost:8000/api/v1/menuuser/1

```json
{
	"menu": 1,
	"menu_option": 1,
	"quantity": 2,
	"specification": "Con queso extraaaaaa"
}
```
* Response
```json
{
    "message": "Order create successfully",
    "order": "Carne enchilada",
    "specification": "Con queso extraaaaaa",
    "order_date": "2022-02-13"
}
```

**Get Orders:**http://localhost:8000/api/v1/menuuser/list/{user_id}

* method: GET

* Request

http://localhost:8000/api/v1/menuuser/list/1

* Response
```json
[
    {
        "specification": "Con queso extraaaaaa",
        "option": "Carne enchilada",
        "menu_option": 3,
        "quantity": 2,
        "order_date": "2022-02-13",
        "username": "Enrique",
        "user_id": 1
    }
]
```
