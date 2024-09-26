import os
import pandas as pd
import matplotlib.pyplot as plt
market_caps={
    'AAPL':2300,
    'MSFT':2100,
    'GOOGL':1600,
    'TSLA':900,
    'BRK-B':600,
    'NVDA':500,
    'META':700,
    'JNJ':400,
    'V':500
}
top_10_companies={
    'AAPL':'Apple Inc.',
    'MSFT':'Microsoft corporation',
    'GOOGL':'Alphabet Inc.',
    'AMZN':'Amazon.com,Inc.',
    'TSLA':'Tesla,Inc.',
    'BRK-B':'Berkshire Hathaway Inc.',
    'NVDA':'NVIDIA Corporation',
    'META':'Meta Platforms,Inc.',
    'JNJ':'Johnson&Johnson',
    'V':'Visa Inc.'
}
Current_directory=os.path.dirname(os.path.abspath(_file_))
csv_file_path=os.path.join(current_dirctory,'top_10_stocks_sample_2013_2023.csv')
df=pd.read_csv(csv_file_path)
df['Date']=pd.to_datetime(df['Date'])
df['Year']=df['Date'].df.year
stock_columns=['AAPL_Close','MSFT_Close','GOOGL_Close','AMZN_Close','TSLA_Close','BRK-B_Close','NVDA_Close','META_Close','JNJ_Close','V_Close']
average_prices=df.groupby('year')[stock_columns]
mean().reset_Index()
plt.figure(figsize=(20,10))
bar_width=0.1
years=average_prices['year']
positions=[years+i*bar_width for i in range(len(stock_columns))]
for i,column in enumerate(stock_columns):plt.bar(positions[i],average_prices[column],width=bar_width,label=column.split('_')[0])
plt.xlabel('year')
plt.ylabel('Average closing price')
plt.title('Average closing price of top 10 stacks(2013_2023)')
plt.xticks(years+bar_width*4.5,years)
plt.legend()
plt.tight_layout()
plt.show()