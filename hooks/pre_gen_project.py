import re
import sys

MODULE_NAME = '{{ cookiecutter.module_name }}'
PACKAGE_NAME = '{{ cookiecutter.package_name }}'

def error(msg: str):
    print(msg, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    if not re.fullmatch(r'(:[a-zA-Z]\w*)+', MODULE_NAME):
        error("Invalid module name")
    package_segments = PACKAGE_NAME.split(".")
    if len(package_segments) <= 1:
        error("Package name must have at least one '.' separator")
    if not all([ re.fullmatch(r'^[a-zA-Z]\w*', seg) for seg in package_segments ]):
        error("Package segments must be of non zero length and should start with a letter")