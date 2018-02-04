#[['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']]
myFirstList = [ list('ACADGILD')]
print (myFirstList)


#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
mySecondList = [ x * i for x in ['x','y','z'] for i in range(1,5)]
print (mySecondList)


#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
myThirdList = [ x * y for x in range(1,5) for y in ['x','y','z']]
print (myThirdList)


#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
myFourthList = [ [x+i] for i in range(0,3) for x in [2,3,4]]
print (myFourthList)


#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
myFourthList = [[(lambda x:x+i) (x) for i in range(0,4)] for x in [2,3,4,5] ]
print (myFourthList)


#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
mySixthList = [(y,x) for x in (1,2,3) for y in (1,2,3)]
print (mySixthList)