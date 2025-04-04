# How to contribute localization

We use [Laravel localization support](https://laravel.com/docs/12.x/localization).

## Add a new language to Agorakit
To add a new language, you may need to ask for help on one of [the contact channel](contact.md).

You can translate all the files found in /lang/resources/en to a new language.

## Enhance translations
Want to contribute better translations to existing languages?

We use [translation.io](https://translation.io) to have a translation GUI instead of directly editing the files by hand. You can also contact us if you want to be added to the [translation.io Agorakit repository](https://translation.io/philippejadin/agorakit/).

Alternatively you can of course propose pull requests using GitHub, although this is a bit more technical.

# Developers
For developers, simply use the laravel built-in trans() or __() functions to add user interface text.
We mainly use the ["classic" short key system](https://laravel.com/docs/12.x/localization#using-short-keys), and most of the translations are in the messages.xxx namespace, which means the english strings are in [resources/lang/en/messages.php](https://github.com/agorakit/agorakit/blob/main/resources/lang/en/messages.php).

## Scan for new strings to be translated
There is an artisan command to detect new translations strings in code and views that automatically add the translations to the english file, just run `php artisan localize` to scan and update the English lang files.

## Sync with translation.io
If you have access to the translation.io repository and want to sync translations, add your translation.io key in your .env file like this : `TRANSLATIONIO_KEY=xxxxx`
Then run `artisan translation:sync`

## The `./translate` script
If you want to run the two steps (scan for new strings and sync with translation.io), you can simply run the `./translate` script located in the root of the project. It takes care of the two commands and should always be non-destructive.

It's also a good idea to always run it so the translation php and json arrays are stored in the exact same way and also ordered, that way we hopefully have clean git revision history.