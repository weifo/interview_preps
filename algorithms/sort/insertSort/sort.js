//时间复杂度 n^2
//内存 1
//稳定否？ 稳定
function sort(arr){
    let l=arr.length;
    for(let i=1;i<l;i++){
        let j=i,
        target=arr[i];
        
        while(j>0&&target<arr[j-1]){
            arr[j]=arr[j-1]
            j--;
        }
    }
    console.log(arr.join(' '))
    return arr
}
let test=[
    [1,4,12,3,8,6,5],
    [8,2,6,1,12,3,7],
    [9,10,3,5,2,6,8]
]
test.forEach(arr=>sort(arr));

