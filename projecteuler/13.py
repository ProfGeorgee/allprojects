
def binomialCoeffUtil(n, k, dp):
     
    
    if dp[n][k] != -1: 
        return dp[n][k] 
 
    
    if k == 0:
        dp[n][k] = 1
        return dp[n][k] 
     
 
    if k == n: 
        dp[n][k] = 1
        return dp[n][k] 
     
   
    dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
                binomialCoeffUtil(n - 1, k, dp))
                  
    return dp[n][k] 
 
def binomialCoeff(n, k):
     
    
    dp = [ [ -1 for y in range(k + 1) ] 
                for x in range(n + 1) ] 
 
    return binomialCoeffUtil(n, k, dp)  

n = 40
k = 20
 
print("Value of C(" + str(n) +
               ", " + str(k) + ") is",
               binomialCoeff(n, k)) 
 
