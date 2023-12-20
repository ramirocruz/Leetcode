class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_min = int(1e9 + 7)
        second_min = int(1e9 + 6)
        
        for price in prices:
            if price < first_min:
                second_min = first_min
                first_min = price
            elif price < second_min:
                second_min = price
        
        print(first_min,second_min)
        
        choco_sum = first_min + second_min
        
        return money - choco_sum if money >= choco_sum else money