int hammingDistance(int x, int y) {
    
    int xorRes,count=0;
    
    xorRes = x ^y;
    
    for(;xorRes>0;xorRes=xorRes>>1){
        if(1 & xorRes) {
            ++count;
        }
    }
    
    return count;
    
}