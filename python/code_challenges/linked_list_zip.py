from data_structures.linked_list import LinkedList

def zip_lists(list1, list2):
        current1 = list1.head
        current2 = list2.head
        if not current1 and not current2:
            return None
        results_LL = LinkedList()
        while current1 and current2:
            results_LL.append(current1.value)
            results_LL.append(current2.value)
            current1 = current1.next
            current2 = current2.next
        while current1:
            results_LL.append(current1.value)
            current1 = current1.next
        while current2:
            results_LL.append(current2.value)
            current2 = current2.next
        return results_LL
