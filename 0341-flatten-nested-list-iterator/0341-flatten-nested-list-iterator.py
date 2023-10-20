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
def dfs(root: NestedInteger,res):
    if root == None:
        return
    
    if root.isInteger():
        res.append(root.getInteger())
        return
    
    for elem in root.getList():
        dfs(elem,res)
    
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat_list = []
        for n_int in nestedList:
            dfs(n_int,self.flat_list)
        
        self.length = len(self.flat_list)
        self.pos = 0
    
    def next(self) -> int:
        result = self.flat_list[self.pos]
        self.pos += 1
        return result
    
    def hasNext(self) -> bool:
        
        return self.pos < self.length
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())