from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as file:
    long_description = file.read()

setup(
    name="async-whatsapp-api-client-python",
    version="0.0.9",
    description=(
        "This library helps you easily create"
        " a Python application with WhatsApp API."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dark04072006",
    author_email="Abrekovalim38702@gmail.com",
    url="https://github.com/Dark04072006/async-whatsapp-api-client-python",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    license=(
        "Creative Commons Attribution-NoDerivatives 4.0 International"
        " (CC BY-ND 4.0)"
    ),
    install_requires=[
        "httpx==0.26.0"
    ],
    python_requires=">=3.10"
)
