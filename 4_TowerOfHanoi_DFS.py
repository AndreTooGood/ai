def tower_of_hanoi(n, source, dest, aux):
    if n == 1:
        print(f"Move Disk 1 from {source} to {dest}")
        return
    tower_of_hanoi(n-1, source, aux, dest)
    print(f"Move Disk {n} from {source} to {dest}")
    tower_of_hanoi(n-1, aux, dest, source)
    
while True:
    try:
        num_disks = int(input("Enter number of disks: "))
        if num_disks > 0:
            break
        else:
            print("Invalid input. Enter a positive integer.")
    except ValueError:
        print("Invalid error. Enter a integer.")
        
tower_of_hanoi(num_disks, "A", "B", "C")