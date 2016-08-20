#!/usr/bin/python
import sys
import glob
import os

sys.path = ["../"] + sys.path
import CppHeaderParser

os.chdir(".")

for file_name in glob.glob("*.hpp"):
    try:
        cppHeader = CppHeaderParser.CppHeader(file_name)
        for class_name, class_items in cppHeader.classes.items():
            print "struct Mock"+class_name+" : "+class_name+" {"
            for public_method in class_items["methods"]["public"]:
                if not public_method["constructor"] and not public_method["destructor"]:
                    print "    MOCK_<const>METHOD_<arg_count>(<name>, <return>(<args>));".\
                        replace('<const>', 'CONST_' if public_method["const"] else '').\
                        replace('<arg_count>', str(len(public_method["parameters"]))).\
                        replace('<name>', public_method["name"]).\
                        replace('<return>', public_method["returns"]).\
                        replace('<args>', ', '.join("%s" % (parameter["type"]) for parameter in public_method["parameters"]))
            print "};"
    except CppHeaderParser.CppParseError as e:
        print(e)
        sys.exit(1)