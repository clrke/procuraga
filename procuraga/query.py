def get(table_name, start_index, number):
	return 'SELECT * FROM "%s" LIMIT %s OFFSET %s' % (table_name, number, (number*start_index))

def year(table_name, year, number=-1):
	return "SELECT * FROM \"{0}\" WHERE publish_date >= '{1}-01-01' and publish_date <= '{1}-12-31' LIMIT 10".format(table_name, year)

def pperunit(table_name, year):
	if year is None:
		return "SELECT org_name, publish_date, business_category, item_name, item_description, budget,qty,region, province FROM {0} WHERE qty <> 0 and budget <> 0 and bid.ref_id = item.ref_id and org.org_id = bid.client_agency_org_id ORDER BY publish_date desc LIMIT 1000".format(table_name)
	else:
		return "SELECT org_name, publish_date, business_category, item_name, item_description, budget,qty,region, province FROM {0} WHERE qty <> 0 and budget <> 0 and publish_date >= '{1}-01-01' and publish_date <= '{1}-12-31' and bid.ref_id = item.ref_id and org.org_id = bid.client_agency_org_id ORDER BY publish_date desc".format(table_name,year)
