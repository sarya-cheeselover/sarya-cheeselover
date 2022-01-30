#!/usr/bin/env python3

### before you run the code, check comments and functionality so you don't end up messing up your sheet or get confused.
### three # means a comment where one # is "disabled" statment.


### first you need to enable API access for a project from google and download the JSON file (google that if needed)
### you would probably use the service_account as it's safer from OAuth client_id
### open the JSON file and share the sheet you want to access with "client_email"
### you need also the path to the JSON file

import gspread

###create connectiong with google sheet. make sure you put the right path to your json file
gc = gspread.service_account(filename='PATH TO THE KEY FILE DOWNLOADED')

### create and open a spreadsheet instant. you can open it by name, key or URL. The method will change.
test_api_sh = gc.open("API testing")

###now let's test if it's working and print the value in the first cell.
print ("printing cell A1 from first sheet: \n" , test_api_sh.sheet1.get('A1'))

### to create a new spreadsheet..
# new_spreadsheet = gc.create('new spreadsheet')

### If you’re using a service account, this new spreadsheet will be visible only to this account.
### To be able to access newly created spreadsheet from Google Sheets with your own Google account you must share it with your email.
### See how to share a spreadsheet in the statment below.
# new_spreadsheet.share('name@email.com', perm_type='user',role='writer')

### let's select a working sheet!! not spreadsheet
sheet_1 = test_api_sh.get_worksheet(0)
###or
sheet_2 = test_api_sh.worksheet("Sheet2")
### full list of worksheets:
worksheet_list = test_api_sh.worksheets() # to view the list you have to print it
###creating a worksheet:
# script_worksheet = test_api_sh.add_worksheet(title='script worksheet',rows=1000, cols=24)
###as you create you shall delete my friend
# test_api_sh.del_worksheet(test_api_sh.worksheet('script worksheet'))

###let's get the value of cell A1 in sheet_2
print("printing cell A1 from second sheet: \n",sheet_2.acell('A1').value)
print ("printing the formula inside cell B1 in second sheet: \n",sheet_2.acell('B1',value_render_option='FORMULA').value) # it returns it as a string ;)

###get all values from a row or a column
row_vals = sheet_2.row_values(1)
print("printing the second value from first row: \n",row_vals[1])

col_vals = sheet_2.col_values(1)
print ("printing the seecond value from second column: \n",col_vals[1])

### off course those are basics...
###when dealing with a lot of data it's waay better to retrieve a bigger amount of data at once


###get all values from a worksheet as list of lists
list_of_list = sheet_2.get_all_values() #list length = to longest row in the sheet, if row is shorter than that, it's then filled with empty strings"
print ("getting all the values from second sheet as list of lists = \n",list_of_list[1])

###get all values from a worksheet as list of dicts
list_of_dicts = sheet_2.get_all_records() #if header is missing, the value probably won't be retrieved
print ("getting all the values from the second sheet as list of dicts: \n", list_of_dicts[0])
