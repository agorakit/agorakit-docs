# Contributing to Agorakit

You want to contribute to the project? Great! Any idea is welcome. 

- Please discuss the bug or feature request in the issue queue first.
- Check the licence (AGPL) to see if it fits your contribution model
- Follow Laravel best practices
- We use Unpoly js for spa like functionality, read a bit about it since it's not as popular as other options (think of it as turbolinks on steroids)
- We use Bootstrap flavored by tabler.io


# Developement server using our lightweight Docker dev setup
This is the recommended way. This custom docker compose setup provides a complete development server.

It provides an as small as possible image that reflects a potential production environment using :

- Frankenphp as a php runtime : container name is **agorakit_php**
- Mariadb : container name is **agorakit_database**
- Mailpit to access email sent : container name is **agorakit_mailpit**
- Phpmyadmin : container name is **agorakit_phpmyadmin**


## Setup dev environment
- Install docker and docker compose

- In order to avoid permission issues, you can define GID and UID environment variables via the `setuid.sh` script. This scripts simply set UID and GID to your current user id (UID) and group id (GID). This will be the user owning the files written by the application. This is to avoid having files owned by root. More explanations can be found here : https://aschmelyun.com/blog/fixing-permissions-issues-with-docker-compose-and-php/

- Run `up.sh` or `docker compose up` in the current directory (docker/dev) to start the container.

The container will take a while to build and if all goes well, you can access the app on localhost (on https, accept the browser exception for self signed certificate)

- Connect to the shell inside the container using `./bash.sh`
- `cp .env.dev .env` _(Hint: before you rebuild, make sure to push this .env out of the way)_
- `composer install`
- `php artisan key:generate`
- `php artisan migrate`

With this you have a working dev setup!

!! Don't use this for production, there are probably security issues that need to be adressed/hardened for production.

If needed, you can completely rebuild the docker image using the script `/docker/dev/rebuild.sh`.


You can now access your installation with the following : 


## Web access
The app can be reached on http://localhost or https://localhost (you need to let your browser accept the local self signed certificate with https)

## Shell access
Connect to the runing container's shell using the `bash.sh` script. You will land directly in the root of the app and can run php artisan commands or composer for example.

## Phpmyadmin
Can be accessed on port 8080 : http://localhost:8080

## Read emails
Mailpit can be accessed on port 8025 : http://localhost:8025

(Mailpit API documentation is available here : http://localhost:8025/api/v1)


# Seed the DB 
In developement, it's often useful to have sample content. If you want to seed the DB with fake content, simply run

    $ php artisan db:seed


# Working on design and css
I ditched all build steps, now everything happens in a flat custom.css file.

All external JS and CSS are served from various CDN's. At some point the files will be re-served from local, when everything will be stabilized, and if there are real benefits of doing so.

No npm, no node, no tailwind, no purge, no minifier, no trouble :)


# Testing your code
Agorakit is tested using the Laravel testing framework.

In order to test, you need to have an existing testing database. Just create an additional empty DB, for instance agorakit_testing and check in the phpunit.xml file that everything matches.

Before comiting code, you should either write more tests (in this case you deserve a cookie). Or at least check that you didn't break anything by simply typing::

    php artisan test

...in the root of your project.

No error should appear (provided that you have everything correctly set up.

We use continuous integration to run all those tests on commit so it will be done automatically for you at some point :-)

All tests must pass for a PR to be considered of course.

# Writing tests
Don't hesitate to write tests. We favor well defined tasks an end user would really accomplish, like registering, creating an account, posting, uploading, etc... It has served us very well in the past to spot errors and it really mirrors real use cases. Although we are open to other kind of tests as well...
