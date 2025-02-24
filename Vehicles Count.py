def vehiclescount(v,w):
  if w<2 or w%2!=0 or w<=v:
    print("INVALID OUTPUT")
  FW=(w-(2*v))/2
  TW= v-FW

  if FW<0 or TW<0:
    print("INVALID OUTPUT")
  else:
      print("Two Wheelers", TW)
      print("Four Wheelers", FW)

v=int(input())
w=int(input())

vehiclescount(v,w)

#200
#540
#Two Wheelers 130.0
#Four Wheelers 70.0
