__author__ = 'drew bailey'
"""
Mimic_lite objects are nested lists with mimic functionality. This makes a trade between processing time and
virtual memory space. The lite object makes the trade in favor of a small memory object at the cost of processing time.
"""

from ...util import clean, collect_garbage
from .excel_objects import *
from .simple_types import *
from .errors import *
from operator import itemgetter
import itertools
import inspect
import copy
import csv
import re


### NEEDED???
# data_encoding = _data_encoding
try_encoding = ['ascii', 'utf-8', 'ISO-8859-1', 'windows-1252']
null = [None, False, [], (), [()], [None, ], (None, ), [(None), ]]

likely_dates = ['dt', 'date', 'dates', 'dts']
likely_dividers = ['^', '$', ' ', '_']

# clean_level = None


class Vector(list):
    """
    Vector objects are designed to represent the COLUMN VECTORS that make up Matrix objects.
    zip(*columns) (or the Matrix.rows() method) will efficiently return a list of tuples that can be used as rows.
    Vectors can however be used as any n-dimensional object.
    """

    def __init__(self, elements=None, clean_level=0, parse_dates=False):
        """
        ...
        :param elements: Iterable of vector elements.
        :param clean_level: How many restrictions to apply for SQL keyword and character cleaning.
        :param parse_dates: Will attempt to parse all elements to datetime objects if strings.
        :return:
        """
        super(self.__class__, self).__init__()
        self._name = None
        self.simple_type = None
        if elements:
            elements, types = self.load_vector(elements=elements, clean_level=clean_level, parse_dates=parse_dates)
            self.extend(elements)
            self.simple_type = max(types)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = clean(raw=str(value), sql=Matrix.clean_level)
        # if self.likely_date_column(value):
        #     self.__init__(elements=self[:], clean_level=Matrix.clean_level, parse_dates=True)
        self._name = value

    @name.deleter
    def name(self):
        self._name = None

    @staticmethod
    def likely_date_column(name):
        """
        Enumerates all outcomes of likely_divider, likely_date, likely_divider combos, if column name is in this return
        True, else return False.
        :param name: Column name to test
        :return: boolean, True if likely date, else False
        """
        l = [likely_dividers, likely_dates, likely_dividers]
        all_likely = [''.join(x) for x in list(itertools.product(*l))]
        if name:
            for rule in all_likely:
                if re.search(rule, name.lower()):
                    return True
        return False

    def __str__(self):
        if self:
            return '%-12s%s' % (self.name, '['+', '.join([str(x) for x in self])+']')
        else:
            return None

    def __repr__(self):
        if self:
            return 'Vector([%s])' % ', '.join([x.__repr__() for x in self])
        else:
            return None

    def load_vector(self, elements, clean_level=0, parse_dates=False):
        vector, types = [], []
        for element in elements:
            e, t = self.load_element(element=element, clean_level=clean_level, parse_dates=parse_dates)
            vector.append(e)
            types.append(t)
        return vector, types

    @staticmethod
    def load_element(element, clean_level=0, parse_dates=False):
        element, py_type = explicit_py_type(obj=element, parse_dates=parse_dates)
        simple_type = explicit_simple_type(py_type=py_type)
        if simple_type in [SimpleTEXT, SimpleNONE, SimpleNULL]:
            element = clean(raw=element, sql=clean_level)
        return element, simple_type

    # def name_from_element(self, index=0):
    #     self.name = []

    def clear(self, full=True):
        """
        Clears self.
        :param full: If full self becomes [], else it becomes [None]*len(self)
        :return:
        """
        if full:
            del self[:]
        else:
            cleared = [None]*len(self)
            del self[:]
            self.extend(cleared)

    def drop_types(self):
        self.simple_type = None

    def gtin_to_upc(self):
        """ Drops the last digit of each element in a vector. Skips None type objects. """
        l = []
        for element in self:
            if element:
                l.append(int(str(int(element))[:-1]))
        self.clear(full=True)
        self.extend(l)

    def upc_to_gtin(self):
        l = []
        for element in self:
            l.append(self.__compute_check_digit(element))
        self.clear(full=True)
        self.extend(l)

    def x_to_mfc_cd(self):
        """
        Drops all but the left five digits of each element in a vector. Skips None type objects.
         - 'mfc cd' stands for manufacturer code.
        """
        l = []
        for element in self:
            if element:
                l.append(int(str(int(element))[:5]))
        self.clear(full=True)
        self.extend(l)

    def slu_to_upc(self):
        """
        Adds five zeros to the end of a SLU.
        """
        l = []
        for element in self:
            if element:
                l.append(int(str(int(element))+'00000'))
        self.clear(full=True)
        self.extend(l)

    def slu_to_gtin(self):
        """
        Adds five zeros to the end of a SLU then computes a check digit.
        """
        l = []
        for element in self:
            l.append(self.__compute_check_digit(int(str(int(element))+'00000')))
        self.clear(full=True)
        self.extend(l)

    @staticmethod
    def __compute_check_digit(upc, n=14):
        """
        Compute the check digit for an n digit UPC code.
        :param upc: Code to compute check digit for.
        :return: GTIN code, (UPC + Check Digit).
        """
        gtin = upc
        if upc:
            upc_ = str(int(upc)).strip()
            diff = (n-1)-len(upc_)
            upc_ = '0'*diff+upc_
            odd, even = 0, 0
            for i, digit in enumerate(upc_):
                if (i+1) % 2 == 0:
                    even += int(digit)
                else:
                    odd += int(digit)
            odd *= 3
            result = 10 - ((odd+even) % 10)
            if result == 10:
                result = 0
            gtin = int(upc_+str(result))
        return gtin

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def append(self, item):
        item, simple_type = self.load_element(element=item)
        self.simple_type = max(self.simple_type, simple_type)
        super(self.__class__, self).append(item)

    def make_date(self):
        self[:], simple_types = self.load_vector(elements=self[:], clean_level=Matrix.clean_level, parse_dates=True)
        self.simple_type = SimpleDATETIME


