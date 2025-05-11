Agorakit is proudly a hypermedia app. We use PHP with Laravel and follows its best practices on the backend. However, we use [Unpoly](https://unpoly.com/) for UI interactivity, flat CSS (no build), and Bootstrap-flavored tabler.io.

!!! tip
    Verify the [AGPLv3](https://www.fsf.org/bulletin/2021/fall/the-fundamentals-of-the-agplv3) licence fits your needs.

!!! warning
    **Before coding:** Review the [roadmap](https://app.agorakit.org/groups/2014/discussions/18470), then propose & discuss changes on the [community](https://app.agorakit.org/groups/2014).

## Quality tools
To maintain code quality, we use:

* [PSR-12](https://www.php-fig.org/psr/psr-12/) (coding standard)
* [PHPUnit](https://phpunit.de/index.html) (Unit & integration tests)
* [PHPStan](https://phpstan.org/) via [Larastan](https://github.com/larastan/larastan?tab=readme-ov-file#%EF%B8%8F-about-larastan) (static analysis)
* [GitHub Actions](https://github.com/agorakit/agorakit/actions) (CI)

## Conventions
To enable clear communication between stakeholders, we use:

* [Semantic versioning](https://semver.org/) ([discussion](https://app.agorakit.org/groups/2014/discussions/18427))
* [Conventional commits](https://www.conventionalcommits.org)
* Pull requests ("Code review" below)

## Code review
We require peer code reviews both to maintain quality and socialize changes. To enable faster acceptance of code changes, we follow these practices.

### Code structure
These checks increase safety and make code review more effective.

1. NEVER combine **functional changes** with coding standards updates nor environment changes (like CI config). Give each their own pull request.
1. New functions & methods MUST have **only one purpose**. This makes them clear, testable, and safe.
1. ALWAYS use descriptive **branch names** (e.g. `fix/some-name` or `feat/new-thing`).

### Pull request basics
Skipping these steps wastes other peoples' time. Everyone should always do them when contributing code.

1. Write descriptive **titles in the [imperative mood](https://grammar.collinsdictionary.com/us/easy-learning/the-imperative)** (e.g. "Fix the thing", "Update the widget"). _If this is difficult, the PR may be too broad_.
1. **Cross-reference** ALL related PRs, issues, discussions, or docs with a link.
1. Verify:
    1. **Target** branch (usually `main`).
    1. **Code diff** is what you intended.
    1. **Quality checks pass** in the CI pipeline.
1. If not immediately ready for review, **make it a draft**.

### Advanced pull request authoring
Writing exception pull requests leads to faster development, less debugging, and more cohesive teams.

1. **Summary**: For longer PRs, start by briefly summarize the entire process (initial challenge to solution) in a sentence or two. This especially helps project leads understand what you've done even if they lack the time to dive into details.
1. **Goals**: What are we trying to accomplish? You should understand our higher-level goals and discuss how your changes align with them, or document in the code why they do not. Link to any relevant work items or discussions.
1. **Solution**: What other solutions did you consider and why did you choose _this_ one? This helps other developers learn from or mentor you, and provides a great log for future considerations.
1. **Methodology**: Why did you implement the solution you chose _this_ way? You can even lead the reviewer thru your code choices like a tour by commenting on lines of your own PR.
1. **Potential**: What future work could be done, and how important is it? Does it warrant writing follow-up issues?
1. **History**: Correct & condense your commit history with `git rebase` to make it easier to understand. Exemplary commit histories present a logical story. Adding PR comments between batches of commits can add further narrative.

How in-depth you discuss each of these items in a pull request will vary greatly depending on scope and experience.


## AI coding assistance

At this time, we have not seen evidence that AI is capable of producing [code reviews as requested above](#advanced-pull-request-authoring). Therefore, we strongly discourage the use of AI in code contributions to this project unless under the careful supervision of a senior software engineer with sufficient experience to revise & contextualize its assistance. We will close pull requests that appear to have been primarily generated with generative AI tools due to requiring exessive review time.
