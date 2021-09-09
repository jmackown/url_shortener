# url-shortener

## Contents
1. [Run](#run)
1. [Develop](#develop)
1. [Test](#test)
1. [To do](#to-do)
1. [Improvements](#improvements)
1. [License](#license)

## Run

Pre-requisites: `docker`

* clone the repo
* `cd url_shortener`
* `docker-compose build`
* `docker-compose run`

The API should be available on [http://0.0.0.0:8004/](http://0.0.0.0:8004/sdfssd)


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

- [ ] add postman suite and instructions

## Improvements

## License


**url-shortener** © [Jennifer Mackown](https://github.com/jmackown). Released under the [MIT](./LICENSE) license.<br>
Authored and maintained by Jennifer Mackown.