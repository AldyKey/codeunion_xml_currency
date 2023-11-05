
# Currency Scraper

Scrape currencies from http://www.nationalbank.kz/rss/rates_all.xml and 
update the currency rates in the database with specified 
regularity.

## Requirements: ##
- Docker
- Python 3.11 (If you want to run the project without Docker)

## Technologies used: ##
- Python
- Django
- DRF
- Docker

## Installation

Clone the repository

```bash
  git clone https://github.com/AldyKey/codeunion_xml_currency.git
```

 - #### Inside the codeunion_xml_currency folder create .env file ####

 - #### Copy the inside of .env_example file and paste it inside .env ####

#### Build the docker containers: ####

  ```
  docker-compose build
  ```

#### Start the Docker containers: ####

  ```
  docker-compose up -d --build 
  ```

#### Run migrations inside the Docker container: ####

  ```
  docker exec -it currency_scraper python3 manage.py migrate
  ```

#### Access the django server at: ####

  ```
  http://0.0.0.0:8000/
  ```
#### How to stop the Docker containers: ####

  ```
  docker-compose down
  ```

## API Reference

#### Register

```http
  POST /api/v1/users/register/
```

| Body              | Type     | Description       |
|:------------------| :------- |:------------------|
| `username`        | `string` | **Required**.     |
| `password`        | `string` | **Required**.     |
| `password_repeat` | `string` | **Required**.     |
| `first_name`      | `string` | **Not Required**. |
| `last_name`       | `string` | **Not Required**. |
| `email`           | `string` | **Not Required**. |


#### Login

```http
  POST /api/v1/users/login/
```

| Body       | Type     | Description                      |
|:-----------| :------- | :------------------------------- |
| `username` | `string` | **Required**. |
| `password` | `string` | **Required**. |

**Response:**

```json
{
  "access_token": "ey.......",
  "type": "Bearer"
}
```

#### Get Currencies

```http
  GET /api/v1/currencies/
```

| Parameter      | Type     | Description       |
|:---------------| :------- |:------------------|
| `access_token` | `string` | **Required**.     |
| `page`         | `string` | **Not Required**. |
| `per_page`     | `string` | **Not Required**. |


**Response:**

```json
[
    {
      "id": 1,
      "name": "USD",
      "rate": 465.01,
      "updated_at": "2023-11-05 10:56:17.382913+00:00"
    }
]
```

#### Get Currency

```http
  GET /api/v1/currencies/currency/${id}/
```

| Parameter | Type     | Description                      |
|:----------| :------- | :------------------------------- |
| `access_token` | `string` | **Required**.     |
| `id`      | `string` | **Required**. |

**Response:**

```json
{
  "id": 1,
  "name": "USD",
  "rate": 465.01,
  "updated_at": "2023-11-05 10:56:17.382913+00:00"
}
```

## Management Commands

- List all the currencies from the database

```bash
  docker exec -it currency_scraper python3 manage.py get_all_currencies
```

- Update currencies rate by ID

```bash
  docker exec -it currency_scraper python3 manage.py update_currency
```

## Running Tests

To run tests on currency app, run the following command

```bash
  docker exec -it currency_scraper python3 manage.py test apps.currency.tests
```

To run tests on user app, run the following command

```bash
  docker exec -it currency_scraper python3 manage.py test apps.user.tests
```
