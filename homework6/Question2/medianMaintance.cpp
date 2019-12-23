#include <iostream> 
#include <queue> 
using namespace std;

#define D(x) cout << "DEBUG: " << #x " = " << x << endl

priority_queue<int> lower;
priority_queue<int, vector<int>, greater<int> > upper;

void addToPqs(int num){
    if(lower.size() == 0 || num < lower.top()){
        lower.push(num);
    } else
        upper.push(num);
}

void rebalance(){
    int lowerSize = lower.size();
    int upperSize = upper.size();
    if(lowerSize - upperSize >= 2){
        upper.push(lower.top());
        lower.pop();
    } else if( upperSize - lowerSize >= 2){
        lower.push(upper.top());
        upper.pop();
    }
}

int getMedian(){
    int lowerSize = lower.size();
    int upperSize = upper.size();
    if(lowerSize >= upperSize){
        return  lower.top();
    } else
        return upper.top();

}

int main(){
    freopen("Median.txt","r", stdin);
    int num;
    unsigned long long sum = 0; 
    while(cin >> num){
        addToPqs(num);
        rebalance();
        sum += getMedian();
    }
    
    cout << sum % 10000 << endl;
    cout << lower.size() << " " << upper.size() << endl;
    return 0;
}
