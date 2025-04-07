# How to contribute localization

We use [Laravel localization support](https://laravel.com/docs/12.x/localization).

## Improve translations
We use [translation.io](https://translation.io) to have a translation GUI instead of directly editing the files by hand. Contact us to be added to the [translation.io Agorakit repository](https://translation.io/philippejadin/agorakit/).

## Add a language
To add a new language, you may need to [ask for help](contact.md). You can translate all the files found in `/lang/resources/en` to a new language.

# Developers
For developers, use the Laravel built-in `trans()` or `__()` functions to add user interface (UI) text.
We use the ["classic" short key system](https://laravel.com/docs/12.x/localization#using-short-keys). Most translations are in the `messages.xxx` namespace, which means the English strings are in [resources/lang/en/messages.php](https://github.com/agorakit/agorakit/blob/main/resources/lang/en/messages.php).

## Scan for new strings to be translated
There is an `artisan` command to detect new translations strings in code and views that automatically add the translations to the English file, just run `php artisan localize` to scan and update the English lang files.

## Sync with translation.io
If you have access to the translation.io repository and want to sync translations, add your translation.io key in your `.env` file (ex: `TRANSLATIONIO_KEY=xxxxx`).
Then run `artisan translation:sync`.

## Shortcut: `translate.sh` script
To run BOTH steps (scan & sync), you can run `./bin/translate.sh`. It is non-destructive.

To keep a clean git revision history, please always verify the translation PHP & JSON arrays remain ordered the same.