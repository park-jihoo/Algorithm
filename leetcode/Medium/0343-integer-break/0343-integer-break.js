/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
    
        if (n<=3)
            return n-1; 
        var ans = 1;
        while (n > 4){
            ans *= 3;
            n -= 3;
        }
        return ans * n;
};