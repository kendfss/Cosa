from setuptools import setup, find_packages

with open('readme.md', 'r') as fob:
    long_description = fob.read()
with open('requirements.txt', 'r') as fob:
    requirements = fob.readlines()

setup(
    name='cosa',
    version='0.0.1',
    author='Kenneth Sabalo',
    author_email='kennethsantanasablo@gmail.com',
    url='https://github.com/kendfss/cosa',
    description="CLI wrapper for common compilers",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='utilities operating path file system local server web',
    license='GNU GPLv3',
    requires=requirements,
    entry_points={
        'console_scripts': [
            'cmpy = cmpy.cli:main'
        ]
    },
    python_requires='>=3.8',
)