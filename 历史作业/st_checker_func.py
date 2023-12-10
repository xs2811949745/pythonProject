# coding=utf-8

## ST 检查
st_target_list = ["21", "22", "23", "24", "25", "26", "27", "31", "32", "33", "34", "35", "36", "37", "38", "39", "41",
                  "51", "52", "91"]


# st_target_list 未来可从packet-schema.json 读


def check_st(st_str):
    try:
        st_v = st_str.split("=")[1]
        # print(st_v)
        if (len(st_v)==0):
            raise ValueError("ST无值")
        elif st_v not in st_target_list:
            raise ValueError("ST值域错误")
    except ValueError as e:
        raise (e)
    # except IndexError as e:
    #     print(e)
    #     raise ValueError("ST格式不合法")
    # except Exception as e:
    #     print(e)
    #     raise ValueError(str(e))


if __name__ == '__main__':
    st_str_input = "ST=21"
    try:
        check_st(st_str_input)
    except Exception as e:
        print(repr(e))