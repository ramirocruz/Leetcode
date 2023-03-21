func dfs(node int, visited map[int]int, adj_list map[int][]int) bool {
    
    visited[node] = 1
        
    for _,v := range adj_list[node] {
        
        if  visited[v] == 0 {
            res := dfs(v,visited,adj_list)
            if res == false {
            return false
            } 
            
        } else if visited[v] == 1 {
                return false
            }    
        
        
    }
    
    visited[node] = 2
    
    return true    
    
}

func canFinish(numCourses int, prerequisites [][]int) bool {
    adj_list := make(map[int][]int)
    visited := make(map[int]int)
    
    for _, value := range prerequisites {
        u := value[0]
        v := value[1]
        adj_list[v] = append(adj_list[v],u)
    }
    
    for node := range adj_list {
        if visited[node] == 0 {
            res := dfs(node,visited,adj_list)
            if res == false {
                return false
            }
        }
    }
    
    return true
    
}