'''
项目: MFPPC的语言文件
作者: NKid（简体中文、繁体中文和英语部分）
描述: MFPPC的语言文件。

項目: MFPPC的語言檔
作者: NKid（簡體中文、繁體中文和英語部分）
描述: MFPPC的語言檔。

Project: MFPPC's language file
Author: NKid(Simplified Chinese,Traditional Chinese and English part)
Description: MFPPC's language file.
'''

wr = {
    'p':
        '预编译...',
    'c':
        '编译...',
    'w':
        '写入...',
    'd':
        '完成',
    'a':
        '全部完成。',
}

wr_t = {
    'p':
        '預編譯...',
    'c':
        '編譯...',
    'w':
        '寫入...',
    'd':
        '完成',
    'a':
        '全部完成。 ',
}

wr_en = {
    'p':
        'Precompile...',
    'c':
        'Compile...',
    'w':
        'Write...',
    'd':
        'Done',
    'a':
        'All Works Done.',
}

wr_s = {
    'p':
        '',
    'c':
        '',
    'w':
        '',
    'd':
        '',
    'a':
        '',
}

w = {
    'help':
        '\n'
        '如果你想使用繁體中文, 請啟用以下開關“-t”或“--Traditional-Chinese”。\n'
        'If you are looking for English, use option "-e" or "--English".\n'
        '\n'
        'MCFunctionPlusPlus 编译器 由 NKid 制作\n'
        '\n'
        '使用方法:\n'
        '    mfppc [-h | --help] [<-o | --output> <输出文件夹>]\n'
        '          [-p | --only-precompile] [-s | --silent]\n'
        '          [<-n | --project-name> <项目名称>]\n'
        '          [<-t | --Traditional-Chinese> | <-e | --English>] <源代码>\n'
        '\n'
        '    -h 或 --help            显示此说明文档。\n'
        '    -o 或 --output          设置准备输出到的文件夹。\n'
        '    输出文件夹              准备输出到的文件夹。\n'
        '                            （默认输出到程序所在目录。）\n'
        '    -p 或 --only-precompile 只进行预编译。\n'
        '    -s 或 --silent          不输出编译信息。（仍输出错误信息。）\n'
        '    -n 或 --project-name    设置项目的名称\n'
        '    项目名称               项目的名称。\n'
        '                            （默认的项目名称是"a"。）\n'
        '    -e 或 --English         使用英语。\n'
        '\n'
        '\n'
        'MFPP的语法:\n'
        '    与Python类似，但不相同。\n'
        '    “if”的用法:\n'
        '        if <条件>:\n'
        '            <若条件为真则执行的语句>\n'
        '\n'
        '        条件                    允许使用任何我的世界（版本1.13或以上）中命令\n'
        '                                /execute中允许使用的条件，例如\n'
        '                                “entity <其他参数>”等。\n'
        '        若条件为真则执行的语句  若条件为真则执行的语句。允许使用任意语句包括\n'
        '                                任何我的世界（版本1.13或以上）中的命令或\n'
        '                                “if”，“unless”等mfpp中的语句。\n'
        '\n'
        '        范例:\n'
        '            if entity @p[r=2]:\n'
        '                if entity @e[r=1]:\n'
        '                    setblock ~ ~ ~ minecraft:air\n'
        '                goto menu\n'
        '\n'
        '    “unless”的用法:\n'
        '        unless <条件>:\n'
        '            <除非条件为真则执行的语句>\n'
        '\n'
        '        条件                    允许使用任何我的世界（版本1.13或以上）中命令\n'
        '                                /execute中允许使用的条件，例如\n'
        '                                “entity <其他参数>”等。\n'
        '        除非条件为真则执行的语句\n'
        '                                除非条件为真则执行的语句。允许使用任意语句\n'
        '                                包括任何我的世界（版本1.13或以上）中的命令或\n'
        '                                “if”，“unless”等mfpp中的语句。\n'
        '\n'
        '        范例:\n'
        '            unless entity @s[type=minecraft:bat]:\n'
        '                fill ^ ^ ^ ^5 ^ ^ minecraft:stone\n'
        '                goto end\n'
        '\n'
        '    “while”的用法:\n'
        '        while <条件>:\n'
        '            <若条件为真则重复执行的语句>\n'
        '\n'
        '        条件                    允许使用任何我的世界（版本1.13或以上）中命令\n'
        '                                /execute中允许使用的条件，例如\n'
        '                                “entity <其他参数>”等。\n'
        '        若条件为真则重复执行的语句\n'
        '                                若条件为真则重复执行的语句。允许使用任意语句\n'
        '                                包括任何我的世界（版本1.13或以上）中的命令或\n'
        '                                “if”，“unless”等mfpp中的语句。\n'
        '\n'
        '        范例:\n'
        '            while entity @a[r=2]:\n'
        '                if entity @a[r=10,type=minecraft:bat]:\n'
        '                    summon minecraft:falling_block ~ ~10 ~\n'
        '\n'
        '    “goto”的用法:\n'
        '        goto <标签>\n'
        '\n'
        '        标签                    准备跳转到的位置标签。可以使用“:<标签名>”\n'
        '                                以自定义标签，但标签名不能含有空格。\n'
        '\n'
        '        范例:\n'
        '            goto _show_menu_EX\n',
    'cr':
        'MCFunctionPlusPlus 编译器 由 NKid 制作',
    'inc_tab':
        '不正确的制表符使用',
    'inc_if_con_:':
        '不正确的“if”使用: 缺少条件和/或“:”',
    'inc_if_con':
        '不正确的“if”使用: 缺少条件',
    'inc_if_:':
        '不正确的“if”使用: 缺少“:”',
    'inc_unless_con_:':
        '不正确的“unless”使用: 缺少条件和/或“:”',
    'inc_unless_con':
        '不正确的“unless”使用: 缺少条件',
    'inc_unless_:':
        '不正确的“unless”使用: 缺少“:”',
    'inc_while_con_:':
        '不正确的“while”使用: 缺少条件和/或“:”',
    'inc_while_con':
        '不正确的“while”使用: 缺少条件',
    'inc_while_:':
        '不正确的“while”使用: 缺少“:”',
}

