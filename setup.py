from setuptools import setup, find_packages


setup(
    name='presto',
    version='0.1',
    description="A demo API",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector'
)
