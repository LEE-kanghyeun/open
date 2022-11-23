### 엑셀 자료 읽기 (read)

import win32com.client
import pandas as pd


class win_excel():

    def read_excel(x : int, y : int , address : str, sheet_name : str):
        """        X: ROW 개수,    Y: COLUMN 개수
        Returns dataframe from excel
        """

        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False  ## 엑셀 파일이 보이도록

        df = pd.DataFrame()
        excel_file3 = excel.Workbooks.Open(address)
        x_sheet3 = excel_file3.Worksheets(sheet_name)

        ##### 엑셀 읽어들이기 본문

        ## (2500,2500)의 범위를 한꺼번에 읽어들임
        df = pd.DataFrame(x_sheet3.Range(x_sheet3.cells(1, 1), x_sheet3.cells(x, y)).Value)

        # 빈칸 컬럼 제거 과정
        a = df.notnull().sum()
        df_new = pd.DataFrame()
        df_list = []
        for i in range(0, y):
            if a[i] != 0:
                df_list.append(list(df[i]))

            else:
                pass

        df_new = pd.DataFrame(df_list)
        # df_new = df_new.transpose()  : list -> df로 변경시, 행과 열이 바뀌나 어차피 다시 row를 제거할것이므로 transpose 필요 없음
        # print(df_new)

        # 빈칸 row 제거 과정
        a = df_new.notnull().sum()
        df_list = []

        for i in range(0, x):
            if a[i] != 0:
                df_list.append(list(df_new[i]))
            else:
                pass
        df_new = pd.DataFrame(df_list)  # : list -> df로 변경시, 행과 열이 다시한번 바뀌면서 원상복귀
        #        print(df_new, df_new.shape)

        excel_file3.Close(SaveChanges=False)
        return df_new

# ## Range(x_sheet3.cells(1,2501),x_sheet3.cells(2500,5000)의 범위를 추가 확인
# df = pd.DataFrame(x_sheet3.Range(x_sheet3.cells(1,2501),x_sheet3.cells(2500,5000)).Value)
# a =df.notnull().sum()
# df_list = []
# print(df, a)

# if a.sum() == 0:
#     print('pass')

# else :
#     # 빈칸 column 제거 과정
#     for i in range(0,2500):
#         if a[i] != 0:
#             df_list.append(list(df[i]))

#         else:
#             pass

#     df_add =  pd.DataFrame(df_list)
#     print(df_add)


#     # 빈칸 row 제거 과정
#     a = df_add.notnull().sum()
#     df_list = []

#     for i in range(0,2500):
#         if a[i] != 0:
#             df_list.append(list(df_add[i]))
#         else:
#             pass
#     df_add =  pd.DataFrame(df_list)   #  : list -> df로 변경시, 행과 열이 다시한번 바뀌면서 원상복귀
#     print(df_add, df_add.shape)
#     df_new = pd.concat(df_new, df_add)
#     print(df_new)


