"""
    dump.py *** PATCHED ***
    place this file into "C:\Python27\lib\sqlite3\dump.py"
    *** MODIFIED WITH PATCH: http://bugs.python.org/file24429/sqlite3dump.patch ***
"""

# Mimic the sqlite3 console shell's .dump command
# Author: Paul Kippes <kippesp@gmail.com>

# Every identifier in sql is quoted based on a comment in sqlite
# documentation "SQLite adds new keywords from time to time when it
# takes on new features. So to prevent your code from being broken by
# future enhancements, you should normally quote any identifier that
# is an English language word, even if you do not have to."

def _iterdump(connection):
    """

    *** MODIFIED WITH PATCH: http://bugs.python.org/file24429/sqlite3dump.patch ***
    *** MODIFIED FURTHER BY drew bailey 2015-03-26 ***

    Returns an iterator to the dump of the database in an SQL text format.

    Used to produce an SQL dump of the database.  Useful to save an in-memory
    database for later restoration.  This function should not be called
    directly but instead called from the Connection method, iterdump().
    """

    cu = connection.cursor()
    yield('BEGIN TRANSACTION;')

    # sqlite_master table contains the SQL CREATE statements for the database.
    q = """
        SELECT "name", "type", "sql"
        FROM "sqlite_master"
            WHERE "sql" NOT NULL AND
            "type" == 'table'
        """
    schema_res = cu.execute(q)
    for table_name, type, sql in sorted(schema_res.fetchall()):
        if table_name == 'sqlite_sequence':
            yield('DELETE FROM "sqlite_sequence";')
        elif table_name == 'sqlite_stat1':
            yield('ANALYZE "sqlite_master";')
        elif table_name.startswith('sqlite_'):
            continue
        # NOTE: Virtual table support not implemented
        #elif sql.startswith('CREATE VIRTUAL TABLE'):
        #    qtable = table_name.replace("'", "''")
        #    yield("INSERT INTO sqlite_master(type,name,tbl_name,rootpage,sql)"\
        #        "VALUES('table','{0}','{0}',0,'{1}');".format(
        #        qtable,
        #        sql.replace("''")))
        else:
            yield('{0};'.format(sql))
 
        # Build the insert statement for each row of the current table
        table_name_ident = table_name.replace('"', '""')
        res = cu.execute('PRAGMA table_info("{0}")'.format(table_name_ident))
        column_names = [str(table_info[1]) for table_info in res.fetchall()]
        q = """SELECT 'INSERT INTO "{0}" VALUES({1})' FROM "{0}";""".format(
            table_name_ident,
            ",".join("""'||quote("{0}")||'""".format(col.replace('"', '""')) for col in column_names))
        query_res = cu.execute(q)
        for row in query_res:
            yield("{0};".format(row[0]))

    # Now when the type is 'index', 'trigger', or 'view'
    q = """
        SELECT "name", "type", "sql"
        FROM "sqlite_master"
            WHERE "sql" NOT NULL AND
            "type" IN ('index', 'trigger', 'view')
        """
    schema_res = cu.execute(q)
    for name, type, sql in schema_res.fetchall():
        yield('{0};'.format(sql))

    yield('COMMIT;')

    def CheckTableDump(self):
        expected_sqls = [
                """CREATE TABLE "index"("index" blob);"""
                ,
                """INSERT INTO "index" VALUES(X'01');"""
                ,
                """CREATE TABLE "quoted""table"("quoted""field" text);"""
                ,
                """INSERT INTO "quoted""table" VALUES('quoted''value');"""
                ,
                "CREATE TABLE t1(id integer primary key, s1 text, " \
                "t1_i1 integer not null, i2 integer, unique (s1), " \
                "constraint t1_idx1 unique (i2));"
                ]

"""
- Issue #9750: Fix sqlite3.Connection.iterdump on tables and fields
  with a name that is a keyword or contains quotes.

- Issue #13933: IDLE auto-complete did not work with some imported
  module, like hashlib.  (Patch by Roger Serwy)
"""
