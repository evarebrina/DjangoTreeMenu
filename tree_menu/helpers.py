def build_tree(items, path):
    result = []
    for item in items:
        if item.parent is None:
            result.append({'item': item, 'children': get_children(item, items), 'is_active': False})
    mark_active(result, path)
    return result


def get_children(item, l):
    res = []
    for i in l:
        if i.parent == item:
            d = {'item': i,
                 'children': get_children(i, l),
                 'is_active': False,
                 }
            res.append(d)
    return res


def mark_active(items, path):
    for i in items:
        if i['children']:
            i['is_active'] = mark_active(i['children'], path)
            if i['is_active']:
                return True
        if str(i['item'].url) in path:
            i['is_active'] = True
            return True

    return False
