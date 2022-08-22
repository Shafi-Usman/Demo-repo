import textwrap

def wrap(string, max_width):
    while max_width!=0:
        print(string[0:max_width])
        string = string.replace(string[0:max_width],"")
        if len(string) < max_width:
            break
    return string #return '\n'.join(textwrap.wrap(string,max_width))
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)