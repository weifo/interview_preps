public class BubbleSort{
    public static int [] sort(int [] arr){
        if(arr==null || arr.length==0){
            return null;
        }
        for(int i=0;i<arr.length-1;i++){
            for (int j=0;j<arr.length-1-i;j++){
                if(arr[j]>arr[j+1]){
                    swap(arr,j,j+1);
                }
            }
        }
        return arr;
        
    }
    public static void swap(int [] arr,int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    public static void main(String args[]){
        int [] test={10,3,8,2,11,4,8};
        int [] res=sort(test);
        for(int i=0;i<res.length;i++){
            System.out.println(res[i]);
        }
    }
}

// BubbleSort b1=new BubbleSort();
// b1.main()