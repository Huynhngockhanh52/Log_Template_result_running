import pandas as pd
import os

def to_int(s):
    try:
        return int(s)
    except ValueError:
        return 0

def create_dataframe_from_csv_files(directory):
    """
    Tạo một dataframe lưu trữ các giá trị khác nhau có trong tất cả các file csv trong một thư mục.

    Args:
        directory: Đường dẫn đến thư mục chứa các file csv.

    Returns:
        Dataframe chứa các giá trị khác nhau có trong tất cả các file csv.
    """
    # Lấy danh sách các file csv trong thư mục.
    csv_files = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if os.path.splitext(file)[1] == ".csv"
    ]
    # Khởi tạo một dataframe trống.
    dataframe = pd.DataFrame(columns=['EventId', 'EventTemplate', 'Occurrences'])
    # Lặp qua từng file csv.
    for csv_file in csv_files:
        # Đọc dữ liệu từ file csv.
        data = pd.read_csv(csv_file)
        dataframe = pd.concat([dataframe, data], ignore_index=True)

    # Thêm các giá trị duy nhất từ file csv vào dataframe dựa trên cột thứ 2.
    values = dataframe["EventTemplate"].unique()
    dataframe = dataframe.pivot_table(
        values=['EventId','Occurrences'], 
        index='EventTemplate', 
        aggfunc={'EventId': sum_str, 'Occurrences':"sum"})
    dataframe.to_csv("resultTemplate.csv", index=True)
    print(dataframe)

def sum_str(x):
    return x.unique()
create_dataframe_from_csv_files("demo_result10")
