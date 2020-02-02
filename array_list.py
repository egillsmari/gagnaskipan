class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self, size, capacity=0):
        self.size = 6
        self.capacity = 6
        self.arr = [1,2,3,4,5]

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""

        for i in range(0, self.size):
            if i == self.size-1:
                return_string += str(self.arr[i])
                return return_string
            return_string += str(self.arr[i])+ ", "

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if self.size == self.capacity:
            arr_lis.resize()
        for i in range(self.size, 0, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[0] = value
        self.size+=1

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index > self.size-1 or index < 0:
            raise IndexOutOfBounds()
        if self.size == self.capacity:
            arr_lis.resize()
        for i in range(self.size, 0, -1):
            if i != index-1:
                self.arr[i] = self.arr[i-1]
        self.arr[index] = value
        self.size+=1


    #Time complexity: O(1) - constant time
    def append(self, value):
        if self.size == self.capacity:
            arr_lis.resize()
        self.arr[self.size-1] = value
        self.size +=1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        return self.arr[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity *=2
        temp_arry = [0] * self.capacity
        for i in range(0, self.size-1):
            temp_arry[i] = self.arr[i]
        self.arr = temp_arry
        return self.arr


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        self.arr = []

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list

    def find(self, value):
        if arr_lis.is_list_orderd() == True:
            for i in range(0, self.size):
                if self.arr[i] == value:
                    return i
        else:
            return arr_lis.binary_search(0, self.size, value)

    def is_list_orderd(self):
        for i in range(0, self.size-1):
            if self.arr[i] <= self.arr[i+1]:
                pass
            else:
                return False
        return True



    def binary_search(self, start, end, target):
        mid = (start + end) // 2
        if self.arr[mid] < target:
            return arr_lis.binary_search(mid + 1, end, target)
        elif self.arr[mid] > target:
            return arr_lis.binary_search(start, mid, target)
        else:
            return mid


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list

    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList(10)

    arr_lis.append(2)
    print(arr_lis.find(2))







