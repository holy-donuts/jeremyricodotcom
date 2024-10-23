sudo kill all gunicorn;
gunicorn -c /var/www/jeremyricodotcom/config/gunicorn/dev.py;
sudo systemctl reload nginx;
