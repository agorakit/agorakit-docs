# Contribuer à Agorakit

Vous voulez contribuer au projet ? C'est très bien ! Toute idée est la bienvenue.

- Veuillez d'abord discuter du bogue ou de la demande de fonctionnalité dans la file d'attente des problèmes.
- Vérifiez la licence (AGPL) pour voir si elle correspond à votre modèle de contribution.
- Suivez les meilleures pratiques de Laravel
- Nous utilisons Unpoly js pour les fonctionnalités de type spa, lisez un peu à son sujet car il n'est pas aussi populaire que les autres options (pensez-y comme des turbolinks sur les stéroïdes).
- Nous utilisons Bootstrap aromatisé par tabler.io


# Serveur de développement utilisant notre installation légère Docker dev
C'est la méthode recommandée. Cette configuration personnalisée de Docker compose fournit un serveur de développement complet.

Elle fournit une image aussi petite que possible qui reflète un environnement de production potentiel en utilisant :

- Frankenphp comme runtime php : le nom du container est **agorakit_php**
- Mariadb : le nom du conteneur est **agorakit_database**
- Mailpit pour accéder aux emails envoyés : le nom du conteneur est **agorakit_mailpit**
- Phpmyadmin : le nom du conteneur est **agorakit_phpmyadmin**


## Configurer l'environnement de développement
- Installer docker et docker compose

- Afin d'éviter les problèmes de permission, vous pouvez définir les variables d'environnement GID et UID via le script `setuid.sh`. Ce script définit simplement UID et GID avec votre identifiant d'utilisateur (UID) et votre identifiant de groupe (GID) actuels. Ce sera l'utilisateur propriétaire des fichiers écrits par l'application. Cela permet d'éviter que les fichiers appartiennent à l'utilisateur root. Plus d'explications peuvent être trouvées ici : https://aschmelyun.com/blog/fixing-permissions-issues-with-docker-compose-and-php/

- Exécutez `up.sh` ou `docker compose up` dans le répertoire courant (docker/dev) pour démarrer le conteneur.

Le conteneur va prendre un certain temps pour se construire et si tout se passe bien, vous pouvez accéder à l'application sur localhost (sur https, acceptez l'exception du navigateur pour le certificat auto-signé).

- Connectez-vous au shell à l'intérieur du conteneur en utilisant `./bash.sh`
- `cp .env.dev .env` _(Astuce : avant de reconstruire, assurez-vous de pousser ce .env hors du chemin)_
- `composer install`
- `php artisan key:generate`
- `php artisan migrate`

Avec cela, vous avez une configuration de développement qui fonctionne !

! ! Ne l'utilisez pas pour la production, il y a probablement des problèmes de sécurité qui doivent être résolus/durcis pour la production.

Si nécessaire, vous pouvez reconstruire complètement l'image docker en utilisant le script `/docker/dev/rebuild.sh`.


Vous pouvez maintenant accéder à votre installation avec le script suivant :


## Accès web
L'application est accessible sur http://localhost ou https://localhost (vous devez laisser votre navigateur accepter le certificat local auto-signé avec https)

## Accès au shell
Connectez-vous au shell du conteneur en cours d'exécution en utilisant le script `bash.sh`. Vous arriverez directement à la racine de l'application et pourrez lancer des commandes php artisan ou composer par exemple.

## Phpmyadmin
Accessible sur le port 8080 : http://localhost:8080

## Lire les emails
Mailpit est accessible sur le port 8025 : http://localhost:8025

(La documentation de l'API Mailpit est disponible ici : http://localhost:8025/api/v1)


# Alimenter la base de données
En développement, il est souvent utile d'avoir des exemples de contenu. Si vous voulez ensemencer la base de données avec du faux contenu, exécutez simplement

    $ php artisan db:seed


# Travailler sur le design et les css
J'ai supprimé toutes les étapes de construction, maintenant tout se passe dans un fichier custom.css plat.

Tous les JS et CSS externes sont servis par différents CDN. A un moment donné, les fichiers seront re-servis en local, quand tout sera stabilisé, et s'il y a de réels avantages à le faire.

Pas de npm, pas de node, pas de tailwind, pas de purge, pas de minifier, pas de problème :)


# Tester votre code
Agorakit est testé en utilisant le framework de test Laravel.

Pour tester, vous devez avoir une base de données de test existante. Il suffit de créer une nouvelle base de données vide, par exemple agorakit_testing et de vérifier dans le fichier phpunit.xml que tout correspond.

Avant de commencer le code, vous devriez soit écrire plus de tests (dans ce cas, vous méritez un cookie). Ou au moins vérifier que vous n'avez rien cassé en tapant simplement: :

    php artisan test

...à la racine de votre projet.

Aucune erreur ne devrait apparaître (à condition que tout soit correctement configuré).

Nous utilisons l'intégration continue pour exécuter tous ces tests lors de la validation, donc cela sera fait automatiquement pour vous à un moment donné :-)

Tous les tests doivent être réussis pour qu'un PR soit pris en compte, bien entendu.

# Écrire des tests
N'hésitez pas à écrire des tests. Nous privilégions les tâches bien définies qu'un utilisateur final accomplirait réellement, comme l'inscription, la création d'un compte, la publication, le téléchargement, etc... Cela nous a très bien servi dans le passé pour repérer les erreurs et cela reflète vraiment les cas d'utilisation réels. Bien que nous soyons ouverts à d'autres types de tests...
