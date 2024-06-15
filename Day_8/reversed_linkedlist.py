class Node():
    def __init__(self,node,next):
        self.node = node
        self.next = next


class ll():
    def __init__(self):
        self.head = None


    def insert(self,data):
        node = Node(data,self.head)
        self.head =node

        itr = self.head
        lst = ''
        while itr:
            lst += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(lst)

    def __reversed__(self):
        cur = self.head
        next = cur.next
        pre = 0

        while(cur!=0):
            per = cur
            cur = next




ll= ll()

ll.insert(45)

ll.insert(5)
ll.insert(50)
