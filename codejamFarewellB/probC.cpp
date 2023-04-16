#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

// s is spacious(k) if max(|e1-e2|) >= k

int main(){
    cin.tie(NULL);
    cin.sync_with_stdio(false);
    int t;
    cin >> t;
    for (int cases = 0; cases < t; cases++){
        int n,k;
        cin >> n >> k;
        vector<long> a(n);
        map<long,long> tree_left;
        map<long,long> tree_right;
        for (auto& e: a){
            cin >> e;
            tree_left.emplace(-e, 0);
            tree_right.emplace(e, 0);
        }
        for (auto it1 = tree_left.rbegin(); it1 != tree_left.rend(); it1++){
            auto it = tree_left.lower_bound(it1->first + k);
            int fill;
            if (it == tree_left.end()){
                fill = 0;
            }
            else{
                fill = it->second;
            }
            it1->second = fill + 1;
        }

        for (auto it1 = tree_right.rbegin(); it1 != tree_right.rend(); it1++){
            auto it = tree_right.lower_bound(it1->first + k);
            int fill;
            if (it == tree_right.end()){
                fill = 0;
            }
            else{
                fill = it->second;
            }
            it1->second = fill + 1;
        }
        cout << "Case #" << cases + 1 << ":";
        for (auto& e: a){
            cout << " " << tree_left[-e] + tree_right[e] - 1;
        }
        cout <<"\n";
    }

}