def get(table_name, start_index, number):
	return 'SELECT * FROM "%s" LIMIT %s OFFSET %s' % (table_name, number, (number*start_index))

def year(table_name, year, number=-1):
	#year = str(year)
	# if number > 0:
	# 	return 'SELECT * FROM "%s" WHERE publish_date LIKE %s LIMIT %s' % (table_name, year, number)
	# else:
	return "SELECT * FROM \"{0}\" WHERE publish_date >= '{1}-01-01' and publish_date <= '{1}-12-31' LIMIT 10".format(table_name, year)
def pperunit(table_name, year,limit):
	return "SELECT item_name,budget,qty FROM \"{0}\" WHERE  modified_date >= '{1}-01-01' and modified_date <= '{1}-12-31' LIMIT {2} ".format(table_name,year,limit)
