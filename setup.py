import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='fivem',  

     version='0.1',

     scripts=['fivem'] ,

     author="Wiktor Metryka",

     author_email="jestemkiosk@gmail.com",

     description="A Python wrapper for the FIVEM API.",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/javatechy/fivem_api",

     packages=['requests'],

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )