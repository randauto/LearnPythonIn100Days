# df = pd.read_excel('banggiachuan.xlsx', sheet_name='Sheet1')
#
# print("Column headings:")
# print(df.columns)
#
#
# def showValue(cot):
#     for i in df.index:
#         print(df[cot][i])
#
#
# # showValue('Ten Hang')
# # showValue('Nhom Hang')
# # showValue(' Gia Bia ')
# showValue(' CTV ')


import excel2json

excel2json.convert_from_file('banggiachuan.xlsx')
