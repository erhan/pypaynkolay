from setuptools import setup

setup(
    name='pypaynkolay',
    version="0.0.1",
    packages=['pypaynkolay'],
    description='Paynkolay pos api python wrapper',
    url='https://github.com/erhan/pypaynkolay',
    author='Erhan Bte',
    license='MIT',
    author_email='',
    install_requires=[
        'requests',
    ],
    keywords='Paynkolay pos api python wrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)