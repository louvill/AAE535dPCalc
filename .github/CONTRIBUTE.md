# Contribute

**Opening new issue?** Please read [ISSUES.md](../ISSUES.md) first.

Contributing to the The Pressure Drop Calculator is easy — simply fork the repository here on GitHub, make your changes, and then send us a pull request.

The Pressure Drop Calculator is released under the MIT License. The code and content of this application is free to use, modify, and redistribute for any purpose whatsoever. See https://choosealicense.com/licenses/mit/ for details.
This means any contribution you make to the project will also be covered by the same license. Larger and distinct works can be distributed under different terms with or without source code.

## Guidelines

There are a couple of guidelines we suggest sticking to:

* Add this repository as an `upstream` remote.
* Keep your `master` branch clean. This means you can easily pull changes made to this repository into yours.
* Create a new branch for each new feature or set of related bug fixes.
* Never merge from your local branches into your `master` branch. Only update that by pulling from `upstream/master`.

## Pull Request Notes
If you file a PR but you're still working on it, please add a [WIP] before the title text. This will tell the reviewers that you still intend to add more to the PR and we don't need to review it yet. When it's ready to be reviewed by a merger just edit the title text to remove the [WIP].

If you are also looking for suggestions then mark it with [CR] — "comments requested". You can use both [WIP] and [CR] to indicated that you need opinion/code review/suggestions to continue working (e.g. "[WIP] [CR] Super awesome big feature"). Feel free to remove [CR] when you feel you got enough information to proceed.

This can help speed up our review process by allowing us to only review the things that are ready for it, and will prevent anything that isn't completely ready from being merged in.

It is not required to solve or reference an open issue to file a PR, however, if you do so, you need to explain the problem your PR is solving in full detail.

### All PRs should have a "Summary" line
Summary is a one-line description of your change that will be extracted and added to the project changelog.

The format is: ```SUMMARY: Category "description"```

The categories to choose from are: Features, Bugfixes, Performance, Infrastructure.

Example: ```SUMMARY: Performance "Changes friction factor calculation to Runge-Kutta Method"```
Or, if you want it treated as a minor tweak that doesn't appear in the changelog:
```SUMMARY: None```

Changelog guidelines will be contructed at a later time for more information of what each category represents.
