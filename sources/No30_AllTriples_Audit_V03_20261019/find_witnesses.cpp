// No.30: exhaustive majority-margin witness search for noncentral triples.
// Tested using g++ -O3 -std=c++17 (uses uint64; odd n <= 61).
// Each emitted witness has exactly m+1 ones and falsifies A o B_ab o A.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
inline U shift_read(U x, int a, int n, U mask){return ((x>>a)|(x<<(n-a)))&mask;}
inline bool central(int a,int b,int m,int n){return (a==1 && b==m+1)||(a==m && b==m+1)||(a==m && b==n-1);}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"usage: find_witnesses <output.csv>\n";return 2;}
 ofstream out(argv[1]);
 out<<"n,a,b,witness_decimal,defect_majority_ones,one_runs\n";
 for(int n=25;n<=61;n+=2){
  int m=(n-1)/2;U mask=(1ULL<<n)-1;
  vector<pair<int,int>> triples;vector<int> status;
  for(int a=1;a<n;a++)for(int b=a+1;b<n;b++)if(!central(a,b,m,n)){
    triples.push_back({a,b});status.push_back(0);
  }
  int remaining=(int)triples.size();
  U x=(1ULL<<(m+1))-1;uint64_t checked=0;
  while(x<=mask && remaining){
    // w_i=x_i x_{i+1}. Actual A defect is a cyclic shift of w.
    U w=x&shift_read(x,1,n,mask);U s[64];
    for(int a=1;a<n;a++)s[a]=shift_read(w,a,n,mask);
    for(int j=0;j<(int)triples.size();j++)if(!status[j]){
      auto [a,b]=triples[j]; U z=(w&s[a])|(w&s[b])|(s[a]&s[b]);
      int nz=__builtin_popcountll(z);
      if(nz>=m){
        int runs=__builtin_popcountll(x & ~shift_read(x,1,n,mask));
        out<<n<<","<<a<<","<<b<<","<<x<<","<<nz<<","<<runs<<"\n";
        status[j]=1;remaining--;
      }
    }
    checked++;
    U lo=x&-x;U hi=x+lo;
    if(!hi || hi>mask)break;
    x=(((hi^x)>>2)/lo)|hi;
  }
  cout<<"n="<<n<<" checked="<<checked<<" eliminated="
      <<(triples.size()-remaining)<<"/"<<triples.size()<<"\n";
  if(remaining){cerr<<"INCOMPLETE for n="<<n<<" remaining="<<remaining<<"\n";return 1;}
 }
}
