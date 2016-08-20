#!/usr/bin/python
import sys
import glob
import os
import CppHeaderParser as Parser

out_file_name = 'output.hpp'
result = ''

os.chdir('.')

for file_name in (f for f in glob.glob('*.hpp') if f != out_file_name):

        try:
            header = Parser.CppHeader(file_name)

            for class_name, class_items in header.classes.items():

                result += 'struct Mock' + class_name + ' : ' + (class_items['namespace'] + "::" if class_items['namespace'] else '') + class_name + ' {\n'

                for method in (m for m in class_items['methods']['public'] if not m['constructor'] and not m['destructor']):

                        result += '    MOCK_<const>METHOD_<arg_count>(<name>, <return>(<args>));\n'.\
                            replace('<const>', 'CONST_' if method['const'] else '').\
                            replace('<arg_count>', str(len(method['parameters']))).\
                            replace('<name>', method['name']).\
                            replace('<return>', method['returns']).\
                            replace('<args>', ', '.join('%s' % (param['type']) for param in method['parameters']))

                result += '};\n\n'

        except Parser.CppParseError as e:
            print(e)
            sys.exit(1)

out_file = open(out_file_name, 'w')
out_file.writelines(result)
out_file.close()

print 'generating:\n'
print result
print 'success! see output.hpp'