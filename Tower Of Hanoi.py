# Tower of hamoi
def tower_of_hanoi(n, source, destination, aux):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return

    tower_of_hanoi(n - 1, source, aux, destination)

    print("Move disk", n, "from rod", source, "to rod", destination)
    tower_of_hanoi(n - 1, aux, destination, source)


n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')

# Path: Tower Of Hanoi.py