
byte a= 0;

/* 5 procesow to zbyt duzo??
*/
active [3] proctype P() {
  byte tmp, i;
  i=0;
  do
  :: i>=3 -> 
    break;
  :: else ->
    tmp=a; tmp++; a=tmp; 
      /* symulacja incr przy pomocy akumulatora
      */
    i++;
  od
}

