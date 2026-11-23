#include <vector>
using namespace std;

class ProductOfNumbers {
public:
    // store prefix products; start with 1 so prefix[i] = product of first i numbers
    vector<long long> prefix;

    ProductOfNumbers() {
        prefix.clear();
        prefix.push_back(1); 
    }

    void add(int num) {
        if (num == 0) {
            
            prefix = {1};
        } else {
            prefix.push_back(prefix.back() * (long long)num);
        }
    }

    int getProduct(int k) {
        int n = prefix.size();          
        if (k >= n) return 0;          
        long long result = prefix.back() / prefix[n - 1 - k];
        return (int)result;
    }
};
