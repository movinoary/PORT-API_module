# API MODULE

I created this API to make it easier for me to create something on various websites that I will create. So just call the API, no need to copy-paste from the previous code. Make the repo that will be created minimalist. Here I use python as the programming language and flask as the framework.

## Tech Stack

**Programming Language:** Python
**Library Framework:** Flask

## Running

run it with the following code

#### `flask --app main run --debug --port 5020`

## Pengguan API

Development Path

#### `http://127.0.0.1:5010`

Production Path

#### `http://127.0.0.1:5010`

### Route API

| Parameter | Methods | Parameter                              |
| :-------- | :------ | :------------------------------------- |
| /uuid     | POST    | create a UUID according to what I want |
| /encode   | POST    | translate base64 as i want             |
| /decode   | POST    | create base64 as i want                |

## Curl

/uuid

```bash
curl --location --request POST 'http://127.0.0.1:5010/api/v-1/uuid/GEO'
```

/encode

```bash
curl --location 'http://127.0.0.1:5010/api/v-1/encode' \
--header 'Content-Type: application/json' \
--data '{
  "encode": "VOSSO-3010-ALJPB-82468HW-BVZDMSDJ6O-S9CAH"
}'
```

/decode

```bash
curl --location 'http://127.0.0.1:5010/api/v-1/decode' \
--header 'Content-Type: application/json' \
--data '{
  "decode": "QUFBQVZnQUFBRThBQUFCVEFBQUFVd0FBQUU4QUFBQXRBQUFBTXdBQUFEQUFBQUF4QUFBQU1BQUFBQzBBQUFCQkFBQUFUQUFBQUVvQUFBQlFBQUFBUWdBQUFDMEFBQUE0QUFBQU1nQUFBRFFBQUFBMkFBQUFPQUFBQUVnQUFBQlhBQUFBTFFBQUFFSUFBQUJXQUFBQVdnQUFBRVFBQUFCTkFBQUFVd0FBQUVRQUFBQktBQUFBTmdBQUFFOEFBQUF0QUFBQVV3QUFBRGtBQUFCREFBQUFRUUFBQUVnPQ=="
}
'
```

## Authors

- [@movinoary](https://github.com/movinoary?tab=repositories)
