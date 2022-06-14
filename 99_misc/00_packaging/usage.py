# Using a package defined internally
# Refer to pycparser/examples/explore_ast.py for more details

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
import sys
sys.path.extend(['.', '..'])

from int_package.TestClass import TestClass
t = TestClass()