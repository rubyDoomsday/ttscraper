# TT Scraper

ttscraper is a script that scrapes the thousand trails campsites for location details and outputs a CSV

## Environment Setup

**Prerequisites**

- [Docker](https://docs.docker.com/engine/install/)
- [Python 3](https://www.python.org/downloads/release/python-380/)

A bootstrap script has been supplied to install these dependencies and more the first time you clone the repository. From the project root run the following command:

```shell
bin/bootstrap
```

# Testing

To run repo tests use

```shell
bin/test
```

## Gitflow

How to develop on this project

### Github CLI

The example below uses [github cli](https://cli.github.com/) and [git](https://git-scm.com/about) to illustrate a typical workflow and
branch naming:

```
  # @Contribute
  my-repo git:(main)> git checkout -b feature/new-thing
  my-repo git:(feature/DATA-1234-new-thing)> # make code changes
  my-repo git:(feature/DATA-1234-new-thing)> git add . && git commit -m "what/why/links/etc"
  my-repo git:(feature/DATA-1234-new-thing)> git push -u origin HEAD
  my-repo git:(feature/DATA-1234-new-thing)> gh pr create -f -B main -a myUserName

  # @Review
  # address feedback, harden testing, QA as needed, etc.
  my-repo git:(feature/DATA-1234-new-thing)> gh pr merge
  # QA in staging environment, look for any gotyas

  # @Deploy
  my-repo git:(main)> git fetch && git pull
  my-repo git:(main)> git tag -a release/2022.01.12.001 -m "Release 1/12-001"
  my-repo git:(main)> git push --tags
  # ensure build and deploy hooks complete

  # @Rinse and Repeat
```
