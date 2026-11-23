
queue = [10, 20, 30]
max = 5

def traverse():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Queue elements:")
        for i in range(len(queue)):
            print(queue[i])

print("Queue:", queue)
traverse()
