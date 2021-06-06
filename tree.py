class TreeNode:
    def __init__(self,data):
        self.data = data
        self.childern = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.childern.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def print_tree(self):
        space = ' ' * self.get_level()*3
        prefix = space + "|__" if self.parent else""
        print(prefix + self.data)
        if self.childern >0:
            for child in self.childern:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Dell"))

    mobile = TreeNode("Mobiles")
    mobile.add_child(TreeNode("Iphone"))
    mobile.add_child(TreeNode("MI"))
    mobile.add_child(TreeNode("RealMe"))

    tv = TreeNode("TV")
    tv.add_child("LG")
    tv.add_child("MI(LED)")
    tv.add_child("SAMSUNG")

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root


if __name__ == '__main__':

    root=build_product_tree()
    root.print_tree()
    
        