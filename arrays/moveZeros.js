// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]


var moveZeroes = function(nums) {
    // var arr_len = nums.length;
    var  i =0;
    var total_zero = 0;
    while(i<nums.length){
        if(nums[i]==0){
            total_zero++;
            nums.splice(i,1);
        }
        else{
            i++;
        }
    }
    while(total_zero>0){
        nums.push(0);
        total_zero--;
    }
};