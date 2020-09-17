class MaxHeap:

    def __init__(self):
        self.queue = [None]

    def insert(self, value):
        # Insert the given value to the Heap
        """
        Input  >> value: int
        Output >> None
        """

        self.queue.append(value)

        i = len(self.queue) - 1
        while i > 1:
            parent = i // 2
            if self.queue[i] > self.queue[parent]:
                tmp = self.queue[i]
                self.queue[i] = self.queue[parent]
                self.queue[parent] = tmp
                i = parent
            else:
                break

    def delete(self):
        # Delete and return value of the root node
        """
        Input  >> None
        Output >> int
        """
        if len(self.queue) == 1:
            print("Heap is empty")
            return

        item = self.queue[1]
        self.queue[1] = self.queue[len(self.queue) - 1]
        self.queue[len(self.queue) - 1] = item

        self.queue.pop()

        i = 1
        while i <= len(self.queue) - 1:

            left = i * 2
            right = i * 2 + 1
            largest = i

            if left <= len(self.queue) - 1 and self.queue[left] > self.queue[largest]:
                largest = left

            if right <= len(self.queue) - 1 and self.queue[right] > self.queue[largest]:
                largest = right

            if largest != i:
                tmp = self.queue[i]
                self.queue[i] = self.queue[largest]
                self.queue[largest] = tmp
                i = largest
            else:
                break

        return item


def HeapSort(the_seq):
    # Sort and return the given list
    """
    Input  >> the_seq: List
    Output >> List
    """
    mh = MaxHeap()
    hslist = []
    result = []
    length = len(the_seq)
    for i in range(length):
        word = the_seq.pop()
        mh.insert(word)
    for j in range(length):
        mhword = mh.delete()
        hslist.append(mhword)
    for k in range(length):
        result.append(hslist.pop())
    return result


def main():
    seq = [5, 10, 2, 5, 7, 6, 15, 1]

    print("Input")
    print(seq)
    print("Result")
    print(HeapSort(seq))


main()
