class MyHashSet {
public:
    vector<bool>ans;
    MyHashSet() {
        for(int i=0;i<1000001;i+=1){
            ans.push_back(false);
        }
    }
    
    void add(int key) {
        ans[key]=true;
        
    }
    
    void remove(int key) {
        ans[key]=false;
    }
    
    bool contains(int key) {
        return ans[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
