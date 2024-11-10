// class Solution {
//     public int maxFrequency(int[] nums, int k) {
        
//         int index=0;
//         Arrays.sort(nums);
//         int max=nums[nums.length-1];
//         // for(int i=1;i<nums.length;i++){
//         //     if(nums[i]>max){
//         //         max=nums;
//         //         index=i;
//         //     }
//         // }
//         for(int i=nums.length-2;i>=0;i--){
//             while(k>0 && nums[i]<max){
//               nums[i]++;
//               k--;
//             } 
//         }
//         // for(int i=0;i<nums.length;i++){
//         //     System.out.print(nums[i]);
//         // }
//         int count=0;
//         for(int i=0;i<nums.length;i++){
//             if(nums[i]==max){
//                 count++;
//             }
//         }
        

//         return count;
//     }
// }



class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, right = 0;
        long res = 0, total = 0;

        while (right < nums.length) {
            total += nums[right];

            while (nums[right] * (right - left + 1L) > total + k) {
                total -= nums[left];
                left += 1;
            }

            res = Math.max(res, right - left + 1L);
            right += 1;
        }

        return (int) res;        
    }
}