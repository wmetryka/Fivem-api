import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='fivem',  

     version='1.0.1',

     scripts=['fivem.py'] ,

     author="Wiktor Metryka",

     author_email="jestemkiosk@gmail.com",

     description="A Python wrapper for the FIVEM API.",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/Jestemkioskiem/Fivem-api/",

     install_requires=['requests'],

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
