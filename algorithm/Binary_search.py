'''
@Author: Ralph
@Type_file: Python
@Date: 2020-07-25 19:10:23
@LastEditTime: 2020-07-25 19:34:52
@FilePath: \workbeach\algorithm\Binary_search.py
@Effect: 二分查找逻辑
'''


def B_S(list_item, item):
    # 最开始的引索
    new_index = 0
    # 整个列表的最终下标
    All_index = len(list_item)
    # 循环查找对应的下标
    while new_index < All_index:
        # 第一次需要查找的引索
        mid = int((new_index + All_index)/2)
        # 在列表中查找到的的引索的对应的值
        index_value = list_item[mid]
        # 如果第一次查找就找到了就返回对应的值
        if index_value == item:
            return mid
        # 如果找到的值比原来大 再次查找把一次找到的引索认定新的最大的列表引索 从新查找
        if index_value > item:
            All_index = mid
        else:
            # 如果是比他小 那么小的引索+1 重新查找
            new_index = mid + 1
    return None


if __name__ == "__main__":
    list_item = [1, 3, 5, 7, 9, 23, 43, 57, 58, 60, 76, 89, 100]
    index = B_S(list_item, 43)
    print('find the index is {0}，value is {1}'.format(index, list_item[index]))
