func reverse(topsort []int){
    
    for x,y:= 0,len(topsort) - 1; x < y ; {
        
        topsort[x],topsort[y] = topsort[y],topsort[x]
        x++
        y--
    }
}
func dfs(node int, visited map[int]int, adj_list map[int][]int, topsort *[]int) bool {
    visited[node] = 1
    
    for _,v := range adj_list[node] {
        
        if visited[v] == 0 {
            if dfs(v,visited,adj_list,topsort) == false {
                return false
            }
        } else if visited[v] == 1 {
            return false
        }
    }
    
    visited[node] = 2
    (*topsort) = append((*topsort),node)
    return true
}
func findOrder(numCourses int, prerequisites [][]int) []int {
    adj_list := make(map[int][]int)
    visited := make(map[int]int)
    topsort := make([]int,0,numCourses)
    
    for _,value := range prerequisites {
        u := value[0]
        v := value[1]
        adj_list[v] = append(adj_list[v],u)
    }
    
    for node := 0; node < numCourses; node++ {
        if visited[node] == 0 {
            if dfs(node,visited,adj_list,&topsort) == false {
                return []int {}
            }
            
        }
    }
    reverse(topsort)
    return topsort
}