def enq(data):
    global qsize
    global rear
    global front
    if (rear + 1) % qsize == front:
        # print('Full')
        front = (front + 1) % qsize
    rear = (rear + 1) % qsize
    q[rear] = data


front = 0
rear = 0
qsize = 4
q = [0] * qsize
enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
while front != rear:
    front = (front + 1) % qsize
    print(q[front])