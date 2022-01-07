class Binary:
    def __init__(self, array):
        self.arr = array

    def binary(self, low, high, x):
        if high >= low:
            mid = (high+low)//2

            if self.arr[mid] == x:
                return True
            elif self.arr[mid] > x:
                return self.binary(low, mid-1, x)
            else:
                return self.binary(mid+1, high, x)
        else:
            return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Binary(arr)

validity = obj.binary(0, 9, 11)

print(validity)
