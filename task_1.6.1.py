hierarchy = {}


def is_parent(classes_: list):
    if len(classes_) == 1:
        classes_.append(classes_[0])
    parent = classes_[0]
    child = classes_[1]
    if parent in hierarchy:
        if child in hierarchy[parent]:
            return 'Yes'
    return 'No'

def request_split(request):
    return request.split(' : ')

def create_ratio(child_parent_raio):
    child = child_parent_raio[0]


def add_ratio_pair(request: str):
    child = request[0]
    parent = request[4]
    update_hierarchy(parent, child)


def add_ratio_single(request):
    update_hierarchy(request, request)


def add_ratio_few(request: str):
    child = request[0]
    parents_list = request[4:].split(' ')
    for parent in parents_list:
        update_hierarchy(parent, child)


def update_hierarchy(parent, child):
    if parent not in hierarchy:
        hierarchy.update({parent: [child]})
    else:
        hierarchy[parent].append(child)


n = int(input())
for i in range(n):
    classes = input()
    str_len = len(classes)
    if str_len == 1:
        add_ratio_single(classes)

    if str_len > 5:
        add_ratio_few(classes)
    elif str_len > 1:
        add_ratio_pair(classes)
    else:
        add_ratio_single(classes)


q = int(input())
for i in range(q):
    classes = input().split(' ')
    print(is_parent(classes))

print(hierarchy)
