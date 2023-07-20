# Software-Solutions API

## Cow-Feed-Calculator

Docker run:

```
docker run -p 5000:5000 -v /var/www/vhosts/julian-steiner.net/api.julian-steiner.net/history:/app/history/ -v /usr/local/psa/var/modules/letsencrypt/etc/archive/api.julian-steiner.net:/app/letsencrypt/ -e FLASK_CERT=/app/letsencrypt/fullchain1.pem -e FLASK_CERT_KEY=/app/letsencrypt/privkey1.pem -e COWFEEDCALC_HISTORY_DIR=/app/history --rm software-solutions-api
```