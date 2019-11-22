const bubbleSort =require('./bubble-sort');
let test=[
    [1,3,4,5,6],
    [2,7,6,8,9],
    [3,0,1,10,8]
];
function compare(a,b){
    return a-b;
}
function JSsort(arr){
    return arr.sort(compare)
}
function execute(){
    for(let arr of test){
        if(bubbleSort(arr).join('')!==JSsort(arr).join('')){
            return false
        }
        console.log(bubbleSort(arr),JSsort(arr))
    }
    return true
}
console.log(execute())
