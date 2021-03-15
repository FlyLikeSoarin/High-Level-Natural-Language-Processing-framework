from setuptools import setup

setup(
    name='odin-nlp',
    description='Easy to use NLP framework will nocode workflow',
    version='0.1.0',
    author='Vikhrev Evgeny',
    author_email='e.vikhrev@phystech.edu',
    license='MIT',
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Text Processing ',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['odin_nlp'],
    entry_points={
        'console_scripts': [
            'odin = odin_nlp.cli:run'
        ],
    },
)
