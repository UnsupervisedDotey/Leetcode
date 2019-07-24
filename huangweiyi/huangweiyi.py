import pandas as pd


if __name__ == "__main__":

    # key：ADAR,ENST00000292205:c.1280A>G
    # value：A-1
    #
    # serial_number = pd.read_excel(r"/Users/lfl/PycharmProjects/Leetcode/huangweiyi/Varient type-coding-patients(3).xlsx")
    # serial_num_dict = dict(zip(list(serial_number['Variant']), list(serial_number['hwy'])))

    # print(serial_num_dict)
    #
    # patient = pd.read_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/patient coding variants.xlsx')

    # 新建excel
    # out_df = pd.DataFrame(columns=list(patient.columns)+["hwy_num"])
    #
    # for row in patient.iterrows():
    #     row[1]["hwy_num"] = serial_num_dict.get(row[1]["variant type"], "")
    #     row_Data = pd.Series(row[1])
    #     # print(row_Data)
    #     out_df = out_df.append(row_Data, ignore_index=True)

    # 去空
    # # for row_out in out_df.iterrows():
    # #     if row_out[1]['hwy_num'] == "":
    # #         out_df = out_df.drop(row_out[0])
    #
    # out_df.to_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/add_hwy_num_all.xlsx', index=False, header=True)

    # 总结出identifier的所有hwy_num
    # identifier = pd.read_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/add_hwy_num_all-patients.xlsx',
    #                            sheet_name="Sheet2")
    #
    # k_id_v_all_hwy_num = dict()
    #
    # for row in identifier.iterrows():
    #     k_id_v_all_hwy_num.setdefault(row[1]['Identifier'], [])
    #     k_id_v_all_hwy_num[row[1]['Identifier']].append(row[1]['hwy_num'])
    #
    # print(k_id_v_all_hwy_num)

    # 新建一列装组合
    # out_df_group = pd.DataFrame(columns=list(identifier.columns)+["hwy_num_group"])
    #
    # for row in identifier.iterrows():
    #     row[1]["hwy_num_group"] = ",".join(k_id_v_all_hwy_num.get(row[1]["Identifier"], []))
    #     row_Data = pd.Series(row[1])
    #     out_df_group = out_df_group.append(row_Data, ignore_index=True)
    #
    # out_df_group.to_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/add_hwy_num_combination.xlsx',
    #                       index=False, header=True)
    #

    # 对照组
    print("对照组 对照组 对照组 对照组 对照组 对照组")

    # # 帮忙编号
    # variant = pd.read_excel(r"/Users/lfl/PycharmProjects/Leetcode/huangweiyi/Varient type-coding-control.xlsx")
    #
    # # ad_control_num = pd.DataFrame(columns=['variant type', 'control_num'])
    # ad_control_num = variant
    # ad_control_num['control_a-z'] = [v[0] for v in list(variant['variant type'])]
    #
    # control_count = ad_control_num.groupby("control_a-z").count()
    #
    # print(list(control_count.index)[0])
    # print(control_count.loc[list(control_count.index)[0]])

    serial_number = pd.read_excel(r"/Users/lfl/PycharmProjects/Leetcode/huangweiyi/Varient type-coding-control.xlsx")
    serial_num_dict = dict(zip(list(serial_number['variant type']), list(serial_number['hwy'])))

    print(serial_num_dict)

    patient = pd.read_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/Control-variants.xlsx')

    # 新建excel
    out_df = pd.DataFrame(columns=list(patient.columns)+["hwy_num"])

    for row in patient.iterrows():
        row[1]["hwy_num"] = serial_num_dict.get(row[1]["variant type"], "")
        row_Data = pd.Series(row[1])
        out_df = out_df.append(row_Data, ignore_index=True)

    # 去空
    # # for row_out in out_df.iterrows():
    # #     if row_out[1]['hwy_num'] == "":
    # #         out_df = out_df.drop(row_out[0])

    # out_df.to_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/add_hwy_num_all.xlsx', index=False, header=True)

    # 总结出identifier的所有hwy_num
    identifier = out_df[['Identifier', "hwy_num"]]

    k_id_v_all_hwy_num = dict()

    for row in identifier.iterrows():
        k_id_v_all_hwy_num.setdefault(row[1]['Identifier'], [])
        k_id_v_all_hwy_num[row[1]['Identifier']].append(row[1]['hwy_num'])

    print(k_id_v_all_hwy_num)

    # 新建一列装组合
    out_df_group = pd.DataFrame(columns=list(identifier.columns)+["hwy_num_group"])

    for row in identifier.iterrows():
        row[1]["hwy_num_group"] = ",".join(k_id_v_all_hwy_num.get(row[1]["Identifier"], []))
        row_Data = pd.Series(row[1])
        out_df_group = out_df_group.append(row_Data, ignore_index=True)

    out_df_group.to_excel(r'/Users/lfl/PycharmProjects/Leetcode/huangweiyi/control_hwy_num_combination.xlsx',
                          index=False, header=True)
