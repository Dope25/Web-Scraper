# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
n_groups = int(input())
groups_dict = dict.fromkeys(groups)

for i in range(n_groups):
    n_children = int(input())
    groups_dict[groups[i]] = n_children

print(groups_dict)
