class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n = len(boxes)
        ports = [0]*(n+1)
        weight = [0]*(n+1)
        for i,(p,w) in enumerate(boxes,1):
            ports[i]=p
            weight[i]=w
        prefW=[0]*(n+1)
        prefC=[0]*(n+1)
        for i in range(1,n+1):
            prefW[i]=prefW[i-1]+weight[i]
            prefC[i]=prefC[i-1]+(1 if i>1 and ports[i]!=ports[i-1] else 0)
        INF=10**9
        dp=[INF]*(n+1)
        dp[0]=0
        from collections import deque
        dq=deque()
        # candidate j=0, value = dp[0] - prefC[1] (prefC[1]=0)
        dq.append((0,0))
        left=0
        for i in range(1,n+1):
            while i-left>maxBoxes or prefW[i]-prefW[left]>maxWeight:
                left+=1
            while dq and dq[0][0]<left:
                dq.popleft()
            best=dq[0][1]
            dp[i]=prefC[i]+2+best
            if i<n:
                val=dp[i]-prefC[i+1]
                while dq and dq[-1][1]>=val:
                    dq.pop()
                dq.append((i,val))
        return dp[n]