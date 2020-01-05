# zpllibrary
A python library helping to generate ZPL.
This is ongoing and is currently in Beta with basic zpl types included

You can test generated code at http://labelary.com/viewer.html

## Usage:
### Single element
```
options = Options() #Sets Default options for rendering
simple_text_field = TextField("Content", 100, 100, Font(), True, False, NewLineConversion.Space)
zpl = Engine(simple_text_field).to_zpl_string(options)
print(zpl)
#Output
#^XA^A0N,30.0,30.0^FO100.0,100.0^FH^FDContent^FS^XZ

```
### Barcode
```
options = Options()
simple_barcode = Barcode39("Content", 100, 100, 200)
zpl = Engine(simple_barcode).to_zpl_string(options)
print(zpl)
#Output
#^XA^FO100.0,100.0^B3N,N,200.0,Y,N^FDContent^FS^XZ
```
### Whole label using all available elements
```
options = Options()

zpl_list = []
zpl_list.append(RawZpl('Check here'))
zpl_list.append(TextField("Some\nText", 10, 10, Font(), True, True, NewLineConversion.Space))
zpl_list.append(FieldBlock("more text is here", 10, 200, 300, Font(), 2))
zpl_list.append(TextBlock("more text is here than before", 10, 300, 400, 200, Font()))

zpl_list.append(Barcode128("123ABC", 100, 100))
zpl_list.append(Barcode39("123ABC", 100, 200))
zpl_list.append(BarcodeAnsi("123ABC", 100, 300, 100, "A", "D"))
zpl_list.append(QrCode("QR content", 100, 400, magnification_factor=12))
zpl_list.append(GraphicBox(100, 500, 100, 100))
zpl_list.append(GraphicDiagonalLine(100, 600, 100, 100))
zpl_list.append(GraphicEllipse(100, 700, 100, 100))
zpl_list.append(GraphicCircle(100, 800, 20))
zpl_list.append(GraphicHorizontalLine(100, 900, 20))
zpl_list.append(GraphicVerticalLine(100, 1000, 20))
zpl_list.append(GraphicSymbol(SpecialCharacter.canadian_standards_association_approval, 100, 100, 100, 100))
zpl_list.append(DownloadGraphic(500, 100, "C:\\Users\\scott\\Pictures\\download.png"))
zpl = Engine(zpl_list).render(options)
print(zpl)
```
