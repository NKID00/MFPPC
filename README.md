#Minecraft Function Plus Plus Compiler by NKid
#
##项目MFPPC - 简体中文
###作者: NKid
###描述: “MFppc's Pretty Prefect, Clever!”的缩写，开玩笑的。其实是“Minecraft Function Plus Plus Compiler”的缩写。它能将用mfpp语言写的源代码编译成一大堆我的世界能执行的mcfunction文件。
##項目MFPPC - 繁體中文
###作者: NKid
###描述: “MFppc's Pretty Prefect, Clever!”的縮寫，開玩笑的。其實是“Minecraft Function Plus Plus Compiler”的縮寫。它能將用mfpp語言寫的原始程式碼編譯成一大堆麥塊能執行的mcfunction檔。
##Project MFPPC - English
###Author: NKid
###Description: The abbreviation of "MFppc's Pretty Prefect, Clever!", just kidding. It's the abbreviation of "Minecraft Function Plus Plus Compiler".
#Minecraft Function Plus Plus
##MFPP - 简体中文
###MFPP是一种python风格的编程语言。
###语法:
    “if”的用法:
        if <条件>:
            <若条件为真则执行的语句>

        条件                     允许使用任何我的世界（版本1.13或以上）中命令
                                /execute中允许使用的条件，例如
                                “entity <其他参数>”等。
        若条件为真则执行的语句      若条件为真则执行的语句。允许使用任意语句包括
                                任何我的世界（版本1.13或以上）中的命令或
                                “if”，“unless”等mfpp中的语句。

        范例:
            if entity @p[r=2]:
                if entity @e[r=1]:
                    setblock ~ ~ ~ minecraft:air
                goto menu

    “unless”的用法:
        unless <条件>:
            <除非条件为真则执行的语句>

        条件                    允许使用任何我的世界（版本1.13或以上）中命令
                                /execute中允许使用的条件，例如
                                “entity <其他参数>”等。
        除非条件为真则执行的语句    除非条件为真则执行的语句。允许使用任意语句
                                包括任何我的世界（版本1.13或以上）中的命令或
                                “if”，“unless”等mfpp中的语句。

        范例:
            unless entity @s[type=minecraft:bat]:
                fill ^ ^ ^ ^5 ^ ^ minecraft:stone
                goto end

    “while”的用法:
        while <条件>:
            <若条件为真则重复执行的语句>

        条件                     允许使用任何我的世界（版本1.13或以上）中命令
                                /execute中允许使用的条件，例如
                                “entity <其他参数>”等。
        若条件为真则重复执行的语句   若条件为真则重复执行的语句。允许使用任意语句
                                包括任何我的世界（版本1.13或以上）中的命令或
                                “if”，“unless”等mfpp中的语句。

        范例:
            while entity @a[r=2]:
                if entity @a[r=10,type=minecraft:bat]:
                    summon minecraft:falling_block ~ ~10 ~

    “goto”的用法:
        goto <标签>

        标签                     准备跳转到的位置标签。可以使用“:<标签名>”
                                以自定义标签，但标签名不能含有空格。

        范例:
            goto _show_menu_EX


##項目MFPPC - 繁體中文
###MFPP是一種python風格的程式設計語言。
###語法:
    “if”的用法:
        if <條件>:
            <若條件為真則執行的語句>

        條件                     允許使用任何麥塊（版本1.13或以上）中命令
                                /execute中允許使用的條件，例如
                                “entity <其他參數>”等。
        若條件為真則執行的語句      若條件為真則執行的語句。 允許使用任意語句包括
                                任何我的世界（版本1.13或以上）中的命令或
                                “if”，“unless”等mfpp中的語句。

        範例:
            if entity @p[r=2]:
                if entity @e[r=1]:
                    setblock ~ ~ ~ minecraft:air
                goto menu

    “unless”的用法:
        unless <條件>:
            <除非條件為真則執行的語句>

        條件                    允許使用任何麥塊（版本1.13或以上）中命令
                                /execute中允許使用的條件，例如
                                “entity <其他參數>”等。
        除非條件為真則執行的語句    除非條件為真則執行的語句。 允許使用任意語句
                                包括任何麥塊（版本1.13或以上）中的命令或
                                “if”，“unless”等mfpp中的語句。

        範例:
            unless entity @s[type=minecraft:bat]:
                fill ^ ^ ^ ^5 ^ ^ minecraft:stone
                goto end

    “while”的用法:
        while <條件>:
            <若條件為真則重複執行的語句>

        條件                    允許使用任何麥塊（版本1.13或以上）中命令
                                /execute中允許使用的條件，例如
                                “entity <其他參數>”等。
        若條件為真則重複執行的語句   若條件為真則重複執行的語句。允許使用任意語句
                                包括任何麥塊（版本1.13或以上）中的命令或
                                “if”，“unless”等mfpp中的語句。

        範例:
            while entity @a[r=2]:
                if entity @a[r=10,type=minecraft:bat]:
                    summon minecraft:falling_block ~ ~10 ~

    “goto”的用法:
        goto <標籤>

        標籤                     準備跳轉到的位置標籤。 可以使用“:<標籤名>”
                                以自訂標籤，但標籤名不能含有空格。

        範例:
            goto _show_menu_EX


##Project MFPPC - English
###MFPP is a Python-like program language.
###Grammar:
    Usage of "if":
        if <Condition>:
            <Commands that run if the condition is true>

        Condition       Condition that included in
                        Minecraf(Version 1.13+)'s command
                        "/execute", like "entity <Something>" etc.
        Commands that run if the condition is true
                        Commands that run if the condition is true.
                        You can use all commands that included in
                        mfpp or in Minecraft(Version 1.13+).

        Example:
            if entity @p[r=2]:
                if entity @e[r=1]:
                    setblock ~ ~ ~ minecraft:air
                goto menu

    Usage of "unless":
        unless <Condition>:
            <Commands that run unless the condition is true>

        Condition       Condition that included in
                        Minecraf(Version 1.13+)'s command
                        "/execute", like "entity <Something>" etc.
        Commands that run unless the condition is true
                        Commands that run if the condition is true.
                        You can use all commands that included in
                        mfpp or in Minecraft(Version 1.13+).

        Example:
            unless entity @s[type=minecraft:bat]:
                fill ^ ^ ^ ^5 ^ ^ minecraft:stone
                goto end

    Usage of "while":
        while <Condition>:
            <Commands that repeat if the condition is true>

        Condition       Condition that included in
                        Minecraf(Version 1.13+)'s command
                        "/execute", like "entity <Something>" etc.
        Commands that repeat if the condition is true
                        Commands that repeat if the condition is
                        true. You can use all commands that included
                        in mfpp or in Minecraft(Version 1.13+).

        Example:
            while entity @a[r=2]:
                if entity @a[r=10,type=minecraft:bat]:
                    summon minecraft:falling_block ~ ~10 ~

    Usage of "goto":
        goto <Label>

        Label   The mark that marks where to go.You can use
                ":<label name>" to make a label,but "label name"
                must not include any space.

        Example:
            goto _show_menu_EX