class Matrix(object):
    """
    Matrix objects are grouping of vector objects.
    Data is loaded row first and is referenced column first.
    """

    clean_level = 0
    dominant_load = True

    def __init__(self, data=None, header=True):
        self.name = ''
        self._columns = []
        if data:
            self.load_matrix(vectors=data, header=header)

        self.min_print_length = 14
        self.max_print_length = 20
        self.max_print_rows = 40

    @property
    def columns(self):
        """
        List of header names
        """
        return self._columns

    @columns.setter
    def columns(self, value):
        # don't let users reset vectors
        # self._columns = value
        self.__init__(data=value)

    @columns.deleter
    def columns(self):
        self._columns = []

    def __repr__(self):
        r, c = self.dimensions()
        self_str = '<%s by %s 2D Matrix object at %s>' % (r, c, id(self))
        if self.name:
            self_str = '<%s by %s 2D Matrix object "%s" at %s>' % (r, c, self.name, id(self))
        return self_str
        # return self.__str__()

    def __str__(self):
        """
        Prints a Matrix object in a readable way.
        """
        # max_row_length = None  # make this lap the the next row if too long...
        max_rows = self.max_print_rows
        repr = self.rows()[:max_rows]
        if repr:
            names, lengths, rules = [], [], []
            min_length = self.min_print_length
            max_length = self.max_print_length
            for item in self.columns:
                if not item:
                    lengths.append(min_length)
                    names.append('None')
                elif len(item.name) > max_length:
                    lengths.append(max_length)
                    names.append(item.name[:max_length-2]+'..')
                elif len(item.name) < min_length:
                    lengths.append(min_length)
                    names.append(item.name)
                else:
                    lengths.append(len(item.name))
                    names.append(item.name)
            for i in range(len(self.columns)):
                rules.append("-"*lengths[i])
            format = " ".join(["%%-%ss" % l for l in lengths])
            result = [format % tuple(names)]
            result.append(format % tuple(rules))
            for row in repr:
                print_row = []
                for i, value in enumerate(row):
                    if value:
                        if len(str(value)) > lengths[i]:
                            value = str(value)[:lengths[i]-2]+'..'
                    print_row.append(value)
                result.append(format % tuple(print_row))
            return "\n" + "\n".join(result)
        return "Empty or corrupt Matrix object at %s" % id(self)

    def __getitem__(self, key):
        """
        Always columns before rows.
        Supports [column][row] object assignment, column can be either a name or an index.
        """
        key = self.get_index(key=key)
        return self.columns[key]

    def __setitem__(self, key, value, header=False):
        key = self.get_index(key=key)
        value.extend([None] * abs(len(value) - len(self[0])))
        vec = Vector(elements=value, clean_level=self.clean_level)
        if header is True:
            header = vec.pop(0)
        elif header:
            if hasattr(header, '__iter__') and not isinstance(header, basestring):
                header = header[0]
            header = clean(raw=header, sql=self.clean_level)
        else:
            try:
                header = self.header()[key]
            except:
                if type(key) is int or not key:
                    header = 'col_' + str(len(self.columns))
                else:
                    header = key
        vec.name = header
        if key in range(len(self.columns)):
            self.columns[key] = vec
        else:
            try:
                self.columns.insert(key, vec)
            except TypeError:
                self.columns.insert(len(self.columns), vec)

    def __delitem__(self, key):
        key = self.get_index(key=key)
        del self.columns[key]

    def __reversed__(self):
        self._columns.reverse()

    def __contains__(self, element):
        """
        Iterates columns for membership check. (Would prefer a method that does not iterate all elements).
        :param element:
        :return:
        """
        for vector in self._columns:
            if element is vector:
                return True
            if element in vector:
                return True
        return False

    def __nonzero__(self):
        """
        Sets bool(self) return.
        """
        if not self._columns:
            return False
        return True

    def __eq__(self, other):
        try:
            if self.columns == other.columns:
                return True
            return False
        except:
            return False

    def __len__(self):
        """
        :return: Length of first column
        """
        if self:
            return len(self._columns)
        else:
            return 0

    def __iter__(self):
        return iter(self.columns)

    def __add__(self, other):
        base = copy.deepcopy(self)
        if self is other:  # avoids infinite loop caused by appending list to itself.
            other = copy.deepcopy(other)

        layer_1a = hasattr(other, '__iter__')
        layer_2a = hasattr(other[0], '__iter__')
        layer_1b = isinstance(other, Vector)
        layer_2b = isinstance(other[0], Vector)

        if layer_2b:
            for item in other:
                base._add_vector(matrix=base, vector=item)
        elif layer_1b:
            base._add_vector(matrix=base, vector=other)
        elif layer_2a:
            for item in other:
                item = base._load_vector(vector=item)
                base._add_vector(matrix=base, vector=item)
        elif layer_1a:
            other = base._load_vector(vector=other)
            base._add_vector(matrix=base, vector=other)
        else:
            raise LoadError("Unsupported object for matrix extension.")
        return base

    @staticmethod
    def _add_vector(matrix, vector):
        name = matrix.get_unique_header(header=matrix.header() + [vector.name])[-1]
        matrix[name] = vector

    def unite(self, other):
        base = copy.deepcopy(self)
        if len(base) > len(other):
            for x in range(abs(len(base)-len(other))):
                other += [None] * len(other.columns[0])
        elif len(base) < len(other):
            for x in range(abs(len(base)-len(other))):
                base += [None] * len(base.columns[0])
        for row in other.rows():
            base.append(row)
        return base

    def dimensions(self):
        """ Returns columns, rows """
        return len(self.columns), len(self.columns[0])

    def header(self):
        """ ... """
        return [h.name for h in self.columns]

    def simple_types(self):
        """ ... """
        return [c.simple_type for c in self.columns]

    def get_index(self, key):
        try:
            return self.header().index(key)
        except ValueError:
            return key

    def load_matrix(self, vectors, header):
        """ ... """
        vectors = zip(*vectors)
        for index, vector in enumerate(vectors):
            if header is True:
                name = clean(raw=vector.pop(0), sql=self.clean_level)
            elif header and header[index]:
                name = clean(raw=header[index], sql=self.clean_level)
            else:
                name = "col_" + str(index)
            parse_dates = Vector.likely_date_column(name=name)
            vector = self._load_vector(vector=vector, parse_dates=parse_dates)
            vector.name = name
            self._columns.append(vector)
            self[index].name = self.get_unique_header()[-1]

    def _load_vector(self, vector, parse_dates=False):
        return Vector(elements=vector, clean_level=self.clean_level, parse_dates=parse_dates)

    def rows(self):
        return zip(*self.columns)

    def iter_rows(self):
        for row in zip(*self.columns):
            yield row

    def elements(self):
        elements = []
        for column in self.columns:
            for element in column:
                elements.append(element)
        return elements

    def iter_elements(self):
        for column in self.columns:
            for element in column:
                yield element

    # def copy_columns(self, column):  # not finished
    #     new = copy.copy(column)
    #     pass

    def reorder(self, key_list):
        _key_list = [self.get_index(k) for k in key_list]
        # print _key_list  # broadcast this
        self._columns = [self._columns[k] for k in _key_list]
        for i, c in enumerate(self._columns):
            m = re.search('^col_\d+$', c.name)
            if m:
                c.name = 'col_' + str(i)

    def move_to_index(self, new_index, key):
        cur_index = self.get_index(key)
        column = self._columns.pop(cur_index)
        self._columns.insert(new_index, column)
        for i, c in enumerate(self._columns):
            m = re.search('^col_\d+$', c.name)
            if m:
                c.name = 'col_' + str(i)

    def get_unique_header(self, header=None, allow_space=True):
        if not header:
            header = self.header()
        new_header = []
        for index, item in enumerate(header):
            if not item:
                item = 'col_' + str(index)
            new_header.append(item)
        new_header.reverse()
        add_index = len(new_header)-len(set(new_header))
        unique_header = []
        for i, item in enumerate(new_header):
            if item in new_header[i+1:]:
                item = str(item) + '_' + str(add_index)
                add_index -= 1
            unique_header.append(item)
        unique_header.reverse()
        if not allow_space:
            unique_header = [item.replace(' ', '_') for item in unique_header]
        return unique_header

    def make_header_unique(self, allow_space=True):
        new_header = self.get_unique_header(allow_space=allow_space)
        for index, item in enumerate(new_header):
            self[index].name = item

    def extend(self, iterable):
        for row in iterable:
            self.append(row=row)

    def append(self, row):
        if len(row) != len(self):
            raise LoadError("Row of length %s cannot be appended to a matrix with %s columns" % (len(row), len(self)))
        for index, item in enumerate(row):
            self[index].append(item)

    def drop_row(self, index):
        for column in self.columns:
            del column[index]

    def drop_rows(self, indices):
        indices = list(set(indices))
        indices.sort()
        indices.reverse()
        for index in indices:
            self.drop_row(index)

    def drop_rows_where(self, conditions):
        """
        accepts a list tuples containing columns and value conditions as strings
            ex) conditions=[('column_one', "< 13"), ('column_nine', "=='hawaii'")]
        :param conditions: [(col1, evaluation to apply as string),]
        :return:
        """
        conditions_ = []
        for condition in conditions:
            column_index = self.get_index(key=condition[0])
            conditions_.append(str("row[%s] %s" % (column_index, condition[1])))
        drop_indices = [i for i, row in enumerate(self.rows()) if all(map(eval, conditions_))]
        if drop_indices:
            self.drop_rows(indices=drop_indices)

    def copy_vector(self, key):
        """ Appends a copy of the vector at key. """
        new = copy.deepcopy(self[key])
        new_name = self.get_unique_header()
        new.name = new_name
        self._columns.append(new)


