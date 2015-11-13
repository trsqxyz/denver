#! usr/bin/python
# -*- coding: utf-8 -*-
"""
This script outputs your Deveropment Environment Version(Deever)
to Markdown file.

Usage:
  toolsver [-h] [-o=<output>]

Options:
  -h --help    show this
  -o=<output>  named output file [default: ./ENVIRONMENT.md]
"""

import pip
import platform
from datetime import datetime
from collections import OrderedDict
from docopt import docopt

class Deever():
    def __init__(self, outp):
        self.outp = str(outp)
        self.freeze = pip.operations.freeze.freeze

    def get_environment(self):
        return [
            datetime.now().isoformat(" ").lstrip(),
            "Python " + platform.python_version(),
            "Compiler: " + platform.python_compiler(),
            "Implementation: " + platform.python_implementation()
        ]

    def get_os_version(self):
        return [platform.version(), platform.processor()]

    def get_modules_version(self):
        return [_ for _ in self.freeze()]

    def set_environment(self):
        return OrderedDict([
            ("# ENVIRONMENT", self.get_environment()),
            ("## OS", self.get_os_version()),
            ("## MODULES", self.get_modules_version()),
        ])

    def write_environment(self):
        with open(self.outp, "w") as f:
            for k, vs in self.set_environment().items():
                f.write("{0}".format(k) + "  \n")
                for v in vs:
                    v = v.rstrip("\n") + "  \n"
                    f.write("{0}".format(v))


def main(outp):
    D = Deever(outp)
    D.write_environment()
    return "Everything is OK"

if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0')
    print(main(args["-o"]))