w_t = {
    'help':
        '\n'
        '如果你想使用简体中文, 请不要用以下开关“-t”或“--Traditional-Chinese”。\n'
        'If you are looking for English,do not use option "-t" or\n'
        '"--Traditional-Chinese" and use option "-e" or "--English".\n'
        '\n'
        'MCFunctionPlusPlus 編譯器 由 NKid 製作\n'
        '\n'
        '使用方法:\n'
        '    mfppc [-h | --help] [<-o | --output> <輸出資料夾>]\n'
        '          [-p | --only-precompile] [-s | --silent]\n'
        '          [<-n | --project-name> <項目名稱>]\n'
        '          [<-t | --Traditional-Chinese> | <-e | --English>] <原始程式碼>\n'
        '\n'
        '    -h 或 --help            顯示此說明文檔。 \n'
        '    -o 或 --output          設置準備輸出到的資料夾。 \n'
        '    輸出資料夾              準備輸出到的資料夾。 \n'
        '                            （預設輸出到程式所在目錄。 ）\n'
        '    -p 或 --only-precompile 只進行預編譯。 \n'
        '    -s 或 --silent          不輸出編譯資訊。 （仍輸出錯誤資訊。 ）\n'
        '    -n 或 --project-name    設置項目的名稱\n'
        '    項目名稱               項目的名稱。\n'
        '                            （默認的項目名稱是"a"。 ）\n'
        '    -e 或 --English         使用英語。 \n'
        '\n'
        '\n'
        'MFPP的語法:\n'
        '    與Python類似，但不相同。 \n'
        '    “if”的用法:\n'
        '        if <條件>:\n'
        '            <若條件為真則執行的語句>\n'
        '\n'
        '        條件                    允許使用任何我的世界（版本1.13或以上）中命令\n'
        '                                /execute中允許使用的條件，例如\n'
        '                                “entity <其他參數>”等。 \n'
        '        若條件為真則執行的語句  若條件為真則執行的語句。 允許使用任意語句包括\n'
        '                                任何我的世界（版本1.13或以上）中的命令或\n'
        '                                “if”，“unless”等mfpp中的語句。 \n'
        '\n'
        '        範例:\n'
        '            if entity @p[r=2]:\n'
        '                if entity @e[r=1]:\n'
        '                    setblock ~ ~ ~ minecraft:air\n'
        '                goto menu\n'
        '\n'
        '    “unless”的用法:\n'
        '        unless <條件>:\n'
        '            <除非條件為真則執行的語句>\n'
        '\n'
        '        條件                    允許使用任何我的世界（版本1.13或以上）中命令\n'
        '                                /execute中允許使用的條件，例如\n'
        '                                “entity <其他參數>”等。 \n'
        '        除非條件為真則執行的語句\n'
        '                                除非條件為真則執行的語句。 允許使用任意語句\n'
        '                                包括任何我的世界（版本1.13或以上）中的命令或\n'
        '                                “if”，“unless”等mfpp中的語句。 \n'
        '\n'
        '        範例:\n'
        '            unless entity @s[type=minecraft:bat]:\n'
        '                fill ^ ^ ^ ^5 ^ ^ minecraft:stone\n'
        '                goto end\n'
        '\n'
        '    “while”的用法:\n'
        '        while <條件>:\n'
        '            <若條件為真則重複執行的語句>\n'
        '\n'
        '        條件                    允許使用任何我的世界（版本1.13或以上）中命令\n'
        '                                /execute中允許使用的條件，例如\n'
        '                                “entity <其他參數>”等。\n'
        '        若條件為真則重複執行的語句\n'
        '                                若條件為真則重複執行的語句。允許使用任意語句\n'
        '                                包括任何我的世界（版本1.13或以上）中的命令或\n'
        '                                “if”，“unless”等mfpp中的語句。\n'
        '\n'
        '        範例:\n'
        '            while entity @a[r=2]:\n'
        '                if entity @a[r=10,type=minecraft:bat]:\n'
        '                    summon minecraft:falling_block ~ ~10 ~\n'
        '\n'
        '    “goto”的用法:\n'
        '        goto <標籤>\n'
        '\n'
        '        標籤                    準備跳轉到的位置標籤。 可以使用“:<標籤名>”\n'
        '                                以自訂標籤，但標籤名不能含有空格。 \n'
        '\n'
        '        範例:\n'
        '            goto _show_menu_EX\n',
    'cr':
        'MCFunctionPlusPlus 編譯器 由 NKid 製作',
    'inc_tab':
        '不正確的定位字元使用',
    'inc_if_con_:':
        '不正確的“if”使用: 缺少條件和/或“:”',
    'inc_if_con':
        '不正確的“if”使用: 缺少條件',
    'inc_if_:':
        '不正確的“if”使用: 缺少“:”',
    'inc_unless_con_:':
        '不正確的“unless”使用: 缺少條件和/或“:”',
    'inc_unless_con':
        '不正確的“unless”使用: 缺少條件',
    'inc_unless_:':
        '不正確的“unless”使用: 缺少“:”',
    'inc_while_con_:':
        '不正確的“while”使用: 缺少條件和/或“:”',
    'inc_while_con':
        '不正確的“while”使用: 缺少條件',
    'inc_while_:':
        '不正確的“while”使用: 缺少“:”',
}

