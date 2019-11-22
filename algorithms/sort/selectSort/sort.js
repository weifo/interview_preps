function select_sort(arr){
    let minIndex=0;
    let l=arr.length;
    for(let i=0;i<l;i++){
        minIndex=i;
        for(let j=i+1;j<l;j++){
            if(arr[j]<arr[minIndex]){
                minIndex=j;
            }
        }
        if(minIndex!==i){
            [arr[i],arr[minIndex]]=[arr[minIndex],arr[i]];
        }
        
    }
    console.log(arr)
    return arr
}

let test=[
    [1,3,12,4,5,2,1],
    [2,3,4,5,4,10,3],
    [3,2,3,4,1,9,5,2]
]
for(let arr of test){
    select_sort(arr)
}