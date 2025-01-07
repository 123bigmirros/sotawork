import os
import pandas as pd

# 指定包含所有CSV文件的目录路径
folder_path = '/Users/mz/Desktop/Learn/knowledge/computer/ML/实习/sotawork/数据'  # 替换为存放CSV文件的目录路径

# 获取目录下所有CSV文件的文件名
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 创建一个空的DataFrame列表
dataframes = []

# 遍历CSV文件并读取内容
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path, encoding='utf-8',skiprows=1)  # 如果需要其他编码方式，如gbk，可替换为'gbk'
        
        
        
        df = df.iloc[1:]
        df = df.iloc[:, 1:4]
        df = df.dropna(subset=df.columns[0:4])
        df = df.dropna()
        df['厅名'] = csv_file.split('-')[1]
        print(df.head(20))
        dataframes.append(df)
        print(f"成功读取文件: {csv_file}")
    except Exception as e:
        print(f"读取文件失败: {csv_file}，错误: {e}")

# 将所有DataFrame合并为一个
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    # 指定输出文件的名称
    output_file = os.path.join(folder_path, 'combined_csv_file.csv')
    # 保存为一个新的CSV文件
    # combined_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"所有CSV文件已成功合并，输出文件: {output_file}")
    print(len(set(combined_df['厅名'].unique())))
else:
    print("未找到任何CSV文件或文件读取失败！")