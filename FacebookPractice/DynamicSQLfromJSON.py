import json

data = """[
   {
      "table": "place_nm",
      "inserts": [
            {
                  "fields": [
                     "lu_stat_id",
                      "lu_use_desig_id",
                       "place_nm"
                   ],
                    "values": [
                        1,
                        1,
                        "National Monument"
                    ]
            },
            {
                    "fields": [
                       "lu_stat_id",
                        "lu_use_desig_id",
                        "place_nm"
                     ],
                     "values": [
                        2,
                        1,
                        "Dulles Airport"
                     ]
              }
        ]
   }
]"""


def querycreate(tbl, ins):
    datatypes = ['int' if type(dt) is int else 'varchar' for dt in ins[0]['values']]
    fields = ins[0]['fields']
    op = [fields[i]+ ' ' + datatypes[i] for i in range(len(fields))]
    createquery = "Create table " + tbl + " (" + ",".join(op) + ')'
    print(createquery)
    # insertquery = "Insert into " + tbl + ' (' + ','.join(fields) + ')' + 'values' + ','.join(str(tuple(ins['values'])))
    # print(insertquery)
    #     print(insertquery)
    for val in ins:
        insertquery = "Insert into " + tbl + ' (' + ','.join(fields) + ')' + 'values' + str(tuple(val['values']))
        print(insertquery)



op = json.loads(data)
# print(op)
for inp in op:
    table = inp['table']
    inserts = inp["inserts"]
    querycreate(table, inserts)
