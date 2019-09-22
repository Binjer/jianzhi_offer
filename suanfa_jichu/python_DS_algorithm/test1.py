class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(4)

class Bird(object):
    def __new__(cls):
        print("执行__new__方法")
        return super().__new__(cls)

    def __init__(self):
        print("执行__init__方法")

    def say(self):
        print("hhhhh")


# Bird()
