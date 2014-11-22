def get(table_name, start_index, number):
	return 'SELECT * FROM "%s" LIMIT %s OFFSET %s' % (table_name, number, (number*start_index))

def year(table_name, year, number=-1):
	if number > 0:
		return 'SELECT * FROM "%s" WHERE publish_date LIKE %s LIMIT %s' % (table_name, year, number)
	else:
		return 'SELECT * FROM "%s" WHERE publish_date LIKE %s' % (table_name, year)
