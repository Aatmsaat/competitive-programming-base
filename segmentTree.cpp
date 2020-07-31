 #include <iostream>
 #include <vector>
 
 using namespace std;
 
 typedef long long ll;
 
 struct SegmentTree{
	 ll n;
	 vector <ll>a;
	 void build(){
		 for(ll i=n-1; i>0; --i)a[i]=a[i<<1]+a[i<<1|1];
	 }
	 
	 void update(ll pos, ll val){
		 for(a[pos+=n]=val; pos>1; pos>>=1)a[pos>>1]=a[pos]+a[pos^1];
	 }
	 
	 ll query(ll l, ll r){
		 ll res=0;
		 for(l+=n, r+=n; l<r; l>>=1, r>>=1){
			 if(l&1)res+=a[l++];
			 if(r&1)res+=a[--r];
		 }
		 return res;
	 }
	 
	 SegmentTree(vector<ll>& arr){
		 n=arr.size();
		 a = vector<ll>(n<<1);
		 for(ll i=0; i<n; ++i)a[i+n]=arr[i];
		 build();
	 }
 };
 
 int main(){
	 ll q, n;
	 vector <ll>arr;
	 do{
	 cin>>n;
	 arr.push_back(n);
	 }while(n);
	 cout<<"Enter no. of queries\n";
	 cin>>q;
	 SegmentTree s = SegmentTree(arr);
	 while(q--){
		 ll u,v, w;
		 cin>>u>>v>>w;
		 if(u==1)s.update(v+1,w);
		 else
			 cout<<s.query(v-1,w)<<"\n";
	 }
	 return 0;
 }
