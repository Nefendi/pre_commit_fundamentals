[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Table of Contents

<!--toc:start-->

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
  - [Using pre-commit](#using-pre-commit)
    - [Initial configuration](#initial-configuration)
      - [Gitlint](#gitlint)
        - [Gitlint in a CI environment](#gitlint-in-a-ci-environment)
      - [Commit messages get dropped upon rejection by gitlint](#commit-messages-get-dropped-upon-rejection-by-gitlint)
    - [Skipping running Git pre-commit hooks](#skipping-running-git-pre-commit-hooks)
    - [Running pre-commit in a CI environment](#running-pre-commit-in-a-ci-environment)
  - [How to play with this repository](#how-to-play-with-this-repository)
  - [Dependencies](#dependencies)
  <!--toc:end-->

# Introduction

This repository contains a set of badly written files with Python code to show
what [pre-commit](https://pre-commit.com/) can do to easily enforce code style
guidelines chosen for a project both on developers' local machines and inside a
CI environment.

## Using pre-commit

**Pre-commit** is a tool for 'managing and maintaining multi-language pre-commit
hooks' (a direct quote from the website linked above). The heart of
**pre-commit** is its configuration file, namely `.pre-commit-config.yaml`. In
this file, it is possible to specify various tools that should be run and check
source code before a Git commit can be made (hence the name `pre-commit`). The
tools mentioned in the configuration files can be local ones or links to
external repositories configured as 'pre-commit hooks providers' (these are my
words). Local tools will be searched for in our local machines, but remote
sources will be downloaded and set up by `pre-commit` automatically.

### Initial configuration

With both a `.pre-commit-config.yaml` file present and the `pre-commit` package
installed (see the [Dependencies](#dependencies) section), you can simply run
`pre-commit install` and everything will be configured and set up, including the
installation of hooks to the `.git` directory. Now, every time you try to make a
commit, the hooks listed in the configuration file will be run and, if needed,
your commit will be rejected. It is worth noticing that running hooks should not
take very long time even in larger projects, because they will be run only on
the files which are currently in the Git's index (i.e. have been staged for the
next commit).

#### Gitlint

By default, `pre-commit` does not install commit-msg hooks, but this is what
Gitlint needs. To fix this issue, you need to run
`pre-commit install --hook-type commit-msg` in addition to the regular
`pre-commit install` command. You can read more about it in
[Gitlint's documentation](https://jorisroovers.com/gitlint/#using-gitlint-through-pre-commit).

Alternatively, you can set the top-level `default_install_hook_types` option to
a list containing both `pre-commit` and `commit-msg` hooks, what is done in the
configuration file attached to this project.

##### Gitlint in a CI environment

In `.pre-commit-config.yaml`, there is a special hook, `gitlint-ci` which is
supposed to be invoked within CI environments. It invokes gitlint without any
parameters, which causes the linting to be applied to the latest commit. The
hook has a `manual` stage hard-coded, which signifies that it needs to be
invoked manually by running `pre-commit run --hook-stage manual gitlint-ci`. You
can read more in the documentation linked above.

#### Commit messages get dropped upon rejection by gitlint

Unfortunately, if your commit gets rejected by `gitlint` and you try to make a
commit once again to correct your mistakes, you will not see the previous commit
message. This is a known limitation of `pre-commit` arising from the fact how
the `commit-msg` hook works in Git. Perhaps there exists a tool for fixing this,
but I have not found it. Nor have I searched for it very vigorously. You can
read more about the issue
[here](https://github.com/pre-commit/pre-commit/issues/833). Luckily, this is
not something that you cannot fix easily by yourself. After your commit has been
rejected, you can edit the previous commit message with this command:
`git commit --edit --file $(git rev-parse --git-path COMMIT_EDITMSG)`.

### Skipping running Git pre-commit hooks

Sometimes when working fast on a feature, you may want to ignore the established
checks, because you are going to correct your mistakes in the future (after a
lot of rebases and clean-ups, for example). Skipping running Git pre-commit
hooks is as easy as passing the `--no-verify` flag to the `git commit` command.

### Running pre-commit in a CI environment

It is also possible to run `pre-commit` without making a commit. It is as easy
as running `pre-commit run --all-files` or `pre-commit run --files` if you want
to check only particular files. For other options, see the output of
`pre-commit --help` command. If you want to run only a particular hook, pass the
hook's ID to the call to `pre-commit run`.

## How to play with this repository

If you want to see for yourself how awesome `pre-commit` is, simply make a
change in one of the files or create a brand new one, add the changes to Git's
staging area and try to commit them.

## Dependencies

The code was written using Python 3.10.9. All the needed dependencies are in the
requirements.txt file. Simply run `pip install -r requirements.txt` in a virtual
environment to download everything.
