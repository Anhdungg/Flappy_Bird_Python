class Car:
    def __init__(self, hangXe, tenXe, mauSac, soBanhXe):
        self.hangXe = hangXe
        self.tenXe = tenXe
        self.mauSac = mauSac
        self.soBanhXe = soBanhXe

    def getHangXe(self):
        return  self.hangXe

    def setHangXe(self, hangXe):
        self.hangXe = hangXe

    def getTenXe(self):
        return  self.tenXe

    def setTenXe(self, tenXe):
        self.tenXe = tenXe
    
    def getMauSac(self):
        return  self.mauSac

    def setMauSac(self, mauSac):
        self.mauSac = mauSac

    def getSoBanhXe(self):
        return self.soBanhXe

    def setSoBanhXe(self, soBanhXe):
        self.soBanhXe = soBanhXe

    def chayXe(self):
        return "Xe dang chay"

    def khoiDongXe(self):
        return "Khoi dong xe"

    def dungXe(self):
        return "Dung xe"
    

honda = Car("Honda", "Civic", "Bac", 3)

mauSac = honda.getMauSac()
# honda.setHangXe("Yamaha")
print(mauSac)
