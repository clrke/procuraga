
def get(table_name, start_index, number)
		return "SELECT * FROM %s LIMIT %s OFFSET %s" % table_name number start_index"
