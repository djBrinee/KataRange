# Coding Kata Range


# Class for Range API

class RangeClass:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def Contains(self, value):
        var = range(self.first, self.last)
        for i in var:
            if(i == value):
                return True
            else:
                return False