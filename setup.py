from setuptools import setup
import versioneer

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'margot',
    packages = ['margot'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='apache-2.0',
    description = 'An algorithmic trading framework for PyData.',
    long_description_content_type='text/markdown',
    long_description = long_description,
    author = 'Rich Atkinson',
    author_email = 'rich@airteam.com.au',
    url = 'https://github.com/atkinson/margot',
    download_url = '',
    keywords = ['quant', 'trading', 'systematic'],
    install_requires=[
            'numpy',
            'pandas',
            'scipy',
            'pyfolio',
            'trading-calendars',
            'versioneer',
            'pytz',
            'alpha_vantage',
            'tables'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3', 
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

