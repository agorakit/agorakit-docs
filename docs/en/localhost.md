Docker provides a minimal image that reflects a potential production environment using:

- **FrankenPHP** container name is `agorakit_php`
- **MariaDB** container name is `agorakit_database`
- **Mailpit** (to access email sent) container name is `agorakit_mailpit`
- **Phpmyadmin** container name is `agorakit_phpmyadmin`

### Setup Docker
- Install Docker and `docker compose`.

- In order to avoid permission issues, you can define GID and UID environment variables via the `setuid.sh` script. This scripts simply set UID and GID to your current user id (UID) and group id (GID). This will be the user owning the files written by the application. This is to avoid having files owned by root. More explanations can be found here : https://aschmelyun.com/blog/fixing-permissions-issues-with-docker-compose-and-php/

- Run `up.sh` or `docker compose up` in the current directory (docker/dev) to start the container.

The container will take a while to build and if all goes well, you can access the app on localhost (on https, accept the browser exception for self signed certificate)

- Connect to the shell inside the container using `./bash.sh`
- `cp .env.dev .env` _(Hint: before you rebuild, make sure to push this .env out of the way)_
- `composer install`
- `php artisan key:generate`
- `php artisan migrate`

With this you have a working dev setup!

!! Don't use this for production, there are probably security issues that need to be addressed/hardened for production.

If needed, you can completely rebuild the docker image using the script `/docker/dev/rebuild.sh`.

You can now access your installation with the following:

### Web access
The app can be reached on http://localhost or https://localhost (you need to let your browser accept the local self-signed certificate with https)

### Shell access
Connect to the running container's shell using the `bash.sh` script. You will land directly in the root of the app and can run php artisan commands or Composer, for example.

### Phpmyadmin
Can be accessed on port 8080: http://localhost:8080

### Read emails
Mailpit is on port 8025 (http://localhost:8025) and its API documentation is at http://localhost:8025/api/v1.
