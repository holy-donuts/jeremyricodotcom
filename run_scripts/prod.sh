sudo kill all gunicorn;
gunicorn -c /var/www/jeremyricodotcom/config/gunicorn/prod.py;
sudo systemctl reload nginx;
