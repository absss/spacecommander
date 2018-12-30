# -*- coding: utf-8 -*-

import re

## TODO: 单行注释符号和内容之间空一格
from AbstractCustomFormatter import AbstractCustomFormatter

class SingleCommentAddSpace(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []
        for line in lines:
            if line.find('//') != -1 and (line.find('// ') == -1):
                line = line.replace('//','// ')
            lines_to_write.append(line)
    
        return "".join(lines_to_write)

if __name__ == "__main__":
    SingleCommentAddSpace().run()
