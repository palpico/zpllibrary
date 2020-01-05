import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Scott Walker",
    author_email="scott.david.walker@hotmail.com",
    name='zpllibrary',
    license="MIT",
    description='zpllibrary is a python package to create zpl simply.',
    version='v1.0.3',
    long_description=README,
    url='https://github.com/scott-david-walker/zpllibrary/tree/master/zpllibrary',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['pillow==7.0.0'],
    long_description_content_type='text/markdown',
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)