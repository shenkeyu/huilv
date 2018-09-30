def main():
    #汇率
    USD_VS_RMB = 6.77
    currency_str_value = input('请输入金额：')
    i = 0
    unit = currency_str_value[-3:]
    while currency_str_value != 'Q':
        i = i+1
        print('循环次数为', i)
        if unit == 'CNY':
            rmb_str_value = currency_str_value[:-3]
            rmb_str_value = eval(rmb_str_value)
            #usd_value = rmb_str_value / USD_VS_RMB
            usd_value_commute = lambda x: x / USD_VS_RMB
            usd_value = usd_value_commute(rmb_str_value)

            print('美元（USD）金额是：', usd_value)
        elif unit == 'USD':
            usd_str_value = currency_str_value[:-3]
            usd_str_value = eval(usd_str_value)
            rmb_value = usd_str_value * USD_VS_RMB
            print('人民币（CNY）金额是：', rmb_value)
        else:
            print('目前版本不支持此货币！')
        print('*********************************')
        currency_str_value = input('请输入金额：(输入Q退出)')

    print("正常退出程序！")

if __name__ == '__main__':
    main()
