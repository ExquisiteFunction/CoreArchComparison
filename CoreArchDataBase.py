class CoreArchDatabase(object):  # HTable):
    """
    A database to store cpu core arch info.
    """

    def __init__(self):
        self.name = "CoreArchDatabase"
        self.filepath = "CoreArchComparision.csv"
        self.row_map = {}
        self.column_map = {}
        self.row_size = 0
        self.column_size = 0
        self.data = []
        self.prop = []

        import csv
        csv_data = []
        with open('CoreArchComparision.csv', 'r') as f:
            for row in csv.reader(f):
                csv_data.append(row)
        self.row_size = len(csv_data)
        self.column_size = len(csv_data[0])
        for i in range(3, self.column_size-1, 1):
            column_name = csv_data[0][i]+"."+csv_data[1][i]
            self.column_map[column_name] = i-3
        for i in range(2, self.row_size, 1):
            row_name = ".".join(csv_data[i][:3])
            self.row_map[row_name] = i-2
            self.data.append(csv_data[i][3:-1])
            self.prop.append(1 if csv_data[i][-1] == "yes" else 0)
        self.row_size -= 2
        self.column_size -= 4

    def saveCSV(self):
        new_row = sorted(self.row_map.keys())
        for r in new_row:
            print(r, self.row_map[r])

    def show(self, row_filter, column_filter, is_save, filename):
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('TkAgg')

        sorted_row = sorted(self.row_map.items(), key=lambda x: x[1])
        shown_row, row_label = [], []
        for r, i in sorted_row:
            if re.match(row_filter, r) and self.prop[i] == 1:
                shown_row.append(i)
                row_label.append(r)
        shown_column, column_label = [], []
        for c, i in self.column_map.items():
            if re.match(column_filter, c):
                shown_column.append(i)
                column_label.append(c)
        if len(shown_column) == 0 or len(shown_row) == 0:
            print("Invalid query.")
            return
        # X = np.arange(len(shown_row))
        # Y = np.arange(len(shown_column))
        Z = [[float(self.data[i][j]) for i in shown_row] for j in shown_column]
        length = 1/(len(shown_column)+1)
        x = [np.arange(len(shown_row))+i * length
             for i in range(len(shown_column))]
        colors = ['skyblue', 'coral', 'lightgreen',
                  'chocolate', 'darkgray', 'pink']

        plt.subplots(1, 1)
        for i in range(len(shown_column)):
            plt.barh(y=x[i], width=Z[i], height=length,
                     label=column_label[i], color=colors[i % 6], alpha=1)
        plt.yticks(x[len(x) >> 1], row_label, ha="right")
        plt.legend()
        plt.tight_layout()
        if is_save:
            plt.savefig(filename)
        else:
            plt.show()


def usage():
    print("\n  Here is Core Architecture Infomation Database.")
    print("  Use regular expression to query and save results.\n")
    print("\t-r, --row\trow_filter\trow_filter in re format.")
    print("\t-c, --column\tcolumn_filter\tcolumn_filter in re format.")
    print("\t-s\t\tfilename\tsave figure with given name.")
    print("\t-h, --help\t\t\tprint help infomation.")


if __name__ == "__main__":
    import re
    import getopt
    import sys
    opts, args = getopt.getopt(sys.argv[1:], 'hr:c:s:',
                               ["row=", "column=", "help"])

    row_filter = ""
    column_filter = ""
    is_save = False
    filename = ""
    for o, a in opts:
        if o in ["-r", "--row"]:
            row_filter = re.compile(a)
        if o in ["-c", "--column"]:
            column_filter = re.compile(a)
        if o in ["-s"]:
            is_save = True
            filename = a
        if o in ["-h", "--help"]:
            usage()
            exit()
    cad = CoreArchDatabase()
    cad.show(row_filter, column_filter, is_save, filename)
# row_filter = "(.*)INT(.*)"
# column_filter = "(.*)Zen[2|3]"
# cad.show(row_filter=row_filter, column_filter=column_filter)
