#############
Release Notes
#############

****************************************************************
[0.3.0] Return zero exit code when no score parsed. (2019-10-14)
****************************************************************

Previously, the command line interface returned an exit code of ``2`` if no score was parsed. In files with
``# pylint: disable-all`` or a file with no code do not generate a score, this caused a false positive. Now, return
an exit code of ``0`` if no score is parsed.

*Thank you to GitHub user tanishq-dubey for proposing this change and for his original pull request.*

*******************************************
[0.2.0] Drop Python 2 support. (2019-06-16)
*******************************************

Remove legacy Python 2 syntax from code.

This release includes the following under-the-hood changes:

- Migrate repository from GitHub to GitLab (including CI/CD).
- Pylint cleanup regarding Python 3 syntax.

******************************************
[0.1.0] Initial beta release. (2019-03-16)
******************************************

Release initial beta version of ``pylint-fail-under`` package with the following features:

- Command line interface to verify that a minimum Pylint score is reached.
