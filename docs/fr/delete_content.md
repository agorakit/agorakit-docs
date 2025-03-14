# Suppression de contenu
La suppression de contenu sur Agorakit suit une procédure qui permet de répondre à différents impératifs :

- le droit de chacun à supprimer ses productions
- le droit de changer d'avis dans un certain délai
- le droit de changer d'avis pendant un certain temps
- la conservation des contributions collectives en cas de départ d'un participant.


Lorsqu'un contenu est supprimé, il est marqué comme tel dans la base de données et n'apparaît plus. Un administrateur de l'instance peut remettre en ligne un contenu supprimé en allant dans le menu "admin > récupérer le contenu".

Le contenu marqué comme supprimé est définitivement supprimé (physiquement) de la base de données après 30 jours. Il n'est plus possible de récupérer du contenu après cette période.


# Suppression du compte d'un utilisateur
Si un utilisateur décide de supprimer son compte, il peut choisir de :

- d'anonymiser son contenu (tout le contenu est transféré à un utilisateur anonyme)
- demander que tout son contenu soit supprimé.

Les discussions avec commentaires sont dans tous les cas attribuées à l'utilisateur anonyme, afin de ne pas perdre les contributions des autres utilisateurs.
Il n'est pas possible de supprimer individuellement un fil de discussion avec commentaires.

Un utilisateur qui est le seul administrateur d'un groupe ne peut pas quitter le groupe.


# Restauration d'un élément supprimé
Un administrateur d'instance peut restaurer tout contenu supprimé pendant la période de rétention (30 jours par défaut). Il suffit d'aller dans `Admin > settings > recover content` et de sélectionner le(s) élément(s) à restaurer.

# Nettoyage de la base de données
Si Agorakit est installé correctement (avec des tâches cron récurrentes), la base de données sera automatiquement nettoyée pour se conformer à ce qui précède.
Le nombre de jours de rétention des données avant leur suppression définitive est configurable et fixé à 30 par défaut.