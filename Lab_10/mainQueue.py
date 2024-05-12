# Patrick Roscio
# Lab_6 mainQueue.py
# Description: From the queue.py file, imports classes "queue" and "EmptyQueueXxception" After reading in the input queue file, the 
# first string in the line is denoted as the opperation, for each possible opperation, a try/except statment is ran to call in the queue 
# functions to enqueue, Peek, dequue, or Clear the queue. If the opperation cannot be ran, the exeption is called informing the user that the
# opperation could not be preformed

from Queue import Queue, EmptyQueueException 

def main():
    queue = Queue()
    with open("Lab_10/inputQueue.txt","r") as file:
        for line in file:
            opperation =line.strip().split()
            if opperation:
                command = opperation[0]
                if command == "peek":
                    try:
                        value = queue.peek()
                        print(f"Peek: {value}")
                    except EmptyQueueException as e:
                        print(e)
                elif command == "enqueue":
                    try:
                        value = opperation[1]
                        queue.enQueue(value)
                        print(f"Queued: {value}")
                    except EmptyQueueException as e:
                        print(e)
                elif command == "dequeue":
                    try:
                        value = queue.deQueue()
                        print(f"De-Queued: {value}")
                    except EmptyQueueException as e:
                        print(e)
                elif command == "clear":
                    queue.clear()
                    print("Queue cleared.")
                else:
                    print(f"All values in the Queue: {queue}")
main()



