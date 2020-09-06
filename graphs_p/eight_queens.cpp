    #include "stdafx.h"
    #include <iostream>
    #include <vector>
    #include <string>
    using namespace std;
    class Solution {
    public:
    	vector<vector<string> > solveNQueens(int n) {
    		column=vector<int>(n,0);
    		principle_diagonals=vector<int>(2*n,0);
    		counter_diagonals=vector<int>(2*n,0);
    		vector<int> C(n,0);  //C[i]的值表示第i行皇后所在的列
    		vector<vector<string>> result;
    		DFS(result,C,0);
    		return result;
    	}
    private:
    	vector<int> column;  //column[i]表示第i行皇后所在的列
    	vector<int> principle_diagonals;  //表示主该主对角线是否已经有皇后
    	vector<int> counter_diagonals;  //表示副对角线是否已经有皇后
    	void DFS(vector<vector<string> >& result,vector<int>&C ,int row)
    	{
    		int n=C.size();
    		if(row==n)    //收敛条件
    		{
    			string tmpStr(n,'.');
    			vector<string>tmpResult(n,tmpStr);
    			for(int i=0;i<n;++i)
    			{
    				tmpResult[i][C[i]]='Q';
    			}
    			result.push_back(tmpResult);
    			return;
    		}
    		for(int i=0;i<n;++i)
    		{
    			bool ok=column[i]==0&&principle_diagonals[row+i]==0 && counter_diagonals[n-row+i]==0;
    			if(ok)  //用于剪枝，只扩展合法的状态
    			{
    				//执行扩展
    				column[i]=principle_diagonals[row+i]=counter_diagonals[n-row+i]=1;
    				C[row]=i;
    				DFS(result,C,row+1);
    				//撤销扩展
    				column[i]=principle_diagonals[row+i]=counter_diagonals[n-row+i]=0;
    				C[row]=0;
    			}
    		}
    	}
    };

    int _tmain(int argc, _TCHAR* argv[])
    {
    	vector<vector<string>> result;
    	Solution sln;
    	result=sln.solveNQueens(4);
    	for (int i=0;i<result.size();++i)
    	{
    		for (int j=0;j<result[0].size();++j)
    		{
    			cout<<result[i][j]<<endl;
    		}
    		cout<<endl;
    		cout<<endl;
    	}
    	return 0;
    }