int reverse(int x) {
    int a[31];
    int i,j,temp,tempNum,reverseNum,reminder;
    
    i=0,temp=x;
    reverseNum = 0;
    while(temp !=0){
        reminder = temp % 10;
        reverseNum = (reverseNum*10) + reminder;
        if (reverseNum /10 !=tempNum){
            return 0;
        }
        tempNum =reverseNum;
         printf("reverseNum %d\n",reverseNum);
        temp = temp/10;
    }
    
    return reverseNum;
}