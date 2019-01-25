def camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(camel('guvi geek'))
