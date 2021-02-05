import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='project_24',
    version='0.0.1',
    author='Laurynas Grusas',
    author_email='laurynas.grusas@gmail.com',
    description='Creating API using Flask to predict car prices for Turing College 2.4 capstone project',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)