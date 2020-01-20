from setuptools import setup, find_packages

from gym_togyzkumalak.envs import TogyzkumalakEnv

with open("README.md", "r") as fh:
    long_description = fh.read()
    pass

version = TogyzkumalakEnv().__version__

setup(
    name='gym_togyzkumalak',
    version=version,
    description='Togyzkumalak is one of the version of mancala games',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Zhassulan Berdibekov',
    author_email='zhasulan87@gmail.com',
    install_requires=['gym', 'texttable', 'numpy'],
    packages=find_packages(),
    python_requires='>=3.6',
    url="https://github.com/zhasulan/gym-togyzkumalak",
)
