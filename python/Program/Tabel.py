class Table:
    def __init__(self):
        self.rows = 0
        self.columns = 0

    def create_table(self, n_rows, n_columns, table_content, table_header):
        max_per_column = [0]*n_columns

        # Find max per column
        for column in range(n_columns):
            max_per_column[column] = len(table_header[column])
            for row in range(n_rows):
                if len(table_content[row][column]) > max_per_column[column]:
                    max_per_column[column] = len(table_content[row][column])
            max_per_column[column] += 1

        # Create row separator
        self.row_separator(n_columns, max_per_column, '=')

        # Table header
        for column in range(n_columns):
            print("| " + table_header[column].ljust(max_per_column[column]), end="")
        print("|")

        # Create row separator
        self.row_separator(n_columns, max_per_column, '=')

        # Table content
        for row in range(n_rows):
            for column in range(n_columns):
                print("| " + table_content[row][column].ljust(max_per_column[column]), end="")
            print("|")
            self.row_separator(n_columns, max_per_column, '-')

    def row_separator(self, n_columns, max_per_column, symbol):
        for column in range(n_columns):
            print(symbol * (max_per_column[column] + 2), end="")
        print(symbol)
