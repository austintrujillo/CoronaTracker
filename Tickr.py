from escpos.printer import Usb
from datetime import datetime

class Tickr(object):

	def __init__(self, vendorId=0x6868, productId=0x0200, endpointIn=0x04, endpointOut=0x02,flip=False):
		super(Tickr, self).__init__()
		self.printer = Usb(vendorId, productId, in_ep=endpointIn, out_ep=endpointOut)
		self.printer.charcode('USA')
		self.printer.set(flip=flip)

	def printImage(self, filepath, align='CENTER'):
		self.printer.set(align=align.upper())
		self.printer.image(filepath)

	def printQrCode(self, content, size=9, align='CENTER'):
		self.printer.set(align=align.upper())
		self.printer.qr(content,size=int(size))

	def printText(self,text,align='LEFT', font='A', bold=False, underline=False, size=1, invert=False):
		type=''
		if bold or underline:
			if bold: type += 'B'
			if underline: type += 'U'
		else: type = 'NORMAL'
		self.printer.set(align=align.upper(), font=font.upper(), text_type=type.upper(), width=int(size), height=int(size), invert=invert)
		self.printer.text(text + '\n')

	def printSpace(self,qty=1):
		for i in range(qty):
			self.printText('\n')

	def printDateStamp(self,align='LEFT', font='A', bold=False, underline=False, size=1, invert=False):
		self.printText(datetime.now().strftime('%d %B %Y'),align=align, font=font, bold=bold, underline=underline, size=size, invert=invert)

	def finishTicker(self):
		self.printer.cut()