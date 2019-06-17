import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    install_requires = [
        'pylint',
        ],

    name             = 'pylint-fail-under',
    version          = '0.2.0',
    author           = 'Tyler N. Thieding',
    author_email     = 'python@thieding.com',
    maintainer       = 'Tyler N. Thieding',
    maintainer_email = 'python@thieding.com',
    url              = 'https://github.com/TNThieding/pylint-fail-under',
    description      = 'Pylint wrapper that verifies code reaches a minimum quality score.',
    long_description = long_description,
    download_url     = 'https://github.com/TNThieding/pylint-fail-under',
    classifiers      = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Quality Assurance',
        ],
    license          = 'MIT License',
    packages=setuptools.find_packages(),

    entry_points = {
        'console_scripts': [
            'pylint-fail-under=pylint_fail_under.__main__:main'
        ]
    }
)