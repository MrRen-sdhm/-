#!/bin/bash
# 替换文件夹中所有文件中的字符串
# sed -i "s/oldString/newString/g"  `grep oldString -rl /path`

suffix="retrain"
path='./test'
sed -i "s/conv11_mbox_conf_new/conv11_mbox_conf_$suffix/g"  `grep conv11_mbox_conf_new -rl $path`
sed -i "s/conv13_mbox_conf_new/conv13_mbox_conf_$suffix/g"  `grep conv13_mbox_conf_new -rl $path`
sed -i "s/conv14_2_mbox_conf_new/conv14_2_mbox_conf_$suffix/g"  `grep conv14_2_mbox_conf_new -rl $path`
sed -i "s/conv15_2_mbox_conf_new/conv15_2_mbox_conf_$suffix/g"  `grep conv15_2_mbox_conf_new -rl $path`
sed -i "s/conv16_2_mbox_conf_new/conv16_2_mbox_conf_$suffix/g"  `grep conv16_2_mbox_conf_new -rl $path`
sed -i "s/conv17_2_mbox_conf_new/conv17_2_mbox_conf_$suffix/g"  `grep conv17_2_mbox_conf_new -rl $path`
