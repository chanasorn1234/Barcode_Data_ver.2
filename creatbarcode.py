import random
import barcode 

id = random.randrange(1001,1050)
barcodeid = 885195235
rbarcodeid = str(barcodeid)
hr = barcode.get_barcode_class('ean13')
Hr = hr(str(rbarcodeid)+str(id))
qr = Hr.save('123')
