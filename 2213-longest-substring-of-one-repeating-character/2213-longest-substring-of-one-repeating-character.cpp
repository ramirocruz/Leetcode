struct SegTree{
    
    int n;
    vector<int>max_len,prefix_len,suffix_len;
    vector<char>left_char,right_char;
    
    SegTree(string &s){
        n = s.size();
        max_len.resize(4*n);
        prefix_len.resize(4*n);
        suffix_len.resize(4*n);
        left_char.resize(4*n);
        right_char.resize(4*n);
        
        build_tree(s,0,n-1,0);
    }
    void build_tree(string &s,int start,int end,int node)
    {
        if(start > end)
            return;
        if(start == end)
        {
            max_len[node] = prefix_len[node] = suffix_len[node] = 1;
            left_char[node] = right_char[node] = s[start];
            return;
        }
        int left_child = node*2 + 1;
        int right_child = node*2 + 2;
        int mid = start + (end - start)/2;
        build_tree(s,start,mid,left_child);
        build_tree(s,mid+1,end,right_child);
        merge_children(start,end,node);
    }
    
    void merge_children(int start,int end, int node)
    {
        int left_child = node*2 + 1;
        int right_child = node*2 + 2;
        int mid = start + (end - start)/2;
        
        prefix_len[node] = prefix_len[left_child];
        suffix_len[node] = suffix_len[right_child];
        left_char[node] = left_char[left_child];
        right_char[node] = right_char[right_child];
        
        int temp_max = 0;
        
        if(right_char[left_child] == left_char[right_child])
        {
           
            temp_max = max(temp_max,suffix_len[left_child] + prefix_len[right_child]);
            if(suffix_len[left_child] == mid - start + 1)
            {
                prefix_len[node] += prefix_len[right_child];
            }
            
            if(suffix_len[right_child] == end - mid)
            {
                suffix_len[node] += suffix_len[left_child];
            }
            
        }
        
        temp_max = max({temp_max,max_len[left_child],max_len[right_child]});
        max_len[node] = max({temp_max,prefix_len[node],suffix_len[node]});
        
    }
    int update(int pos,char val)
    {
        return update_helper(0,0,n-1,pos,val);
    }
    
    private:
    int update_helper(int node,int start,int end,int pos,char val)
    {
        if(start > end)
            return 0;
        if(start == end)
        {
            max_len[node] = prefix_len[node] = suffix_len[node] = 1;
            left_char[node] = right_char[node] = val;
            return max_len[node];
        }
        
        int mid = start + (end - start)/2;
        int left_child = node*2 + 1;
        int right_child = node*2 + 2;
        if(pos >= start && pos <= mid)
        {
            update_helper(left_child,start,mid,pos,val);
        }
        else
        {
            update_helper(right_child,mid+1,end,pos,val);
        }
        merge_children(start,end,node);
        
        return max_len[node];
    }
};
class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        
        SegTree segtree(s);
        int q = queryIndices.size();
        vector<int>ans;
        ans.reserve(q);
        
        for(int i = 0;i < q; i++)
        {
            ans.push_back(segtree.update(queryIndices[i],queryCharacters[i]));
        }
        
        return ans;
    }
};