from queue import Queue
import threading

# class worker:
class   Worker(threading.Thread):

    def run(self):
        print("> worker")

queue = Queue(3)

thread1 = Worker()
thread2 = Worker()
thread3 = Worker()

threadList = [
            thread1,
            thread2,
            thread3
            ]

print("queue_size: ", queue.qsize())
print("queue_empty: ", queue.empty())
print("queue_full: ", queue.full())

for element in threadList:
    queue.put(element)

for index in range(0, 3):
    queue.get().start()

thread1.join()
thread2.join()
thread3.join()