w_en = {
    'help':
        '\n'
        '如果你想使用简体中文, 请不要用以下开关 “-e” 或 “--English”。\n'
        '如果你想使用繁體中文, 請不要用以下開關 “-e” 或 “--English”，並啟用以下開關\n'
        '“-t” 或 “--Traditional-Chinese”。\n'
        '\n'
        'MCFunctionPlusPlus Compiler by NKid\n'
        '\n'
        'Usage:\n'
        '    mfppc [-h | --help] [<-o | --output> <output folder>]\n'
        '          [-p | --only-precompile] [-s | --silent]\n'
        '          [<-n | --project-name> <project name>]\n'
        '          [<-t | --Traditional-Chinese> | <-e | --English>] <source>\n'
        '\n'
        '    -h or --help             Show this document.\n'
        '    -o or --output           Change the folder that output into.\n'
        '    output folder            The folder that output into.\n'
        '                             (Default folder is ".".)\n'
        '    -p or --only-precompile  Only precompile\n'
        '    -s or --silent           Do not show compile information.\n'
        '                             (Still show error messages.)\n'
        '    -n or --project-name     Set project\'s name.\n'
        '    project name             The project\'s name.\n'
        '                             (Default project\'s name is "a".)\n'
        '    -e or --English          Use English.\n'
        '\n'
        '\n'
        'Grammar of MFPP:\n'
        '    Like Python, but not equal.\n'
        '    Usage of "if":\n'
        '        if <Condition>:\n'
        '            <Commands that run if the condition is true>\n'
        '\n'
        '        Condition       Condition that included in\n'
        '                        Minecraf(Version 1.13+)\'s command\n'
        '                        "/execute", like "entity <Something>" etc.\n'
        '        Commands that run if the condition is true\n'
        '                        Commands that run if the condition is true.\n'
        '                        You can use all commands that included in\n'
        '                        mfpp or in Minecraft(Version 1.13+).\n'
        '\n'
        '        Example:\n'
        '            if entity @p[r=2]:\n'
        '                if entity @e[r=1]:\n'
        '                    setblock ~ ~ ~ minecraft:air\n'
        '                goto menu\n'
        '\n'
        '    Usage of "unless":\n'
        '        unless <Condition>:\n'
        '            <Commands that run unless the condition is true>\n'
        '\n'
        '        Condition       Condition that included in\n'
        '                        Minecraf(Version 1.13+)\'s command\n'
        '                        "/execute", like "entity <Something>" etc.\n'
        '        Commands that run unless the condition is true\n'
        '                        Commands that run if the condition is true.\n'
        '                        You can use all commands that included in\n'
        '                        mfpp or in Minecraft(Version 1.13+).\n'
        '\n'
        '        Example:\n'
        '            unless entity @s[type=minecraft:bat]:\n'
        '                fill ^ ^ ^ ^5 ^ ^ minecraft:stone\n'
        '                goto end\n'
        '\n'
        '    Usage of "while":\n'
        '        while <Condition>:\n'
        '            <Commands that repeat if the condition is true>\n'
        '\n'
        '        Condition       Condition that included in\n'
        '                        Minecraf(Version 1.13+)\'s command\n'
        '                        "/execute", like "entity <Something>" etc.\n'
        '        Commands that repeat if the condition is true\n'
        '                        Commands that repeat if the condition is\n'
        '                        true. You can use all commands that included\n'
        '                        in mfpp or in Minecraft(Version 1.13+).\n'
        '\n'
        '        Example:\n'
        '            while entity @a[r=2]:\n'
        '                if entity @a[r=10,type=minecraft:bat]:\n'
        '                    summon minecraft:falling_block ~ ~10 ~\n'
        '\n'
        '    Usage of "goto":\n'
        '        goto <Label>\n'
        '\n'
        '        Label   The mark that marks where to go.You can use\n'
        '                ":<label name>" to make a label,but "label name"\n'
        '                must not include any space.\n'
        '\n'
        '        Example:\n'
        '            goto _show_menu_EX\n',
    'cr':
        'MCFunctionPlusPlus Compiler by NKid',
    'inc_tab':
        'Incorrect Tabs',
    'inc_if_con_:':
        'Incorrect usage of if: condition or/'
        'and \':\' is/are missing.',
    'inc_if_con':
        'Incorrect usage of if: condition is missing.',
    'inc_if_:':
        'Incorrect usage of if: \':\' is missing.',
    'inc_unless_con_:':
        'Incorrect usage of unless: condition or/'
        'and \':\' is/are missing.',
    'inc_unless_con':
        'Incorrect usage of unless: condition is missing.',
    'inc_unless_:':
        'Incorrect usage of unless: \':\' is missing.',
    'inc_while_con_:':
        'Incorrect usage of unless: condition or/'
        'and \':\' is/are missing.',
    'inc_while_con':
        'Incorrect usage of unless: condition is missing.',
    'inc_while_:':
        'Incorrect usage of unless: \':\' is missing.',
}
