If you just installed Agorakit, take some time to configure it correctly for your use case.

## Homepage introduction text 
Set an intro text on the homepage for newcomers : go to the admin page from your user profile dropdown.
Using the editor you can add external images and whatever you want.

## Check all the admin settings
Go to the admin menu (from your user profile dropdown) and check all the settings there. Pay attention to the various permissions and group types you allow on your server.

## Inbound emails
This additional step allows you to have one mailbox for each group so members can post by email to create discussions and reply to discussions emails to create new comments.

!!! note
    Inbound email support is experimental but in use on several instances. You might however experience bugs, please report them if it happens to your installation.

- You need an email address on a server with imap support. It must either be a catch all on a subdomain (or even on a domain) or a server supporting "+" addressing (gmail for example allows this).
- You need the php imap extension
- Configuration happens in your .env

Let's say you installed Agorakit on agora.example.org:
- Create a catchall mailbox on * .@agora.example.org
- Edit your .env file and add/define the following settings:

```
# Inbox mail box server settings, use for incoming emails.
# Set INBOX_DRIVER to null to disable this feature
INBOX_DRIVER=imap
INBOX_HOST=yourmailhost.tld
INBOX_USERNAME=username of the mailbox
INBOX_PASSWORD=password of the mailbox
INBOX_PREFIX=
INBOX_SUFFIX=@agora.example.org
```

### Defining prefixes and suffixes
You need to fill prefix and suffix. Two cases there :

- For a catch-all there is no prefix. The suffix in the above example would be `@agora.example.org`. This will create emails like `group-slug@agora.example.com`.
- On the other hand if you use "+" addressing (a gmail box for instance, let's call it agorakit@gmail.com),
    - prefix will be `agorakit+`
    - suffix will be `@gmail.com`

    This will create emails like `agorakit+group-slug@gmail.com`

If you enable inbound email, the mailbox will be automatically checked and processed email will be put in a "processed" folder under INBOX. Failed emails will be similarly put a "failed" folder under INBOX for inspection.
