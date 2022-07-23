#include <iostream>
#include <vector>

int main(){
    std::cin.tie(NULL);
    std::cin.sync_with_stdio(false);
    int t, n, m;
    std::cin >> t;
    while(t--){
        std::cin >> n >> m;
        std::vector<int> stdq(m,{0});
        std::vector<bool> coll(m,{0});
        std::vector<int> rowl(m,{0});
        int rowsum=0, colgood=0;
        for (int i=0;i<n*m;i++){
            int j = i % m;
            char c;
            std::cin >> c;
            int a = c - '0';
            rowsum -= stdq[j];
            stdq[j] = a;
            rowsum += a;
            if (rowsum != 0){
                rowl[j]+=1;
            }
            if (a==1 && coll[j]==0){
                colgood += 1;
                coll[j] = 1;
            }
            std::cout << rowl[j]+colgood;
            if (i<n*m-1){
                std::cout << " ";
            }
            else{
                std::cout << "\n";
            }
        }
    }
    return 0;
}