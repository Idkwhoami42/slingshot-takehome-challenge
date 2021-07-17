#include <bits/stdc++.h>
using namespace std;

struct Node{
    unordered_map<char, Node*> children;
    bool leaf;
};

struct Trie{
    Node* root = new Node();
    
    void insert(string s){
        Node* node = root;
        for(int i = 0;i<s.size();i++){
            if(node->children[s[i]] == nullptr){
                node->children[s[i]] = new Node();
            }
            node = node->children[s[i]];            
        }
        node->leaf=1;
    }

    bool search(string s){
        Node* node = root;
        for(int i = 0;i<s.size();i++){
            if(node->children[s[i]] == nullptr) return false;
            node = node->children[s[i]];
        }
        return node->leaf;
    }

    void erase(string s){
        if (!search(s)){
            cout << "String Not Found\n";
            return;
        }   
        Node* node = root;
        vector<Node*> path = {node};
        for(auto i:s){
            node = node->children[i];
            path.push_back(node);
        }

        Node* last = path.back();
        
        bool has_no_child = true;
        for(int i = 0;i<26;i++){
            char y = char(i + 97);
            if(last->children[y] != nullptr) has_no_child = false;
        }

        if(has_no_child){
            // cout << "searched " + s << '\n';
            last->leaf = false;
            for(int i = path.size() - 2; i>=0;i--){
                Node* node = path[i];
                int count = 0;
                for(int j = 0;j<26;j++){
                    char y = char(j + 97);
                    if(node->children[y] != nullptr) count += 1;
                }
                if(count == 1 && node->children[s[i]]->leaf == false){
                    node->children[s[i]] = nullptr;
                }
                else break;
            }
        }
        else last->leaf = false;

    }
    
    void get_keywords(string curr, vector<string> &keywords, Node* node = nullptr){
        if(node == nullptr)node = root;
        if(node->leaf){
            keywords.push_back(curr);
        }
        for(int x = 0;x<26;x++){
            char y = char(x + 97);
            if(node->children[y] != nullptr){
                get_keywords(curr + y, keywords, node->children[y]);
            }
        }
    }
};

vector<string> split(string s){
    vector<string> v;
    stringstream ss(s);
    string x;
    while (ss >> x){
        v.push_back(x);
    }
    return v;
}

int main(){
    Trie trie;
    while (1) {
        string command;
        getline(cin,command);
        
        vector<string> v = split(command), commands = {"help", "insert", "delete", "search", "prefix"};

        if(v[1] == "help"){
            cout << "List of commands\n\n";
            cout << "help               : displays this message\ninsert <keyword>   : inserts keyword to the trie\ndelete <keyword>   : deletes the keyword if found in the trie\nsearch <keyword>   : returns whether keyword is in the trie or not\nprefix <keyword>   : print all the words with keyword as prefix\ndisplay            : prints all the keywords in the trie\n";
        }    
        else if(v[1] == "insert"){
            trie.insert(v[2]);
            cout << "successfully inserted " << v[2] << '\n';
        }
        else if(v[1] == "delete"){
            if(!trie.search(v[2])) cout << v[2] << " is not found";
            else{
                trie.erase(v[2]);
                cout << "successfully deleted " << v[2] << '\n';
            }
        }
        else if(v[1] == "search"){
            cout << (trie.search(v[2]) ? "Found" : "Not Found") << '\n';
        }
        else if(v[1] == "prefix"){
            
        }
        else if(v[1] == "display"){
            cout << "List of keywords in the trie:\n";
            vector<string> keywords;
            trie.get_keywords("", keywords);
            sort(keywords.begin(), keywords.end());
            for(auto keyword:keywords)cout << keyword << '\n';
        }
    }
}
