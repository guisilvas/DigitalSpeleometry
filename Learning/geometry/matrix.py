from vector import Vector

class Matrix:
    def __init__(self, rows):
        rows = tuple(Vector(row) for row in rows)
        if len(rows) == 0:
            raise ValueError("Matrix cannot be empty.")
        n_cols = len(rows[0].coord)
        for row in rows:
            if len(row.coord) != n_cols:
                raise ValueError("Rows must have the same length.")
        self.rows = rows

    def __repr__(self):
        return str(self.rows)
    
    def n_rows(self):
        return len(self.rows)

    def n_cols(self):
        return len(self.rows[0].coord)

    def dim(self):
        return (self.n_rows(), self.n_cols())
    
    def has_diff_dim(self, other):
        return (len(self.rows) != len(other.rows)) or (len(self.rows[0].coord) != len(other.rows[0].coord))
    
    def has_diff_col_row(self, other):
        return self.n_cols() != other.n_rows()
    
    def check_sum_compatible(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Must be a matrix.")
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")
    
    def check_mult_compatible(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Must be a matrix.")
        if self.has_diff_col_row(other):
            raise ValueError("Incompatible dimension.")

    def diff(self, other):
        self.check_sum_compatible(other)
        result_rows = []
        for i in range(self.n_rows()):
            row = self.rows[i].diff(other.rows[i])
            result_rows.append(row.coord)
        return Matrix(result_rows)
    
    def sum(self, other):
        self.check_sum_compatible(other)
        result_rows = []
        for i in range(self.n_rows()):
            row = self.rows[i].sum(other.rows[i])
            result_rows.append(row.coord)
        return Matrix(result_rows)

    def scalar_mult(self, x):
        result_rows = []
        for i in range(self.n_rows()):
            row = self.rows[i].scalar_mult(x)
            result_rows.append(row.coord)
        return Matrix(result_rows)

    def inverse(self):
        result_rows = []
        
        return Matrix(result_rows)