class Mimic(Matrix):
    """
    High level data object used in rpt module. Intended to interact with reporting classes to enable easy read and write
    processes. Holds useful data information including name, sql (string of code used to generate), crs (a sql engine
    connection.cursor object). Maintains sql and added members on data merges.
    """

    auto_parse_dates = True

    @classmethod
    def from_csv(cls, file_name, header=True, delimiter=',', quote_char='"'):
        """
        Loads a Mimic instance data from a csv file.
        Uses builtin csv package.
        :param file_name: file name (including '.csv'), passed as mimic name
        :param header: if True use first line as header, if list use that as header if not use default vector names,
            defaults to True
        :param delimiter: csv file delimiter, defaults to ',' (comma)
        :param quote_char: csv quote character, defaults to '"', (double quote)
        :return: data, header, name to Mimic.__init__
        """
        with open(file_name, 'rb') as f:
            c = csv.reader(f, delimiter=delimiter, quotechar=quote_char)
            return cls(data=c, header=header, name=file_name)

    @classmethod
    def from_excel(cls, file_name, sheet_name, header=True, row_start=0, row_end=None, col_start=0, col_end=None):
        """
        Loads a Mimic instance with data from an excel range.
        Row and column start and end points are zero indexed integers.
        Uses xlrd package. ("pip install xlrd" to install).
        :param file_name: file name (including '.xlsx')
        :param sheet_name: worksheet name, passed as mimic name
        :param header: if True use first line as header, if list use that as header if not use default vector names,
            defaults to True
        :param row_start: row start index, defaults to 0
        :param row_end: row end index, defaults to 2,000,000
        :param col_start: column start index, defaults to 0
        :param col_end: column end index, defaults to 2,000,000
        :return: data, header, and name to Mimic.__init__
        """
        r = ExcelReader()
        data = r.read(file_name=file_name, sheet_name=sheet_name, row_start=row_start, row_end=row_end,
                      col_start=col_start, col_end=col_end)
        return cls(data=data, header=header, name=sheet_name)

    def __init__(self, data, header=None, name='', sql='', cursor=None):
        if not header and cursor:
            header = self.__get_header_from_cursor(cursor=cursor)
        super(self.__class__, self).__init__(data=data, header=header)
        self.name = name
        self.sql = sql
        self.cursor = cursor
        self.members = []
        print self.__repr__()
        print self

    def __repr__(self):
        if self._columns:
            r, c = self.dimensions()
            self_str = '<%s by %s 2D Mimic object at %s>' % (r, c, id(self))
            if self.name:
                self_str = '<%s by %s 2D Mimic object "%s" at %s>' % (r, c, self.name, id(self))
            return self_str
        return "Empty or corrupt Mimic object at %s" % id(self)

    def __add__(self, other):
        """
        Returns result of adding a primary object or iterable to this mimic.
        Differences from matrix __add__:
            cursors are an unsafe object to deepcopy, it is held apart while matrix __add__ runs and re-added after
            base cursor is set to this cursor
        :param other:
        :return:
        """
        base_crs = self.cursor
        self.cursor = None  # clears cursor for copy
        ### matrix method start ###
        base = copy.deepcopy(self)
        if self is other:  # avoids infinite loop caused by appending list to itself.
            other = copy.deepcopy(other)

        layer_1a = hasattr(other, '__iter__')
        layer_2a = hasattr(other[0], '__iter__')
        layer_1b = isinstance(other, Vector)
        layer_2b = isinstance(other[0], Vector)

        # add_vector = super(self.__class__, self)._add_vector
        if layer_2b:
            for item in other:
                base._add_vector(matrix=base, vector=item)
        elif layer_1b:
            base._add_vector(matrix=base, vector=other)
        elif layer_2a:
            for item in other:
                item = base._load_vector(vector=item)
                base._add_vector(matrix=base, vector=item)
        elif layer_1a:
            other = base._load_vector(vector=other)
            base._add_vector(matrix=base, vector=other)
        else:
            raise LoadError("Unsupported object for mimic extension.")  # 'matrix' changed to 'mimic'
        ### matrix method end ###
        self.__add_member(base=base, other=other)
        self.cursor = base_crs
        base.cursor = base_crs
        return base

    def union(self, other):
        base_cursor = self.cursor
        self.cursor = None
        ### Matrix method start ###
        base = self.unite(other=other)
        ### Matrix method end ###
        self.__add_member(base=base, other=other)
        self.cursor, base.cursor = base_cursor, base_cursor
        return base

    def to_csv(self, file_name='', delimiter=',', quote_char='"', header=True):
        if not file_name:
            if self.name:
                name = self.name
            else:
                name = 'mimic_data'
            file_name = name+'.csv'
        with open(file_name, 'wb') as f:
            c = csv.writer(f, delimiter=delimiter, quotechar=quote_char, quoting=csv.QUOTE_MINIMAL)
            if header:
                c.writerows([self.header()] + [row for row in self.iter_rows()])
            else:
                c.writerows(self.iter_rows())

    def to_excel(self, file_name=None, sheet_name=None):
        if not file_name and self.name:
            file_name = str(self.name) + '.xlsx'
        else:
            file_name = 'mimic_data.xlsx'
        w = ExcelWriter()
        w.write(mimic_list=[self], file_name=file_name, sheet_name=sheet_name)

    @staticmethod
    def __add_member(base, other):
        try:
            if base.sql and other.sql:
                base.sql += '\n\n' + other.name + ':' + '\n\n' + other.sql
        except AttributeError:
            pass
        try:
            if not base.members:
                base.members = []
            if other.name:
                base.members.append(other.name)
            else:
                raise AttributeError
        except AttributeError:
            base.members.append('unknown_member')

    @staticmethod
    def __get_header_from_cursor(cursor):
        return [desc.strip() for desc in list(zip(*cursor.description)[0])]

    def rank(self, partition_by, order_by, desc=False):
        """
        :param partition_by: key to partition by
        :param order_by: key to order by
        :param desc:
        :return:
        """
        part = self[partition_by]
        order = self[order_by]
        new = [None] * len(part)
        for item in set(part):
            root_indices, rank_indices, elements = [], [], []
            for i, x in enumerate(order):
                if part[i] == item:
                    root_indices.append(i)
                    elements.append(x)
            if desc:
                rank_indices = [sorted(elements, reverse=True).index(x) for x in elements]
            else:
                rank_indices = [sorted(elements).index(x) for x in elements]
            for root, rank in zip(root_indices, rank_indices):
                new[root] = rank + 1
        if desc:
            field_name = 'rank_%s_by_%s_desc' % (partition_by, order_by)
        else:
            field_name = 'rank_%s_by_%s' % (partition_by, order_by)
        self[field_name] = new

    # def order(self, keys):
    #     keys = [self.get_index(key=key) for key in keys]
    #     indices, values = zip(*sorted(enumerate(self.rows()), key=itemgetter(*keys)))
    #     for c, column in enumerate(self.columns):
    #         values = [column[i] for i in indices]
    #         for v, value in enumerate(values):
    #             self[c][v] = value