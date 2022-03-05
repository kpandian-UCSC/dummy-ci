from setuptools import setup, find_packages

setup(
    name='Databricks Test',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='none',
    description='An example python package with functions simulating depositing and withdrawing cash from a bank account',
    long_description=open('README.md').read(),
    py_modules=['src', 'src/secrets'],
    install_requires=[],
    url='REPOSITORY_URL',
    author='AUTHOR_NAME',
    author_email='AUTHOR_EMAIL'
)