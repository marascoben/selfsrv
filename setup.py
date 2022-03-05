from setuptools import setup

setup(
    name='selfsrv',
    packages=['selfsrv'],
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv',
    ],
)