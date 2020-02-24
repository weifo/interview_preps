//时间复杂度 nlogN
//内存 logN||1
//稳定否？ depends

function quickSort(a,left,right){
  let pivot,
      partitionIndex;
  
  if(left<right){
    pivot=right;
    partitionIndex=partition(a,left,right,pivot);
    
    quickSort(a,left,partitionIndex-1);
    quickSort(a,partitionIndex+1,right)
  }
  return a;
}

function partition(arr,left,right,pivotIndex){
  let pivotValue=arr[pivotIndex];
  let partitionIndex=left;
  swap(arr,right,pivotIndex);
  
  for(let i=left;i<right;i++){
    if(arr[i]<pivotValue){
      swap(arr,i,partitionIndex);
      partitionIndex++;
    }
  }
  swap(arr, right, partitionIndex);
  return partitionIndex
}
function swap(arr,i,j){
  [arr[i],arr[j]]=[arr[j],arr[i]]
}
let arr1=quickSort(a,0,a.length-1)
