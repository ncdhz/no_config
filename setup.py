import setuptools
from . import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='no_config',
    version=__version__,
    author='ncdhz',
    author_email='ncdhz@qq.com',
    description='Simple configuration handling in Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ncdhz/no_config',
    python_requires='>=3.7',
    install_requires=[
        'PyYAML',
        'toml'
    ],
    packages=setuptools.find_packages()
)
