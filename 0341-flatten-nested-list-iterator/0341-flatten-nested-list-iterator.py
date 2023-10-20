# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

    
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat_list = []
        def flatten_list(nested_list):
            if nested_list == None:
                return
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self.flat_list.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList())
        
        flatten_list(nestedList)
        self.pos = -1
    
    def next(self) -> int:
        self.pos += 1
        return self.flat_list[self.pos]
    
    def hasNext(self) -> bool:
        return self.pos + 1 < len(self.flat_list)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())