puppet [![travis](https://img.shields.io/travis/poying/puppet.svg?style=flat)](https://travis-ci.org/poying/puppet)
======

__main feature__: git-like subcommands. Others can write third-party subcomand in there favorite language. [example](./examples/simple)

```bash
$ pip install puppet
```

## Quick Start

### Write usage information/configuration

```python
'''
    Usage: json-prettify [options] json

    Options:

        -h, --help                 output this information
        -V, --version              output the version number
        -i, --indent=<int>         [default: 4]
        -s, --sort                 [default: True]
'''
```

[option types](./puppet/parser/doc.py#L37)

### Start cli program

```python
from puppet import puppet

puppet('simple', '0.1.0')
```

### Define `main` function

`main` is a entry point of our cli program

```python
def main(program):
    # do something
```

### Custom option handler

```python
def option_name_or_alias_name(program, value):
    # do something

def help(program, value):
    print('custom usage information')
    sys.exit()
```

## Examples

[./examples](./examples)

## API

* program.flags
* program.usage
* program.args
* program.doc
    * program.doc['sections'][section_name]

## License

The MIT License

Copyright © 2014

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
