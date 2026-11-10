/* Stage 59 finite, exact integer-scaled local criterion.
 * Build: cc -O3 -std=c11 local_cert_native.c -o local_cert
 * Run: ./local_cert 1000000
 * Scope: finite test ONLY, not a universal Goldbach proof.
 * Native arithmetic uses signed long long and requires max <= 1000000.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static int wheel(int n) {
  int ps[]={3,5,7},a=1;
  for(int j=0;j<3;j++){int p=ps[j];a*=n%p?p-2:p-1;}
  return a;
}
static long long gcd_ll(long long a,long long b){
  while(b){long long t=a%b;a=b;b=t;}return a;
}
int main(int argc,char**argv) {
  int max=argc>1?atoi(argv[1]):1000000;
  if(max<10 || max>1000000) {
    fprintf(stderr,"limit must be 10..1000000\n"); return 2;
  }
  unsigned char *prime=calloc((size_t)max+1,1);
  int *r=calloc((size_t)max+1,sizeof(int));
  int *ps=malloc(((size_t)max+1)*sizeof(int));
  if(!prime||!r||!ps){fprintf(stderr,"allocation failed\n"); return 3;}
  for(int i=2;i<=max;i++)prime[i]=1;
  for(int p=2;(long long)p*p<=max;p++)
    if(prime[p])for(int q=p*p;q<=max;q+=p)prime[q]=0;
  int pc=0;
  for(int p=3;p<=max;p+=2)if(prime[p])ps[pc++]=p;
  long long configurations=0;
  for(int i=0;i<pc;i++){
    int p=ps[i];
    for(int j=i+1;j<pc;j++){
      int n=p+ps[j];
      if(n>max)break;
      r[n]++; configurations++;
    }
  }
  int tests=0,fail=0,Htests=0,Hfail=0,first=0;
  for(int n=8;n+2<=max;n+=2) {
    int loc[3]={n-2,n,n+2}; long long l=1;
    for(int i=0;i<3;i++){
      int a=wheel(loc[i]);
      l=l/gcd_ll(l,a)*a;
    }
    long long v[3];
    for(int i=0;i<3;i++)v[i]=(long long)r[loc[i]]*(l/wheel(loc[i]));
    /* Equivalent to mean^2 > (2/9)*cyclic energy.
       Exact, avoiding division or floating-point rounding. */
    long long lhs=2*(v[0]*v[1]+v[1]*v[2]+v[2]*v[0]);
    long long rhs=v[0]*v[0]+v[1]*v[1]+v[2]*v[2];
    int ok=(lhs>rhs);
    int H=n-1>1 && n/2>1 && !prime[n-1] && !prime[n/2];
    tests++;
    if(H)Htests++;
    if(!ok){
      fail++;
      if(H)Hfail++;
      if(!first)first=n;
      if(fail<=10) printf("failed center N=%d, H=%d\n",n,H);
    }
  }
  printf("limit=%d unordered_distinct_pair_configurations=%lld\n",max,configurations);
  printf("centers_tested=%d total_failures=%d first_failure=%d\n",tests,fail,first);
  printf("residual_centers=%d residual_failures=%d\n",Htests,Hfail);
  free(prime);free(r);free(ps);
  return 0;
}
