from setuptools import setup, find_packages

setup(
    name='pacote-process-imagem',
    version='0.1.0',
    author='Sérgio Santos',
    author_email='seuemail@example.com',
    description='Pacote Python para processamento básico de imagens.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Santosdevbjj/pacoteProcessImagem',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['Pillow>=10.0.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8',
)
