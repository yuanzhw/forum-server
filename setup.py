import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='forum',
    version='1.0.0',
    url='https://github.com/yuanzhw/forum-server',
    license='BSD',
    maintainer='Yuanzhw',
    maintainer_email='yuanzhw@vip.qq.com',
    description='A Forum Demo with Flask',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'sqlalchemy',
        'redis',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
