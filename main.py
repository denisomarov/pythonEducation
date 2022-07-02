# # Решение примеров для изучения алгоритмов на языке Phyton
#
# # Разработка процедуры быстрого поиска
# # Бинарный поиск
# def BFind(list, n):
#
#     # list - упорядоченный список для поиска
#     # n - искомое число
#     # процедура выдает позицию и количество шагов поиска
#
#     list_ = list                 # дублируем список
#     start = 0                    # первая позиция списка
#     end = len(list_)             # последняя позиция списка
#     p = (end-start) // 2         # позиция для проверки
#     v = list_[p]                 # значение под номером p
#     step = 0
#
#     while  v != n:
#
#         step = step +1
#         if v > n:
#             end = p-1
#         else:
#             start = p+1
#
#         p = start + (end - start) // 2
#         v = list_[p]
#
#     return p+1, step
#
# def BFind2(list, item):
#     low = 0
#     high = len(list)-1
#     step = 0
#
#     while low<=high:
#         step = step + 1
#         mid = (low+high) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid+1, step
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# list_s = [1,2,3,4,5,6,7,8,9,10]
# # print(BFind(list_s, 10))
# print(BFind2(list_s, 10))



# # Сортировка массива по возрастанию
# # процедура поиска индекса наименьшего элемента
#
# def SmallestInd(arr):
#     smallest_value = arr[0]
#     smalliest_index = 0
#
#     for i in range(1, len(arr)):
#         if arr[i]<smallest_value:
#             smallest_value = arr[i]
#             smalliest_index = i
#
#     return smalliest_index
#
# def SortArr(arr):
#
#     NewArr = [0,0,0,0,0,0,0,0,0,0]
#     for i in range(0,len(arr)):
#         smallest_value_index = SmallestInd(arr)
#         NewArr[i] = arr[smallest_value_index]
#         arr.remove(arr[smallest_value_index])
#
#     return NewArr
#
# Arr1 = [10,9,8,7,6,5,4,3,2,1]
# print(SortArr(Arr1))

# Глава 4.
# Напишите код для функции sum
#
# def sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#     return arr[0]+sum(arr[1:])
#
# Поиск количества элементов методом рекурсии
#
# def count(arr):
#     if len(arr) == 1:
#         return 1
#     return 1+count(arr[1:])
#
# Поиск наибольшего значения методом рекурсии
#
# def FindMax(arr):
#     if len(arr) == 1:
#         return arr[0]
#     sub_max = FindMax(arr[1:])
#     if sub_max < arr[0]:
#         sub_max = arr[0]
#     return sub_max
#
# Алгоритм быстрой сортировки
#
# def quicksort(arr):
#     if len(arr) <2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i < pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         list_ = quicksort(less)
#         list_.append(pivot)
#         list_ = list_+quicksort(greater)
#         return list_
#
# Глава 6. Поиск в ширину
# Функция поиска в ширину

# from collections import deque
#
# def serch(name):
#     serch_queue = deque()
#     serch_queue += graph[name]
#     searched = []
#     while serch_queue:
#         person = serch_queue.popleft()
#
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person,' is mango seller!')
#                 return True
#             else:
#                 serch_queue += graph[person]
#                 searched.append(person)
#     return False
#
# def person_is_seller(name):
#     return name == 'jonny'
#
# graph = {}
# graph['you'] = ['alise', 'bob', 'clair']
# graph['bob'] = ['anuj', 'peggie']
# graph['alise'] = ['peggie']
# graph['clair'] = ['thom', 'jonny']
# graph['anuj'] = []
# graph['peggie'] = []
# graph['thom'] = []
# graph['jonny'] = []
#
# print(serch('you'))


#
# arr_ = [1,20,3,4]
# # print(sum(arr_))
# # print(count(arr_))
# #print(FindMax(arr_))
# print(quicksort(arr_))

# Глава 7. Алгоритм Дейкстры
# Функция реализации алгоритма Дейкстры

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)



print(graph)
print(costs)
print(parents)
