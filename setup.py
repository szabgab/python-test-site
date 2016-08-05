from setuptools import setup

setup(
    name='demo',
    packages=['demo'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    #setup_requires=[
    #    'pytest-runner',
    #],
    #tests_require=[
    #    'pytest',
    #],
)
