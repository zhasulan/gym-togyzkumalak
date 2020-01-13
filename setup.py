from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gym_toguzkumalak',
    version='0.0.3',
    description='Toguzkumalak is a one of the version of mancala games',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Zhassulan Berdibekov',
    author_email='zhasulan87@gmail.com',
    install_requires=['gym', 'texttable'],
    packages=find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    python_requires='>=3.6',
    url="https://github.com/zhasulan/gym-toguzkumalak",
)
