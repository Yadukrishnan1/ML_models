# Converting a string to datetime object

date_string = "21 June, 2018"

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

"""
%d - Represents the day of the month. Example: 01, 02, ..., 31
%B - Month's name in full. Example: January, February etc.
%Y - Year in four digits. Example: 2018, 2019 etc. 
and 
many 
more (check https://www.programiz.com/python-programming/datetime/strptime)
"""

#---------------------------------------------------------------
# Using groupby in pandas for plotting monthly sales of a company

ts=sales.groupby(["date_block_num"])["item_cnt_day"].sum()
ts.astype('float')
plt.figure(figsize=(16,8))
plt.title('Total Sales of the company')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.plot(ts);


