from setuptools import setup, find_packages

VERSION = "1.0"
DESCRIPTION = "A quick way to crawl around the web"
LONG_DESC = "With this package, you can choose to webscrape a webpage or live scrape a webpage with an interface displaying what is being done in the background"


setup(
    name="QuickCrawl",
    version="2.0",
    author="Gabriel Mendieta Hernandez",
    author_email="gmendieta4109@cristorey.net",
    description=DESCRIPTION,
    long_description=LONG_DESC,
    packages=find_packages(),
    install_requires=[
        "selenium",
        "requests",
        "beautifulsoup4",
        "colorama",
        "click",
        "lxml",
        "webdriver_manager"
    ],
    url="https://github.com",
    keywords=["python", "spider", "quick", "crawl", "crawl", "live", "scrape"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
