from setuptools import setup

from pathlib import Path
root_folder = Path(__file__).parent
long_description = (root_folder / "README.md").read_text()

setup(
    name='py-mrandom',
    version='0.1',
    description='mrandom is a library for generating random numbers.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sidharth Mudgil',
    packages=['mrandom'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
