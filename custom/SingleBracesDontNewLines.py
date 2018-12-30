# -*- coding: utf-8 -*-

## TODO: 单个括号一行放到上一行中去
from AbstractCustomFormatter import AbstractCustomFormatter

class SingleBracesDontNewLines(AbstractCustomFormatter):
    def format_lines(self, lines):
        lines_to_write = []
        previous_line = ''; #上一行
        for line in lines:
            
            stripped_line = line.strip()
            
            if stripped_line == "{":
                if previous_line.endswith('\n'):
                    previous_line = previous_line[:-1]
                    previous_line += " {\n"
                    line = ''
            lines_to_write.append(previous_line) ## 添加上一行
        
            previous_line = line;
        
        lines_to_write.append(previous_line); ## 加最后一行
        return "".join(lines_to_write)

if __name__ == "__main__":
    SingleBracesDontNewLines().run()
