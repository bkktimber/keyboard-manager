pass_df = pd.DataFrame()
for event_file in wc_event_files:
    with open(event_file + '.json') as file:
        data = json.load(file)
        pass_df = pass_df.append(get_df(int(event_file[-4:]), 'pass', data))
print('Load {} events in WC2018'.format(pass_df.shape[0]))

pass_df.columns

pass_df.groupby(['team']).get_group('France')['length']

receipt_df = pd.DataFrame()
for event_file in wc_event_files:
    with open(event_file + '.json') as file:
        data = json.load(file)
        receipt_df = receipt_df.append(
            get_df(int(event_file[-4:]), 'ball receipt*', data))

print(receipt_df.shape[0])

receipt_df.sample()