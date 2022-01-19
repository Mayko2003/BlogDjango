from django import template
register = template.Library()



@register.filter
def next_page(path, arg):
    prev = str(arg - 1)
    arg = str(arg)
    if '?' in path and 'page' not in path:
        path = path + '&page=' + arg
    else:
        if 'page' in path:
            path = path.replace('page=' + prev, 'page=' + arg)
        else:
            path = path + '?page=' + arg
    prev = arg
    return path

@register.filter
def prev_page(path,arg):
    prev = str(arg + 1)
    arg = str(arg)
    if '?' in path and 'page' not in path:
        path = path + '&page=' + arg
    else:
        if 'page' in path:
            path = path.replace('page=' + prev, 'page=' + arg)
        else:
            path = path + '?page=' + arg
    prev = arg
    return path
