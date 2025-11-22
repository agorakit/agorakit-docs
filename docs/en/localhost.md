Agorakit provides a development environment Docker image running:

- **FrankenPHP** container name is `agorakit_php`
- **MariaDB** container name is `agorakit_database`
- **Mailpit** (to access email sent) container name is `agorakit_mailpit`
- **Phpmyadmin** container name is `agorakit_phpmyadmin`

!!! warning "Localhost Development Only"
    Don't use this in Production or anywhere publicly accessible, it is very insecure!

## Setup & Run Docker
- Install Docker Desktop on [Mac](https://docs.docker.com/desktop/setup/install/mac-install/), [Windows](https://docs.docker.com/desktop/setup/install/windows-install/), or [Linux](https://docs.docker.com/desktop/setup/install/linux/).
- From the repo root, run: `./bin/dev-init.sh`

The containers may take a moment to build.
If all goes well, it should **immediately connect you to the shell** on the dev instance (in `/app`).

That's it!  The copy of the code there is mounted to your code repo — it's the same files!
You can now access the app on localhost. If HTTPS throws a warning, see below.

## Trust Caddy's CA
To use HTTPS you'll want to [add the CA certificate to your browser](https://docs.docker.com/engine/network/ca-certs/).

### MacOS Safari
1. Open the Keychain Access app.
1. In Keychain Access, select System, then switch to the Certificates tab.
1. Drag-and-drop `./.docker/dev/root.crt` into the list of certificates. Enter your password if prompted.
1. Find the newly added certificate, double-click it, and expand the Trust section.
1. Set Always Trust for the certificate. Enter your password if prompted.

### MacOS Firefox
1. Copy `./.docker/dev/root.crt` to your Desktop (Firefox cannot find it in a dot folder).
1. Open Firefox's Settings -> Privacy & Security.
2. Find **Certificates** and select "View Certificates >".
3. On the **Authorities** tab, select the "Import..." button and select your copy of `root.crt`.
5. In the popup, check "Trust this CA to identify websites." and select OK, then OK again.

## Connect PHPStorm to Docker

### Daemon
Make sure Docker is running, then in PHPStorm:

* File -> Settings... -> Build, Execution, Deployment -> Docker -> '+' (middle column)
* It should auto-connect and say "Connection successful".
* Click '+' (bottom of right column)
  * Set 'Virtual machine path' to `/app`
  * Set 'Local path' to wherever you cloned the repo.
* 'OK'

### CLI Interpreter
In PHPStorm:

* File -> Settings... -> PHP
  * 'CLI Interpreter:' (right column) -> '...' button -> '+' button
  * 'From Docker, Vagrant, (etc)' -> Docker Composer (option)
* 'Configuration files:' (folder icon) -> '+' (in popup)
  * Select `compose.dev.yml` file (root of repo) -> 'OK'
* Select Service: 'frankenphp' -> 'OK'

### Xdebug
To enable step debugging, [get the browser extension](https://xdebug.org/docs/step_debug#browser-extensions) and configure your IDE to listen on port `9003`.

In PHPStorm: "Start Listening for PHP Debug Connections".

Use the browser extension to enable it and trigger a connection when navigating to the localhost site.

## Use the Environment

### App access
In your **browser**, visit `http://localhost` or `https://localhost` (accepting the local self-signed certificate).

### Shell access
From the **CLI**, run `./bin/dev-connect.sh`. You will land in the app root and can run `php artisan` commands or Composer.

### Database access
**Phpmyadmin** is on port 8080 (`http://localhost:8080`).

### Email access
**Mailpit** is on port 8025 (`http://localhost:8025`) and its API documentation is at `http://localhost:8025/api/v1`.

### Use Docker
Use Docker Desktop's UI to stop the containers or:

- Stop the containers: `docker compose -f compose.dev.yml stop`
- Rebuild the containers: `docker compose -f compose.dev.yml build --no-cache`
- Shell into the dev box when it's already running: `./bin/dev-connect.sh`
  - Alias for: `docker exec -it agorakit-dev bash`

It is safe to re-run `./dev-init.sh` any time to rebuild the containers & shell in.
On first run, it will create `.env.dev` and generate the Laravel `APP_KEY`.
To regenerate it, simple delete `.env.dev` and run the script again.
