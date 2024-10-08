from setuptools import setup, find_packages





setup(
    name='django-unique-id-field',
    version='0.1.0',
    description='A Django Custom Model Field To Generate Random Unique ID -> (Characters & digits)',
    author="Moataz",
    author_email="motazfawzy73@gmail.com",
    url='https://github.com/Moataz0000/Django_generate_unique_ID_Field-',
    packages=find_packages(),
    install_requires=[
        'django>=3.0',
    ],
)