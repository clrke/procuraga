def get(table_name, start_index, number):
	return 'SELECT * FROM "%s" LIMIT %s OFFSET %s' % (table_name, number, (number*start_index))

def year(table_name, year, number=-1):
	#year = str(year)
	# if number > 0:
	# 	return 'SELECT * FROM "%s" WHERE publish_date LIKE %s LIMIT %s' % (table_name, year, number)
	# else:
	return "SELECT * FROM \"{0}\" WHERE publish_date >= '{1}-01-01' and publish_date <= '{1}-12-31' LIMIT 10".format(table_name, year)

def pperunit(table_name, year,limit):
	return "SELECT org_name, publish_date, business_category, item_name,budget,qty,region, province FROM {0} WHERE bid.ref_id = item.ref_id and org.org_id = bid.client_agency_org_id ORDER BY publish_date desc LIMIT {2}".format(table_name,year,limit)
