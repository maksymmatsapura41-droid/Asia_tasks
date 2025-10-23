class Tree:
   def __init__(self, height):
       self.__height = height

   @property
   def height(self):
       print("getter")
       return self.__height

   @height.setter
   def height(self, new_height):
       if not isinstance(new_height, int):
           raise TypeError("Tree height must be an integer")
       if 0 < new_height <= 40:
           self.__height = new_height
       else:
           raise ValueError("Invalid height for a pine tree")


first_tree = Tree(100)
first_tree.height = 50
print(first_tree.height)