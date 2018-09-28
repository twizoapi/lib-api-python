from setuptools import setup

setup(
    name='twizo-lib-python',
    description='Connect to the Twizo API using Python.',
    version='0.1',
    author='Yarince Martis',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Library',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='twizo 2fa security sms',
    author_email='infor@twizo.com',
    url='https://www.twizo.com',
    packages=['app'],
    install_requires=[
        "requests"
    ],
    extras_require={
        'test': ['coverage'],
    }
)
