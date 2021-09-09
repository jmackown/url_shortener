# url-shortener

## Contents
1. [Run](#run)
1. [Develop](#develop)
1. [Test](#test)
1. [To do](#to-do)
1. [Improvements](#improvements)
1. [License](#license)

## Run

Pre-requisites: `docker`, `postman` (optional)

* clone the repo
* `cd url_shortener`
* `docker-compose build`
* `docker-compose run`

The API should be available on [http://0.0.0.0:8004/](http://0.0.0.0:8004/)

Check out an existing link to see it in action: [http://0.0.0.0:8004/OjrHZTlVDa](http://0.0.0.0:8004/OjrHZTlVDa)

For more examples, import the Postman collection in `url_shortener/docs`

## Develop
*caveat - only tested on a Mac!*

Pre-requisites: `python 3.9`

* clone the repo
* `cd url_shortener`
* create a virtual environment `python3 -m venv venv`
* `pip3 install -r url_api/requirements.txt`
* run the tests: `python3 -m pytest` (they should all pass!)
* install the pre-commit hooks: `pre-commit install`
* write some code!

## Test
## To Do

- [x] add an example link
- [x] add postman suite and instructions
- [ ] add basic web page to enter new url
- [ ] add OpenAPI docs

## Improvements

## License


**url-shortener** © [Jennifer Mackown](https://github.com/jmackown). Released under the [MIT](./LICENSE) license.<br>
Authored and maintained by Jennifer Mackown.