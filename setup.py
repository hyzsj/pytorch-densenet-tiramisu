from setuptools import setup, find_packages

setup(
    name='DenseNet',
    version='0.1.0',
    description='PyTorch implementation of DenseNet and FCDenseNet',
    author='Federico Baldassarre',
    author_email='baldassarre.fe@gmail.com',
    url='https://github.com/baldassarreFe/pytorch-densenet-tiramisu',
    packages=find_packages(exclude='test'),
)
