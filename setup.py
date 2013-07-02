from setuptools import find_packages, setup

setup(
    name='allegro',
    version='0.1.2',
    author='Malwina Nowakowska',
    author_email='malwina.nowakowska@stxnext.pl',
    packages=find_packages(),
    test_suite="allegro.tests",
    entry_points='''\
        [console_scripts]
        allegro=allegro.script:main
    ''',
    description='allegro browser',
    long_description='README.txt',
    install_requires=[
        'python >= 2.7',
        'lxml',
        'mock',
        'beautifulsoup4',
        'mechanize'
    ],
)
