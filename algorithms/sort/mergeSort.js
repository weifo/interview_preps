//时间复杂度 nlogn
//占用内存 n
//稳定否？ 稳定

function mergeSort(a){
  let len=a.length;
  
  if(len<2){
    return a
  }
  let mid=Math.floor(len/2),
      left=a.slice(0,mid),
      right=a.slice(mid);
  console.log(left,right)
  return merge(mergeSort(left),mergeSort(right))
}

function merge(a,b){
  let la=a.length,
      lb=b.length,
      result=[];
  let ia=0,
      ib=0;
  while(ia<la||ib<lb){
    if(ia==la){
      return result.concat(b.slice(ib));
    }else if(ib==lb){
      return result.concat(a.slice(ia));
    }else if(a[ia]<b[ib]){
      result.push(a[ia]);
      ia++;
    }else{
      result.push(b[ib]);
      ib++;
    }
  }
  return result;
}
let arr=[33,15,6,9,43,18]
let res=mergeSort(arr);
console.log(res)
