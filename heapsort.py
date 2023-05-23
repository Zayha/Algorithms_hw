def change_pos(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def build_tree(lst, size, root_index, direction):
    left_child_element = root_index * 2 + 1
    right_child_element = root_index * 2 + 2
    root_max = root_index

    def compare(x, y):
        if direction == 'asc':
            return x < y
        else:
            return x > y

    if left_child_element < size and compare(lst[root_index], lst[left_child_element]):
        root_max = left_child_element

    if right_child_element < size and compare(lst[root_max], lst[right_child_element]):
        root_max = right_child_element

    if root_max != root_index:
        change_pos(lst, root_index, root_max)
        build_tree(lst, size, root_max, direction)


def heap_sort(sortable_list, direction='asc'):
    sortable_list_size = len(sortable_list)
    for i in range(sortable_list_size // 2 - 1, -1, -1):
        build_tree(sortable_list, sortable_list_size, i, direction)

    for j in range(sortable_list_size - 1, 0, -1):
        change_pos(sortable_list, j, 0)
        build_tree(sortable_list, j, 0, direction)
    return sortable_list


def main():
    lst = [6, 6, 5, 4, 88, 41, 0, 12, 2, 3, 9]
    print(f'Исходный список:                {lst}')
    print(f'Отсортированный по возростанию: {heap_sort(lst)}')
    print(f'Отсортированный по убыванию:    {heap_sort(lst, "desc")}')


if __name__ == '__main__':
    main()
