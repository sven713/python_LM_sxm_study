original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
distinct_set = set(original_list)
print(distinct_set)



my_dict = {
    "lisi_info":[
        ("lisi","李四","小四"),
        {90,85,99}
    ],
    "wangwu_info":[
        ("wangwu","王五","小五"),
        (90,85,100)
    ]
}

print(my_dict, type(my_dict))

# 获取王五同学的100分成绩
print(my_dict["wangwu_info"][1][2])