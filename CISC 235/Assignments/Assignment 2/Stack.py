class Stack:
    
    def __init__(self):
        self.arrList = list()

    def isEmpty():
        if len(arrList) == 0:
            return True
        else:
            return False

    def push(item):
        arrList.append(item)
        
    def pop():
        item = arrList[len(arrList) - 1]
        arrList.remove(item)
        return item

    def top():
        item = arrList[len(arrList) - 1]
        return item

    def size():
        return len(arrList)
