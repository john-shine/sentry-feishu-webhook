#!/usr/bin/env python

from setuptools import setup, find_packages
from src.sentry_feishu import VERSION

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='sentry-feishu-webhook',
    version=VERSION,
    author='john',
    author_email='mr.john.shine@gmail.com',
    url='https://github.com/john-shine/sentry-feishu-webhook',
    description='Sentry plugin that send errors exceptions to FeiShu client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='sentry feishu webhook',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_feishu = sentry_feishu.plugin:FeiShuPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)
