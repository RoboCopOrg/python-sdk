from setuptools import setup, find_packages

setup(
    name="pythonsdk",
    version="0.1.0",
    description="A simple Python SDK that provides a sayHello() method and CLI.",
    author="Harish Ved",
    author_email="ved.harish3@gmail.com",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        'console_scripts': [
            'sayHello=pythonsdk.cli:cli',
        ],
    },
    python_requires='>=3.6',
    include_package_data=True,
    license="MIT",
)
