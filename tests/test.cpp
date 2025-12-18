#include <bits/stdc++.h>
using namespace std;

#include "../RandLib/randlib.h"
using namespace RandLib;

signed main(){
    ios_base::sync_with_stdio(0); cin.tie(0);

    NumberGen NumGen;
    cout << NumGen.Rand(-100, 100) << '\n';

    return 0;
}