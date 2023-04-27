<p align="center"><h1>💡 Simple Stemmer</h1></p>
[![Generic badge](https://img.shields.io/badge/languge-polish-red.svg)](https://shields.io/)

A simple stemmer based on Porter stemmer for polish langage.

This file is a modification of _pl_stemmer_ library.

**[Go to pl_stemmer](https://github.com/Tutanchamon/pl_stemmer/tree/master)**

ℹ️ **NOTE:** Changes between simple_stemmer and pl_stemmer: 
> * Support for Python 3
> * No file handling only raw text
> * Consistent output as an object 
> * Added text cleaning class

ℹ️ **HOW TO USE:**
> python simple_stemmer.py "To jest przykładowe zdanie w języku polskim"

> [('To', 'to'), ('jest', 'jest'), ('przykładowe', 'przykład'), ('zdanie', 'zdan'), ('w', 'w'), ('języku', 'język'), ('polskim', 'polskim')]
