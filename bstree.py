class BSTree:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self._parent = parent
        self._left = left
        self._right = right
        self.data = data

    def __iter__(self):

        items = []

        def _iter_helper(node):
            if node is None:
                return []
            else:
                items.append(node)
                _iter_helper(node.left)
                _iter_helper(node.right)

        _iter_helper(self)
        for item in items:
            yield item

    def set_left(self, value):
        self._left = BSTree(value)

    def get_left(self):
        return self._left

    left = property(get_left, set_left)

    def set_right(self, value):
        self._right = BSTree(value)

    def get_right(self):
        return self._right

    right = property(get_right, set_right)

    def set_parent(self, value):
        self._parent = value

    def get_parent(self):
        return self._parent

    parent = property(get_parent, set_parent)

    def get_leafs(self):
        elements = list(self.__iter__())
        leafs = list(
            filter(lambda x: x.left is None and x.right is None, elements))
        return leafs