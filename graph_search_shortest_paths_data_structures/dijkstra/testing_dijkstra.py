from heap_dijkstra import dijkstra
from naive_dijkstra import naive_dijkstra

# function built for using the stanford algs tester
# tester looks for function named alg by default
# solution is string of ints repr shortest paths from 1 to 7,37,59,82,99,115,133,165,188,197

# Heap implementation passes all tests. Naive no.


def dijkstra_test_wrapper(filename):
    "Wrapper for dijkstra implementation used with course tester file"

    source_vertex = '1'
    shortest_paths_dict = dijkstra(filename, source_vertex)

    nodes = "7,37,59,82,99,115,133,165,188,197".split(',')  # by assignment
    res = ''

    for node in nodes:
        res = res + f"{shortest_paths_dict[node]},"

    return res[:-1]  # remove trailing comma


filename = 'test_cases/input_random_1_4.txt'  # pass
if __name__ == "__main__":
    res = dijkstra_test_wrapper(filename)
    print(res)