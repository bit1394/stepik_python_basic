namespaces = {'global': {'parent': None, 'vars': []}}


def create(namespace: str, parent: str) -> None:
    namespaces.update({namespace: {'parent': parent, 'vars': []}})


def add(namespace: str, var: str) -> None:
    namespaces[namespace]['vars'].append(var)


def get(namespace: str, var: str):
    if namespace in namespaces:
        if var in namespaces[namespace]['vars']:
            return namespace
        else:
            parent_space = namespaces[namespace]['parent']
            return get(parent_space, var)


n = input()
for i in range(n):
    method, name_space, obj = input().split()
    if method == 'create':
        create(name_space, obj)
    elif method == 'add':
        add(name_space, obj)
    else:
        print(get(name_space, obj))
