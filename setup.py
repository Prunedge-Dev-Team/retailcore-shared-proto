import re
from setuptools import find_packages, setup

with open('retailcore_proto/__init__.py', 'rb') as f:
    version = str(eval(re.search(r'__version__\s+=\s+(.*)', f.read().decode('utf-8')).group(1)))

setup(
    name='retailcore_proto',
    version=version,
    description='RetailCore Shared Proto',
    url='https://github.com/Prunedge-Dev-Team/retailcore-shared-proto',
    author='Daniel Ale',
    author_email='daniel.ale@prunedge.com',
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: RetailCore Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
