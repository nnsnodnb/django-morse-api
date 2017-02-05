# django-morse-api

## Description

Morse code API

## Request example

```bash
$ curl -X POST \
> -H 'Content-Type: application/json' \
> https://morse.nnsnodnb.moe/api/alphabet \
> -d '{"sentence": "Hello world"}'
```

## Response example

```json
{"sentence":"Hello world","result":[{"morse":["0","0","0","0"],"word":"h"},{"morse":["0"],"word":"e"},{"morse":["0","1","0","0"],"word":"l"},{"morse":["0","1","0","0"],"word":"l"},{"morse":["1","1","1"],"word":"o"},{"morse":[],"word":" "},{"morse":["0","1","1"],"word":"w"},{"morse":["1","1","1"],"word":"o"},{"morse":["0","1","0"],"word":"r"},{"morse":["0","1","0","0"],"word":"l"},{"morse":["1","0","0"],"word":"d"}]}
```

## Author

Yuya Oka (nnsnodnb)
