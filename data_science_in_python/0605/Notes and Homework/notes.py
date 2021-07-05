'''
Notes for Liam's Lab June 5, 2021
Code used to run things in the "June 5, 2021 Notes.pdf" file
'''


array = [1, -10, 2, 3, 4]

def BubbleSort(array):
    
    for i in range(len(array)):
        for j in range(len(array)-i-1):

            if array [j] > array [j+1]:
                array [j], array [j+1] = array [j+1], array [j]
    print(array)

BubbleSort(array)

#Output: [-10, 1, 2, 3, 10]

graph = {
    '1': ['3', '7'],
    '7': ['1', '2'],
    '3': [],
    '2': ['8'],
    '8': ['3']
}

visited = set()

def DepthFirstSearch(visited, graph, node):

    if node not in visited:
        print(f'Hey I found {node}')
        visited.add(node)
        for neighbor in graph[node]:
            DepthFirstSearch(visited, graph, neighbor)

print('Hey let me climb down this tree, watch me go \n', DepthFirstSearch(visited, graph, '1'))

l = ["H","e","l","l","o"," ","w","o","r","l","d"]
print(('').join(l))

l = [1, 1, 1, 1, 1, 1, 1]
print(f'There are {l.count(1)} 1s')
print(set(l))

bean_count = 0
the_jar = ['bean', 'bean', 'bean', 'bean', 'bean', 'bean']
for every_bean in the_jar:
    bean_count = bean_count + 1
print(f'There are {bean_count = } beans!')
