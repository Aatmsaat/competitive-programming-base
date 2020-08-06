//mo's , square root decomposition, 
//stregth decomposition
//#include<bits/stdc++.h>
#include <iostream>
#include <cmath>
using namespace std;
int i,l,r,n,m,b,c[200005],f[1000005];
long long cnt,ans[200005];
struct Q{
	int l,r,k;
	bool operator<(const Q &a)const{
		return ((l-1)/b<(a.l-1)/b) || ((l-1)/b==(a.l-1)/b && r<a.r);
	}
}a[200005];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
	cin >> n >> m;
	for(i=1;i<=n;i++) cin >> c[i];
	for(i=1;i<=m;i++){
        cin >> a[i].l >> a[i].r;
        a[i].k=i;
	}
	b=sqrt(n);
	sort(a+1,a+m+1);
	for(l=i=1; i<=m; i++){
		//write operation at c[l], adjust l and r
		// according to current pattern
		for(;l<a[i].l;cnt-=1ll*c[l++]);
		for(;l>a[i].l;cnt+=1ll*c[--l]);
		for(;r<a[i].r;cnt+=1ll*c[++r]);
		for(;r>a[i].r;cnt-=1ll*c[r--]);
		ans[a[i].k]=cnt;
	}
	for(i=1;i<=m;i++) cout << ans[i] << "\n";
}
