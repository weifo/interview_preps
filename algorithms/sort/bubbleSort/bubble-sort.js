function sort(arr){
    let l=arr.length;
    for(let i=0;i<l-1;i++){
        for(let j=0;j<l-i-1;j++){
            if(arr[j]>arr[j+1]){
                // arr[i+1],arr[i]=arr[i],arr[i+1]
                let tmp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=tmp;
            }
        }
    }
    return arr
}

module.exports=sort;
