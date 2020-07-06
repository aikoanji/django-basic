import json, io, csv, base64, pandas


def generate_csv(data="", header=[], fields=[]):
    csv_file = io.StringIO()
    rows_data = json.dumps(data)
    rows = json.loads(rows_data)
    writer = csv.writer(csv_file)
    header.insert(0, "No")
    fields.insert(0, "no")
    writer.writerow(header)
    no = 1
    for x in rows:
        x['no'] = no
        writer.writerow([x[i] for i in fields])
        no += 1

    value = csv_file.getvalue()
    encode = base64.b64encode(bytes(value, 'utf8')).decode('utf8')
    return encode



def generate_xls_base64(data, column=[], field=[], header=[], title=None, sheet_name="Sheet1"):
    def get_col_widths(dataframe):
        # First we find the maximum length of the index column
        idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
        # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
        return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]

    dt = []
    if data:
        # set data
        for z in data:
            tmp_dt = []
            for i in field:
                tmp_dt.append(z[i])
            dt.append(tmp_dt)

    # initiate position row of data
    position_row_dt = 1 if title else 0
    position_row_dt += len(header) + 2 if header else 0

    df = pandas.DataFrame(dt, columns=column)
    output = io.BytesIO()
    writer = pandas.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name, index=False, startrow=position_row_dt, startcol=1, header=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    position_row = 0
    count_columns = len(df.columns)

    # if has title
    if title and title != "":
        title_format = workbook.add_format({
            'bold': True,
            'text_wrap': False,
            'font_size': 16,
            'align': 'left'})
        worksheet.merge_range(0, 0, 0, count_columns, "")
        worksheet.write(0, 0, title, title_format)

        # plus next row position if title is exists
        position_row += 1

    # if has header
    if header:
        header_format = workbook.add_format({'bold': True, 'align': 'right'})
        for x, i in enumerate(header):
            x += position_row
            worksheet.merge_range(x, 0, x, 1, x)
            worksheet.merge_range(x, 2, x, count_columns, x)
            worksheet.write(x, 0, "%s : " % i['label'], header_format)
            worksheet.write(x, 2, i['value'] if i['value'] is not None and i['value'] != "" else "All %s" % i['label'])

        # plus next row position if header is exists
        position_row += len(header)

    # separator column
    worksheet.merge_range(position_row, 0, position_row, count_columns, "")

    # plus next row position
    position_row += 1

    # Add a header format.
    column_header_format = workbook.add_format({
        'bold': True,
        'text_wrap': False,
        'valign': 'middle',
        'align': 'center',
        'font_color': '#ffffff',
        'fg_color': '#044272',
        'border': 1})

    # Write the column headers with the defined format.
    worksheet.write(position_row, 0, "No", column_header_format)
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(position_row, col_num + 1, value, column_header_format)

    # plus next row position after header
    position_row += 1

    # add index no
    loop = position_row
    for row_num, value in enumerate(data):
        worksheet.write(loop, 0, "%s." % str(row_num + 1), workbook.add_format({'align': 'center'}))
        loop += 1

    # set width column
    for i, width in enumerate(get_col_widths(df)):
        worksheet.set_column(i, i, width)

    writer.save()
    writer.close()

    encode = base64.b64encode(output.getvalue()).decode('utf8')

    return encode