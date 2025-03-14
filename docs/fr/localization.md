# Comment contribuer à la localisation d'Agorakit

Nous utilisons [Laravel localization support] (https://laravel.com/docs/12.x/localization).

## Ajouter une nouvelle langue à Agorakit
Pour ajouter une nouvelle langue, vous devrez peut-être demander de l'aide sur l'un des [canaux de contact](contact.md).

Vous pouvez traduire tous les fichiers trouvés dans /lang/ressources/en dans une nouvelle langue

## Améliorer les traductions

Vous souhaitez contribuer à l'amélioration des traductions dans les langues existantes ?

Nous utilisons [translation.io](https://translation.io) pour avoir une interface graphique de traduction au lieu d'éditer directement les fichiers à la main. Vous pouvez également nous contacter si vous souhaitez être ajouté au dépôt [translation.io Agorakit](https://translation.io/philippejadin/agorakit/).

Vous pouvez également proposer des pull requests en utilisant Github, bien que cela soit un peu plus technique.


# Développeurs
Pour les développeurs, il suffit d'utiliser les fonctions trans() ou __() intégrées à Laravel pour ajouter du texte à l'interface utilisateur.
Nous utilisons principalement le ["classic" short key system](https://laravel.com/docs/12.x/localization#using-short-keys), et la plupart des traductions sont dans l'espace de noms messages.xxx, ce qui signifie que les chaînes anglaises sont dans [resources/lang/en/messages.php](https://github.com/agorakit/agorakit/blob/main/resources/lang/en/messages.php).

## Recherche de nouvelles chaînes à traduire
Il existe une commande artisan pour détecter les nouvelles chaînes de traduction dans le code et les vues qui ajoutent automatiquement les traductions au fichier anglais, il suffit de lancer `php artisan localize` pour scanner et mettre à jour les fichiers de langue anglaise.

## Synchroniser avec translation.io
Si vous avez accès au dépôt translation.io et que vous voulez synchroniser les traductions, ajoutez votre clé translation.io dans votre fichier .env comme ceci : `TRANSLATIONIO_KEY=xxxxx`
Puis lancez `artisan translation:sync`

## Le script `./translate`
Si vous voulez exécuter les deux étapes (recherche de nouvelles chaînes et synchronisation avec translation.io), vous pouvez simplement lancer le script `./translate` situé à la racine du projet. Il prend en charge les deux commandes et devrait toujours être non destructif.

C'est aussi une bonne idée de toujours l'exécuter pour que les tableaux php et json de la traduction soient stockés exactement de la même manière et aussi dans l'ordre, de cette façon nous avons l'espoir d'avoir un historique de révision git propre.