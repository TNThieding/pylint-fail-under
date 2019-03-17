"""Test module for primary command line interface."""

import sys
import unittest

import mock

from pylint_fail_under.__main__ import main

if sys.version_info > (3, 0):
    # Python 3
    from io import StringIO
else:
    # Python 2
    from StringIO import StringIO


class _MockPylintLinter(object):

    def __init__(self, score):
        self.stats = {"global_note": score}


class _MockPylintResults(object):

    def __init__(self, score):
        self.linter = _MockPylintLinter(score)


class TestCmdLineInterface(unittest.TestCase):

    """Test case class for primary command line interface."""

    def test_pass(self):
        """Test success/passing when Pylint score exceeds argument-specified minimum."""
        sys_args = [None, "--fail_under", "8.5", "--disable", "duplicate-code", "my_pkg"]
        with mock.patch("sys.argv", sys_args):
            with mock.patch("pylint_fail_under.__main__.Run",
                            return_value=_MockPylintResults(9.3)) as pl_mock:
                exit_code = main()

        pl_mock.assert_called_once_with(
            args=["--disable", "duplicate-code", "my_pkg"], do_exit=False)
        assert exit_code == 0

    def test_fail(self):
        """Test failure when Pylint score is less than argument-specified minimum."""
        sys_args = [None, "my_pkg", "--fail_under", "9.25"]
        with mock.patch("sys.argv", sys_args):
            with mock.patch("pylint_fail_under.__main__.Run",
                            return_value=_MockPylintResults(7.73)) as pl_mock:
                exit_code = main()

        pl_mock.assert_called_once_with(args=["my_pkg"], do_exit=False)
        assert exit_code == 1

    def test_default(self):
        """Verify that a score of 10 is required if not specified as an argument."""
        sys_args = [None, "my_pkg"]
        with mock.patch("sys.argv", sys_args):
            with mock.patch("pylint_fail_under.__main__.Run",
                            return_value=_MockPylintResults(10.0)):
                exit_code = main()
                assert exit_code == 0

            with mock.patch("pylint_fail_under.__main__.Run",
                            return_value=_MockPylintResults(9.9)) as pl_mock:
                exit_code = main()
                assert exit_code == 1

        pl_mock.assert_called_once_with(
            args=["my_pkg"], do_exit=False)

    def test_no_score(self):
        """Verify failure when no Pylint score is returned (i.e. fatal error)."""
        sys_args = [None, "--disable", "trailing-whitespace", "bad_pkg", "--fail_under", "9.5"]
        with mock.patch("sys.argv", sys_args):
            mock_pl_results = _MockPylintResults(9.3)
            del mock_pl_results.linter.stats["global_note"]
            with mock.patch("pylint_fail_under.__main__.Run",
                            return_value=mock_pl_results) as pl_mock:
                exit_code = main()

        pl_mock.assert_called_once_with(
            args=["--disable", "trailing-whitespace", "bad_pkg"], do_exit=False)
        assert exit_code == 2

    def test_help(self):
        """Verify printing usage information to the console if no arguments specified."""
        sys_args = [None]
        with mock.patch("sys.argv", sys_args):
            _stdout = sys.stdout
            sys.stdout = StringIO()
            exit_code = main()
            _printed = sys.stdout.getvalue()
            sys.stdout = _stdout

        assert "usage: pylint-fail-under [--fail_under SCORE] [Pylint Command Line Arguments]" in _printed
        assert exit_code == 0


if __name__ == "__main__":
    unittest.main()
