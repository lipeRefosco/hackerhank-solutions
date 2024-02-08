# Cycle detection
# Create a hashMap / Dict
def has_cycle(head):
    current = head
    bucket = {}
    
    while current is not None:
        if current.__hash__() in bucket:
            return 1
        else:
            bucket[current.__hash__()] = current
            current = current.next
    return 0