from itertools import permutations

def tsp(cost):
    # Number of nodes
    numNodes = len(cost)
    nodes = list(range(1, numNodes))
    mincost = float('inf')

    # Generate all permutations of the remaining nodes
    for perm in permutations(nodes):
        currcost = 0
        currNode = 0

        # Calculate the cost of the current permutation
        for node in perm:
            currcost += cost[currNode][node]
            currNode = node

        # Add the cost to return to the starting node
        currcost += cost[currNode][0]

        # Update the minimum cost if the current cost is lower
        mincost = min(mincost, currcost)

    return mincost


if __name__ == "__main__":
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    res = tsp(cost)
    print(res)