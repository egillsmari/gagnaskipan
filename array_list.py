class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self, capacity = 4 ,size=0):
        self.size = 0
        self.capacity = capacity
        self.arr = [0]*self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(0, self.size):
            if i == self.size-1:
                return_string += str(self.arr[i])
                return return_string
            return_string += str(self.arr[i])+ ", "
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        '''Moves each element in the list to their index + 1 to make space for a element in the front'''
        self.resize()
        for i in range(self.size, 0, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[0] = value
        self.size+=1

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        '''Creates a temp list with the same capacity. Copies the elements in self.arr to the temp list until we reach
            the index where we want to append.'''
        if index > self.size or index < 0:
            raise IndexOutOfBounds()
        self.resize()
        temp_array = [0] * self.capacity
        for i in range(0, self.size+1):
            temp_array[i] = self.arr[i]
            if i == index:
                temp_array[i] = value
                self.size +=1
            elif i > index:
                temp_array[i] = self.arr[i-1]
        self.arr = temp_array


    #Time complexity: O(1) - constant time
    def append(self, value):
        '''Adds a element to the end of the list. If the list is empty we add a zero placeholder because we cant assigne a value
            to and index if the list is completely empty'''
        if self.arr == []:
            self.arr = [0]
        self.resize()
        self.arr[self.size] = value
        self.size +=1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index > self.size-1 or index < 0:
            raise IndexOutOfBounds()
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.arr[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        '''Increases capacity by 2 and makes sure we dont loose any elements'''
        if self.size == self.capacity:
            self.capacity *=2
            temp_array = [0] * self.capacity
            for i in range(0, self.size):
                temp_array[i] = self.arr[i]
            self.arr = temp_array

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        '''Makes a temp list and moves elements over to self.arr but when it comes to the removing index
            we skip it and continue'''
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
        temp_array = [0] * self.capacity
        for i in range(0, self.size):
            if i == self.size-1:
                self.arr = temp_array
                self.size -=1
                break
            if i >= index:
                temp_array[i] = self.arr[i+1]
            else:
                temp_array[i] = self.arr[i]


    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        '''Finds the position where the value fits in the ordered list by iterating checking the values next i. When the
            correct location is found we re-use methods to put the value in its place. We used break because there is no
            point in continuing looping afer placing the value. '''
        if self.size == 0:
            self.append(value)
        if self.is_list_orderd() == False:
            raise NotOrdered()
        else:
            for i in range(0, self.size):
                if self.size-1 == i and value > self.arr[i]:
                    self.append(value)
                    break
                elif i == 0 and value < self.arr[i]:
                    self.prepend(value)
                    break
                if self.arr[i] <= value and value <= self.arr[i+1]:
                    self.insert(value, i+1)
                    break


    #Time complexity: O(n) - linear time in size of list
    def not_orderd_find(self, value):
        for i in range(0, self.size):
            if self.arr[i] == value:
                return i
            elif self.size-1 == i:
                raise NotFound()


    def find(self, value):
        '''Finds out if the list is ordered or not and the uses the corresponding method'''
        if self.is_list_orderd() == False:
            return self.not_orderd_find(value)
        else:
            return self.binary_search(0, self.size, value)

    def is_list_orderd(self):
        '''Checks if element above it is bigger or equal to decide if the list is ordered or not'''
        for i in range(0, self.size-1):
            if self.arr[i] <= self.arr[i+1]:
                pass
            else:
                return False
        return True

    # Time complexity: O(log n) - logarithmic time in size of list
    def binary_search(self, start, end, target):
        '''Finds the middle of the list recursively and finds of middle of the list is bigger or smaller then
            the target. '''
        mid = (start + end) // 2
        if self.arr[mid] < target:
            return self.binary_search(mid + 1, end, target)
        elif self.arr[mid] > target:
            return self.binary_search(start, mid, target)
        else:
            return mid


    #Time complexity: O(n) - linear time in size of list


    def remove_value(self, value):
        '''Finds the index of the value and re-uses the remove_at method'''
        for i in range(0, self.size):
            if value == self.arr[i]:
                self.remove_at(i)
                break
            elif self.size-1 == i:
                raise NotFound()



if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    #14, 21, 17, 80, 99, 13, 55, 91
    arr_lis = ArrayList()
    print(str(arr_lis))
    arr_lis.insert_ordered(15)
    arr_lis.insert_ordered(25)
    arr_lis.insert_ordered(13)
    arr_lis.insert_ordered(11)
    arr_lis.insert_ordered(13)
    print(arr_lis)







