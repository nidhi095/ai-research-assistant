from src.linked_list import LinkedList

def test_append_to_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.to_list() == [1, 2]
