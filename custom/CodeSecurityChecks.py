# -*- coding: utf-8 -*-

import re

def containCopy(keywords):
    if 'copy' in keywords:
        return True
    return False

def containStrong(keywords):
    if 'strong' in keywords:
        return True
    return False

def containWeak(keywords):
    if 'weak' in keywords:
        return True
    return False

def containWeak(keywords):
    if 'weak' in keywords:
        return True
    return False

def containAssign(keywords):
    if 'assign' in keywords:
        return True
    return False

def wrongBlock(string):
    if string.find('^') != -1 and string.startswith('@property') and string.find('copy') == -1:
        return True
    return False

def isDelegate(string):
    if string.find('id<') != -1:
        return True
    return False

def check(s):
    if wrongBlock(s):
        return "block should use copy"
    pattern = "@property \((.*?)\) (\S+) *?\S+;"
    res = re.match(pattern,s)
    type = None
    Error = None;
    keywords = []
    useCopyTypeArray = ['NSArray','NSString','NSDictionary','NSSet','NSURLRequest']
    useAssignTypeArray = ['CGFloat','int','double','float','long','NSInteger','unsign','BOOL']
    if res:
        for s in res.groups()[0].split(','):
            s = s.strip()
            keywords.append(s)
            type = res.groups()[1]
    
        if type in useAssignTypeArray:
            if not containAssign(keywords):
                Error = '%s maybe should use %s'%(type,'assign')
        elif type in useCopyTypeArray:
            if not containCopy(keywords):
                Error = '%s maybe should use %s'%(type,'copy')
        elif isDelegate(type):
            if not containWeak(keywords):
                Error = '%s if it is a protocol,you should use weak,if not , you can use `// ignore check error to` to ignore it'%(type,'weak')
    return Error

## TODO: 格式检查
from AbstractCustomFormatter import AbstractCustomFormatter

class CodeSecurityChecks(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []
        previous_line = ''; #上一行
        for line in lines:
            error = check(line)
            origin_line = line
            if error and not previous_line.startswith('#warning check error') and not previous_line.startswith('// ignore check error'):
                line = '#warning check error:%s\n%s'%(error,line)
            lines_to_write.append(line)
            previous_line = origin_line
        return "".join(lines_to_write)

if __name__ == "__main__":
    CodeSecurityChecks().run()




