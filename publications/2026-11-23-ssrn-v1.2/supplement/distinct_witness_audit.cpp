// Exact finite witness coverage. No probabilistic primality tests.
#include <array>
#include <cstdlib>
#include <iostream>
#include <vector>
int main(int argc,char**argv){
    const int B=argc==2?std::atoi(argv[1]):8000000;
    if(B<6 || B>100000000 || B%2) return 2;
    std::vector<unsigned char> is(B+1,1);
    is[0]=is[1]=0;
    for(int p=2;p<=B/p;++p) if(is[p])
        for(int j=p*p;j<=B;j+=p) is[j]=0;
    std::vector<int> lp(B+1), ps;
    for(int n=2;n<=B;++n){
        if(!lp[n]){lp[n]=n;ps.push_back(n);}
        for(int p:ps){if(p>lp[n]||p>B/n) break;lp[p*n]=p;}
        if((lp[n]==n)!=bool(is[n])) return 3;
    }
    std::array<long long,3> targets{}, witnessed{};
    std::cout<<"limit="<<B<<"\n";
    for(int n=4;n<=B;n+=2){
        const int k=(lp[n/2]==n/2)?2:((lp[n-1]==n-1)?1:0);
        if(is[n/2]!=(k==2)) return 4;
        ++targets[k];
        int a=0,b=0;
        for(int p:ps){if(p>=n-p) break;if(is[n-p]){a=p;break;}}
        for(int p=3;p<n-p;p+=2){if(lp[p]==p && lp[n-p]==n-p){b=p;break;}}
        if(a!=b) return 5;
        if(a) ++witnessed[k];
        else {
            std::cout<<"no_distinct_pair="<<n<<"\n";
            if(k!=2) return 6;
        }
    }
    const char* cat[]={"H","H1","prime_midpoint"};
    for(int i=0;i<3;++i)std::cout<<cat[i]<<" targets="<<targets[i]<<" witnesses="<<witnessed[i]<<"\n";
}
