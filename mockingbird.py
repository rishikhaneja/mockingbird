#!/usr/bin/python
import sys
import glob
import os
import CppHeaderParser

os.chdir('.')

out_file = 'output.hpp'
result = ''

for file_name in glob.glob('*.hpp'):
    if file_name != out_file:
        try:
            cppHeader = CppHeaderParser.CppHeader(file_name)
            for class_name, class_items in cppHeader.classes.items():
                result += 'struct Mock'+class_name+' : '+class_name+' {\n'
                for public_method in class_items['methods']['public']:
                    if not public_method['constructor'] and not public_method['destructor']:
                        result += '    MOCK_<const>METHOD_<arg_count>(<name>, <return>(<args>));\n'.\
                            replace('<const>', 'CONST_' if public_method['const'] else '').\
                            replace('<arg_count>', str(len(public_method['parameters']))).\
                            replace('<name>', public_method['name']).\
                            replace('<return>', public_method['returns']).\
                            replace('<args>', ', '.join('%s' % (parameter['type']) for parameter in public_method['parameters']))
                result += '};\n'
        except CppHeaderParser.CppParseError as e:
            print(e)
            sys.exit(1)
mock_file = open(out_file, 'w')
mock_file.writelines(result)
mock_file.close()
print 'generating:'
print result
print 'success! see output.hpp'