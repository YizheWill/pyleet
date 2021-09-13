# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    if linkedList is None:
        return
    head = linkedList
    val = linkedList.value
    while linkedList.next:
        if linkedList.next.value == val:
            linkedList.next = linkedList.next.next
            continue
        else:
            val = linkedList.next.value
            linkedList = linkedList.next
    return head
