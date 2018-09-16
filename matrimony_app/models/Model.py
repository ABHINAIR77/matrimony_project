from flask import current_app
from pprint import pprint as pp

class Model:
    def create(self, dict_object):
        mysql = current_app.db
        cur = mysql.connection.cursor()

        cmd = "insert into " + self.table
        values = " values (NULL,"
        values_list = []
        for field in self.fields:
            values_list.append(dict_object[field])

        for val in values_list[:-1]:
            values += "'"+val+"',"

        cmd += values + "'"+values_list[-1]+"')"
        cur.execute(cmd)
        mysql.connection.commit()

        return True

    def get(self, filter=None):
        mysql = current_app.db
        cur = mysql.connection.cursor()

        cmd = 'select * from '+self.table+' '
        if filter:
            condition_list = []
            cmd += 'where '
            for key, value in filter.items():
                condition_list.append(key+'="'+value+'"')

            for conditions in condition_list[:-1]:
                cmd += conditions + "and"
            cmd += condition_list[-1]
        pp(cmd)
        cur.execute(cmd)
        result = cur.fetchone()
        pp(result)
        for index, value in enumerate(result):
            setattr(self, self.fields[index], value)
        return self

