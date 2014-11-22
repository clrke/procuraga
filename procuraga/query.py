def query(table_name, p1, p2=None)
	if (p2==None)
		return "SELECT * FROM %s LIMIT %s" % table_name p1 p2"
	else
		return "SELECT * FROM %s WHERE ROWNUM %s AND ROWNUM %s" % table_name p1 p2"
