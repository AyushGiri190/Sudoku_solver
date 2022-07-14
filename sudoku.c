#include<stdio.h>
int grid[9][9];
int possible(int row,int column,int number);
int solve();
int main()
{
    for (int i=0;i<9;i++)
    {
        for (int j=0;j<9;j++)
        {
            scanf("%d",&grid[i][j]);
        }
    }
    solve();

}
int possible(int row,int column, int number)
{
    for (int i=0;i<9;i++)
    {
        if (grid[row][i] == number)
            return 0;
    }
    for (int i=0;i<9;i++)
    {
        if (grid[i][column] == number)
            return 0;
    }
    int x0=(column/3)*3;
    int y0=(row/3)*3;
    for (int i=0;i<3;i++)
    {
        for (int j=0;j<3;j++)
        {
            if (grid[y0+i][x0+j]==number)
                return 0;

        }
    }
    return 1;
}
int solve()
{
    for(int i=0;i<9;i++)
    {
        for(int j=0;j<9;j++)
        {
            if (grid[i][j]==0)
            {
                for (int number=1;number<10;number++)
                {
                    if(possible(i,j,number))
                    {
                        grid[i][j]=number;
                        solve();
                        grid[i][j]=0;
                    }


                }
                return 1;
            }
        }
    }
    printf("\n");
    for (int i=0;i<9;i++)
    {
        for (int j=0;j<9;j++)
        {
            printf("%d ",grid[i][j]);
        }
        printf("\n");
    }
}
