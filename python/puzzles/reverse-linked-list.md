# Reverse Lionked List

```py
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# a -> b -> c -> d -> None
# d -> c -> b -> a -> None
def reverse(head):
    new_head = None
    curr = head # a
    previous = None

    while True:
        # b | c
        tmp_curr = curr.next

        # a -> None | b -> a
        curr.next = previous

        previous = curr

        if not tmp_curr:
            break

        # b | c
        curr = tmp_curr

    return curr

l = ListNode(5)
```