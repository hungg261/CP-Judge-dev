#include <bits/stdc++.h>
#define int long long
using namespace std;

#include "../../RandLib/randlib.h"
using namespace RandLib;

NumberGen NumGen;
void generate(int test){
    int n = test <= 5 ? NumGen.Rand<int>(1, 10) : NumGen.Rand<int>(1, 1e9);
    cout << n << '\n';
}

signed main(int32_t argc, char* argv[]){
    ios_base::sync_with_stdio(0); cin.tie(0);

    int test = stoi(argv[1]);
    generate(test);

    return 0;
}