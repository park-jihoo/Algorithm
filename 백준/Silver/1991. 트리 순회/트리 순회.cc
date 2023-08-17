#include <iostream>
#include <vector>
#include <map>

using namespace std;

map<char, pair<char, char> > adj;

void preorder(char root){
    if(root == '.') return;
    cout << root;
    preorder(adj[root].first);
    preorder(adj[root].second);
}

void inorder(char root){
    if(root=='.') return;
    inorder(adj[root].first);
    cout << root;
    inorder(adj[root].second);
}

void postorder(char root){
    if(root=='.') return;
    postorder(adj[root].first);
    postorder(adj[root].second);
    cout << root;
}

int main(){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        char node, left, right;
        cin>>node>>left>>right;
        adj[node] = make_pair(left, right);
    }

    preorder('A');
    cout << endl;
    inorder('A');
    cout << endl;
    postorder('A');
    cout << endl;
    return 0;
}