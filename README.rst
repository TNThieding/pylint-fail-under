###########################
[pylint-fail-under] Package
###########################

.. image:: https://travis-ci.org/TNThieding/pylint-fail-under.svg?branch=master
    :target: https://travis-ci.org/TNThieding/pylint-fail-under

.. image:: https://coveralls.io/repos/github/TNThieding/pylint-fail-under/badge.svg?branch=master
    :target: https://coveralls.io/github/TNThieding/pylint-fail-under?branch=master

.. image:: https://readthedocs.org/projects/pylint-fail-under/badge/?version=latest
    :target: https://pylint-fail-under.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Pylint wrapper that verifies code reaches a minimum quality score.

***********
Quick Start
***********

Execute the ``pylint-fail-under`` command with the same arguments as a ``pylint`` call. In addition,
specify the minimum Pylint quality score with the ``--fail_under`` argument.

If the Pylint score is greater than the fail under value, the script exits successfully with an
exit code of zero. For example::

    $ pylint-fail-under --fail_under 9.0 my_package
    ************* Module my_package
    my_package\__init__.py:1:0: C0111: Missing module docstring (missing-docstring)
    ### Pylint output removed for documentation conciseness! ###
    my_package\tests\test_my_pkg.py:328:0: C0303: Trailing whitespace (trailing-whitespace)

    ------------------------------------------------------------------
    Your code has been rated at 9.49/10 (previous run: 9.49/10, +0.00)

Otherwise, if the Pylint score is under the minimum, the script exits with a non-zero exit code. For
example::

    $ pylint-fail-under --fail_under 9.75 my_package
    ************* Module my_package
    my_package\__init__.py:1:0: C0111: Missing module docstring (missing-docstring)
    ### Pylint output removed for documentation conciseness! ###
    my_package\tests\test_my_pkg.py:328:0: C0303: Trailing whitespace (trailing-whitespace)

    ------------------------------------------------------------------
    Your code has been rated at 9.49/10 (previous run: 9.49/10, +0.00)

    ERROR: score 9.4921875 is less than fail-under value 9.75
