from xlrd import open_workbook

wb = open_workbook("./data/objects.xls")
ws = wb.sheet_by_name("loginpage")
use_r = ws.nrows
# print(use_r)



# for i in range(0, use_r):
#     data = ws.row_values(i)
#     print(data)



# locators = { }
# for i in range(1, use_r):
#     data = ws.row_values(i)
#     locators[data[0]] = (data[1], data[2])
# print(locators)



# def read_locators(pagename):
#     wb = open_workbook("./data/objects.xls")
#     ws = wb.sheet_by_name(pagename)
#     use_r = ws.nrows
#     locators = {}
#     for i in range(1, use_r):
#         data = ws.row_values(i)
#         locators[data[0]] = (data[1], data[2])
#     return locators
# print(read_locators('loginpage'))
# print(read_locators('homepage'))
# print(read_locators('registrationpage'))



# def read_header(sheet_name, test_case_name):
#     wb = open_workbook('./data/testdata.xls')
#     ws = wb.sheet_by_name(sheet_name)
#     used_row = ws.nrows
#     for i in range(0, used_row):
#         row = ws.row_values(i)
#         if row[0] == test_case_name:
#             headers = ws.row_values(i-1)
#             headers = [header for header in headers if header]
#             return ",".join(headers)
# print(read_header('smoke','test_payment'))
# print(read_header('smoke', 'test_login_positive'))




#
# def read_data(sheet_name, test_case_name):
#     wb = open_workbook('./data/testdata.xls')
#     ws = wb.sheet_by_name(sheet_name)
#     used_row = ws.nrows
#     for i in range(0, used_row):
#         row = ws.row_values(i)
#         if row[0] == test_case_name:
#             data = [item for item in row if item]
#     print(data)
# print(read_data('smoke','test_registration'))


#
# def read_data(sheet_name, test_case_name):
#     wb = open_workbook('./data/testdata.xls')
#     ws = wb.sheet_by_name(sheet_name)
#     used_row = ws.nrows
#     for i in range(0, used_row):
#         row = ws.row_values(i)
#         if row[0] == test_case_name:
#             data = [item for item in row if item]
#             if data[1] == 'Yes':
#                 print(data)
#
# print(read_data('smoke','test_registration'))


#
# def read_data(sheet_name, test_case_name):
#     wb = open_workbook('./data/testdata.xls')
#     ws = wb.sheet_by_name(sheet_name)
#     used_row = ws.nrows
#     for i in range(0, used_row):
#         row = ws.row_values(i)
#         if row[0] == test_case_name:
#             data = [item for item in row if item]
#             if data[1] == 'Yes':
#                 print(data[2:])
#
# print(read_data('smoke','test_registration'))





def read_data(sheet_name, test_case_name):
    actual_data = [ ]
    wb = open_workbook('./data/testdata.xls')
    ws = wb.sheet_by_name(sheet_name)
    used_row = ws.nrows
    for i in range(0, used_row):
        row = ws.row_values(i)
        if row[0] == test_case_name:
            data = [item for item in row if item]
            if data[1] == 'Yes':
                actual_data.append(data[2:])
    return actual_data

print(read_data('smoke','test_registration'))

