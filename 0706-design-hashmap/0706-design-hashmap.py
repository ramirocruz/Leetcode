class MyHashMap:

    def __init__(self):
        self.M = 1000
        self.data = [None]*self.M
        

    def put(self, key: int, value: int) -> None:
        hashed_key = self.__hash(key)
        if(self.data[hashed_key] == None):
            self.data[hashed_key] = [(key,value)]
        else:
            for idx in range(len(self.data[hashed_key])):
                if self.data[hashed_key][idx][0] == key:
                    self.data[hashed_key][idx] = (key,value)
                    return
            self.data[hashed_key].append((key,value))
        
        

    def get(self, key: int) -> int:
        hashed_key = self.__hash(key)
        if(self.data[hashed_key] == None):
            return -1
        for item in self.data[hashed_key]:
            if item[0] == key:
                return item[1]
        
        return -1

    def remove(self, key: int) -> None:
        hashed_key = self.__hash(key)
        if(self.data[hashed_key] == None):
            return
        for idx in range(len(self.data[hashed_key])):
            try:
                
                if self.data[hashed_key][idx][0] == key:
                    self.data[hashed_key][idx],self.data[hashed_key][-1] = self.data[hashed_key][-1],self.data[hashed_key][idx]
                    self.data[hashed_key].pop()
            
            except Exception as e:
                print(e)
                    
        
    
    def __hash(self,key: int) -> int:
        return int(key%self.M)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)