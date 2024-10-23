hey stupid

so the site when down again huh?

Here's what you need to do yah fuckin idiot:

1. Make sure the /var/run/gunicorn/prod.pid file exists. Sometimes it gets randomly deleted

   If it exists try updating gunicorn

   (Run tail tail /var/log/gunicorn/error.log to check the error logs)

2. run the following:

   $ cd /var/www/jeremyricodotcom
   $ activate
   $ prod


   You HAVE to be in that directory for the gunicorn workers to recognize jeremyricodotcom as a wsgi module

If neither of those work you're on your own pal

Love,
Your past self