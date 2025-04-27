# Welcome to Agorakit

Agorakit is an **open source**, **Web-based** groupware for **collectives**. It allows groups to collaborate, organize events, and store files. It keeps everyone updated with a discussion forum, agenda, file manager, and email notifier.

Most of the time, Agorakit doesn't even need an admin, keeping the process **as horizontal as possible**.

If you are looking for ways to contribute (great!), check the [contribution guide](contribute.md).

## Try Agorakit
If you want to try Agorakit without installing it, go to <https://app.agorakit.org> to create an account and then create or join some groups.

For guidance, check the [user guide](usage.md) or [group owner guide](group.md).

Server admins can alternatively [install](install.md) or [upgrade](upgrade.md) it themselves.

## Mission Statement
Agorakit offers a complete toolset for a community to effectively self-organize that encourages cohesion at a sustainably small scale while supporting continuous change. It supports good governance by providing strong individual & group protections, enabling emergent leadership, and facilitating group alignment & mediation.

## Beliefs
To stay aligned on how we achieve our mission, Agorakit subscribes to these core beliefs:

1. Communities should **only** be divided by individual choices: interest, labor, location, or belief (_except_ beliefs that create _additional_ divisions or restrict those individual choices).
2. Sustainable communities **must** support diversity, equity, inclusion, & accessibility, which requires an accountable power structure within the software and that the community owns its own data.
3. Communities require trust, which requires the investment of time between individuals. Therefore, you **cannot** create community that is frictionless, fully automated, or infinitely scalable.
4. Every community is unique and its software should reflect that, but community management should not require programming plugins or themes.
5. The open Web is critical to the future of humanity and is best supported through standards-based interoperability, strong data privacy, and platform transferability.

For more information, see the [community discussion](https://app.agorakit.org/groups/2014/discussions/18471).

## Features Overview

### Groups
- Create an unlimited amount of groups
- Each group can be open (anyone can join) or private (invite-only)
- Each group has a discussion list, calendar, map, file repository, and member list
- Content is public in public groups and private in private groups

### Discussions
- Create discussion topics & reply with comments
- Mention others in comments using @name (they get notified)
- Mention files using f: (autocomplete opens)
- Mention other discussions using d: (autocomplete opens)

### Calendar
- Global and per group calendars with RSS & iCal feeds
- List upcoming events as a list or as a dynamic calendar
- Show geolocalized events on a map
- Embed elsewhere using iframes

### Files
- Upload & tag many files at once
- Quick search among files by author, filename, and tags
- Mention files in comments

### Members
- Access a list of members (global / per group)
- Contact others without leaking your/their email (privacy)
- Check what others are up to (activity feed)
- Fill your profile with portrait, bio, address (if you want)

### Notifications / emails
- Choose how often you want to be notified per group (from hourly for the hardcore up to monthly to keep your mailbox cool)
- Auto-login from "Reply" links (great time saving)
- Instant notifications when someone mentions you (for urgent matters)

### Admin
- Get stats on everything
- Mass-invite new members via email
- Mass-add existing members to groups

### Architecture
- Standard Laravel application - anyone who knows Laravel can work with Agorakit easily
- Simple hypermedia page loading, not single page app complexities
- Bootstrap-based UI
- Simple security model, database schema, & file storage scheme

### Privacy
- Your data is yours, host it where you want
- Geolocalization is opt-in and obscured by ~100 meters
- Open source you can study and trust
