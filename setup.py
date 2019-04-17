from setuptools import setup

setup(name='cm_scraper',
      version='0.1',
      description='A variety of scraping tools',
      url='http://github.com/chadmiko/cm_scraper',
      author='Chad Miko',
      author_email='chadmiko@gmail.com',
      license='MIT',
      packages=['cm_scraper'],
      install_requires=[
            'requests',
            'bs4'
      ],
      zip_safe=False)
