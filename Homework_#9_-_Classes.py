class Vehicle:
    def __init__(self,make,model,year,weight):
        self.needmain=False
        self.trip=0
        self.make_=make
        self.modelno=model
        self.year=year
        self.weight=weight
        #print(self.make_, self.modelno, self.year, self.weight)

    def setmake(self,xmake):
        self.make=xmake
    def setmodel(self,xmodel):
        self.modelno=xmodel
    def setyear(self, xyear):
        self.year=xyear
    def setweight(self,xweight):
        self.weight=xweight
class Cars(Vehicle):
    def __init__(self,make,model,year,weight):
        self.isdriving=False
        super(). __init__(make,model,year,weight)
    def drive(self):
        self.isdriving=True
    def stop(self):
        self.isdriving=False
        self.trip=self.trip+1
        if self.trip>100:
            self.needmain=True
    def Repair(self):
        self.trip=0
        self.needmain=False
    def print(self):
        print("Make: "+str(self.make_), "\nModel No.: "+str(self.modelno), "\nYear Of Manufacture: "+str(self.year), "\nWeight: "+str(self.weight))
        print("\tNeed Maintenance: "+str(self.needmain), "\tTrip:"+ str(self.trip))

o=Cars("Suzuki", 100021, 2000, 800)
o.drive()
o.stop()
o.print()
o=Cars("Chevrolet", 12413, 2014, 900)
o.drive()
o.stop()
o.drive()
o.stop()
o.print()
o=Cars("Tata", 98121, 2009, 690)
o.drive()
o.stop()
o.drive()
o.stop()
o.drive()
o.stop()
o.drive()
o.stop()
o.print()