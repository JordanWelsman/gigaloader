# Module imports
from setuptools import setup

# Arguments
version = "1.0.0" # update __init__.py
python_version = ">=3.10"

# Long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# Define list of submodules
py_modules = ["gigaloader"]

# Run stup function
setup(
    name = 'gigaloader',
    version = version,
    description = 'A simple but verbose Python loading bar.',
    license='MIT',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'Jordan Welsman',
    author_email = 'jordan.welsman@outlook.com',
    url = 'https://pypi.org/project/gigaloader/',
    download_url='https://github.com/JordanWelsman/gigaloader/tags',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
        'Topic :: Utilities'
    ],
    package_data = {
      'gigaloader': py_modules
      },
    python_requires=python_version,
    install_requires = [
        "jutl>=0.5.0,<0.6.0"
    ],
    keywords='python, status, terminal, verbose, loading-bar, qol'
)