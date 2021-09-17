#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
using namespace std;

int main(){
    int N;
    cin>>N;
    vector<int> A(N), B(N);
    for (int i=0; i<N; i++)
    {
        cin>>A[i]>>B[i];
        if (A[i]!=-1)
            A[i]--;
        if (B[i]!=-1)
            B[i]--;
    }

    vector<int> I(2*N, -1);
    vector<bool> F(2*N);
    for (int i=0; i<N; i++)
    {
        if (A[i]!=-1)
        {
            if (I[A[i]]!=-1)
            {
                cout<<"No"<<endl;
                return 0;
            }
            I[A[i]] = i;
            F[A[i]] = true;
        }
        if (B[i]!=-1)
        {
            if (I[B[i]]!=-1)
            {
                cout<<"No"<<endl;
                return 0;
            }
            I[B[i]] = i;
            F[B[i]] = false;
        }
        if (A[i]!=-1 && B[i]!=-1 &&
            A[i]>=B[i])
        {
            cout<<"No"<<endl;
            return 0;
        }
    }

    vector<bool> OK(2*N+1);
    OK[0] = true;
    for (int i=0; i<2*N; i++)
        if (OK[i])
        {
            for (int j=1; i+2*j<=2*N; j++)
            {
                bool ok = true;
                for (int k=0; k<j; k++)
                {
                    if (I[i+k]==-1 && I[i+j+k]==-1)
                        ;
                    if (I[i+k]==-1 && I[i+j+k]!=-1)
                    {
                        if (F[i+j+k])
                            ok = false;
                    }
                    if (I[i+k]!=-1 && I[i+j+k]==-1)
                    {
                        if (!F[i+k])
                            ok = false;
                    }
                    if (I[i+k]!=-1 && I[i+j+k]!=-1)
                    {
                        if (I[i+k]!=I[i+j+k])
                            ok = false;
                    }
                }
                if (ok)
                    OK[i+2*j] = true;
            }
        }

    cout<<(OK[2*N] ? "Yes" : "No")<<endl;
}
