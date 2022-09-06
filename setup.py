from setuptools import setup, find_packages

setup(
    name="melkor_engine",
    version="1.0",
    author="Yiqi Sun (Zongjing Li)",
    author_email="ysun697@gatech.edu",
    description="Melkor Concept Engine.",

    # project main page
    url="http://jiayuanm.com/", 

    # the package that are prerequisites
    packages=find_packages(),
    package_data={
        '':['melkor_engine'],
        'bandwidth_reporter':['melkor_engine']
               },
)