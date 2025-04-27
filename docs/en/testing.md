## Seed the DB
In development, it's often useful to have sample content. If you want to seed the DB with fake content, simply run

    $ php artisan db:seed

## Running tests
Agorakit is tested using the Laravel testing framework.

In order to test, you need to have an existing testing database. Just create an additional empty DB, for instance agorakit_testing and check in the phpunit.xml file that everything matches.

Before committing code, you should either write more tests (in this case you deserve a cookie). Or at least check that you didn't break anything by simply typing (in the root of your project):

    php artisan test

No error should appear, provided that you have everything correctly set up.

We use continuous integration to run all those tests before merging pull requests. All tests must pass for a PR to be considered of course.

## Writing tests
Don't hesitate to write tests. We favor well-defined tasks an end user would really accomplish, like registering, creating an account, posting, uploading, etc. It has served us very well in the past to spot errors and it really mirrors real use cases. We are open to other kind of tests as well.
