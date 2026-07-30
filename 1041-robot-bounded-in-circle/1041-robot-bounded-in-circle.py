class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        d='N'
        directions={'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
        nextDirection={'N':('E','W'),'S':('W','E'),'E':('S','N'),'W':('N','S')}
        k=0
        while(k<4):
            k+=1    
            for i in instructions:
                if(i=='G'):
                    x+=directions[d][0]
                    y+=directions[d][1]
                elif(i=='R'):
                    d=nextDirection[d][0]
                else:
                    d=nextDirection[d][1]
            if(x==0 and y==0):
                return True
        return False




        