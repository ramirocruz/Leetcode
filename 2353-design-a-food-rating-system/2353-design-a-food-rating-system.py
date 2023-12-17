class Food:
    def __init__(self,food: str, rating: int):
        self.food = food
        self.rating = rating
    
    def __lt__(self,other):
        if self.rating == other.rating:
            return self.food < other.food
        return self.rating > other.rating

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_food_map = {}
        self.food_cuisines_map = {}
        self.ratings_map = {}
        for i in range(len(foods)):
            self.ratings_map[foods[i]] = ratings[i]
            self.food_cuisines_map[foods[i]] = cuisines[i]
            if cuisines[i] not in self.cuisines_food_map:
                self.cuisines_food_map[cuisines[i]] = []
            
            heapq.heappush(self.cuisines_food_map[cuisines[i]],Food(foods[i],ratings[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings_map[food] = newRating
        cuisine = self.food_cuisines_map[food]
        heapq.heappush(self.cuisines_food_map[cuisine],Food(food,newRating))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisines_food_map[cuisine][0]
        while self.ratings_map[highest_rated.food] != highest_rated.rating:
            heapq.heappop(self.cuisines_food_map[cuisine])
            highest_rated = self.cuisines_food_map[cuisine][0]
        
        return highest_rated.food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)