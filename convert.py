import xlrd

file_name = input('Please put this script alongside with the spec excel file.\nPlease input the file name: ')
book = xlrd.open_workbook(file_name+'.xlsx')
sh = book.sheet_by_index(0)

spec_dict = {}

prefix = '<div id="ProdSummary" class="prod-div"><div id="specs-table"><br><br><div><table class="table table-bordered table-hover table-striped"><tr style="display:none"><th>Specifications</th><th></th></tr>'
postfix = '</table></div></div>'

infix = []
for row_num in range(sh.nrows):
    row = sh.row(row_num)
    property_name = str(row[0].value)
    property_value = str(row[1].value)
    if property_value.endswith(".0"):
        property_value = property_value[:-2]
    infix.extend(['<tr><td><b>', property_name, '</b></td><td><span>', property_value, '</span><br></td></tr>'])
print(prefix + ''.join(infix) + postfix)
