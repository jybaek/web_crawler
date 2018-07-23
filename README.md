[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# crawler
Program pieces.
 
## Summary 
Space for collecting used crawlers.

* [torrent](torrent/)
* [OAuthGoogle](OAuthGoogle/)
* [facebook](fb_post/)

## Usage
The `chromedriver` must be installed by default.
```
$ python crawler.py -h
usage: crawler.py [-h] [--chromedriver CHROMEDRIVER] [--site SITE] [--id ID]
                  [--passwd PASSWD]

optional arguments:
  -h, --help            show this help message and exit
  --chromedriver CHROMEDRIVER
                        Location of chromedriver.
  --site SITE           Your website address.
  --id ID               Your site ID.
  --passwd PASSWD       Your site password.
```
 
## License
[MIT](LICENSE)
