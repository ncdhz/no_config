import setuptools
from os import path

with open(path.join('docs', 'README.md'), 'r', encoding='utf-8') as fh:
    long_description = fh.read()

about = {}

with open(path.join('no_config', '__init__.py'), 'r') as f:
    exec(f.read(), about)

setuptools.setup(
    name='no_config',
    version=about['__version__'],
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
