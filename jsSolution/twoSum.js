var twoSum = function(nums,target){
    var ans=[];
    for(var i = 0; i < nums.length; i++){
        for(var j = i + 1; j < nums.length; j++){
            if(nums[i]+nums[j] === target)
            {
                ans.push(i);
                ans.push(j);
                return ans;
            }
        }
    }
    return ans;
};
