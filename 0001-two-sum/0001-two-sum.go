func twoSum(nums []int, target int) []int {
    mp := make(map[int]int)
    for index, value := range nums{
        rem_value := target - value
        _, isPresent := mp[rem_value]
        if isPresent{
            return []int {index,mp[rem_value]}
        }
        mp[value] = index
    }
    return []int {}
}