#!/usr/bin/env python
#coding=utf-8

case = {
    "id": "BOLL",
    "cname": "布林通道线",
    "type": "MAIN",
    "src": """
//该模型仅仅用来示范如何根据指标编写简单的模型
//用户需要根据自己交易经验，进行修改后再实际应用!!!
// //后为文字说明，编写模型时不用写出
MID:MA(CLOSE,N);//求N个周期的收盘价均线，称为布林通道中轨
TMP2:=STD(CLOSE,M);//求M个周期内的收盘价的标准差
TOP:MID+P*TMP2;//布林通道上轨
BOTTOM:MID-P*TMP2;//布林通道下轨
BOTTOM2:MA(MID,N);
""",
    "params": [
        ("N", 5, 100000, 26),
        ("M", 1, 100000, 26),
        ("P", 1, 10, 2),
    ],
    "expected": """
function* CDP(C){
C.DEFINE({
type: "MAIN",
cname: "逆势操作",
state: "KLINE",
});
//定义指标参数
let N = C.PARAM(20.000000, "N", {"MIN": 1.000000, "MAX":100.000000});
//输入序列
let HIGH = C.SERIAL("HIGH");
let LOW = C.SERIAL("LOW");
let CLOSE = C.SERIAL("CLOSE");
//输出序列
let AH = C.OUTS("LINE", "AH", {color: RED});
let AL = C.OUTS("LINE", "AL", {color: RED});
let NH = C.OUTS("LINE", "NH", {color: RED});
let NL = C.OUTS("LINE", "NL", {color: RED});
//临时序列
let S_1 = [];
let S_2 = [];
let S_3 = [];
let PT = [];
let S_4 = [];
let S_5 = [];
let S_6 = [];
let S_7 = [];
let CDP = [];
let S_8 = [];
let S_9 = [];
let S_10 = [];
let S_11 = [];
let S_12 = [];
let S_13 = [];
let S_14 = [];
let S_15 = [];
let S_16 = [];
let S_17 = [];
//指标计算
while(true){
let i = yield;
S_1[i]=REF(i, HIGH,1, S_1);
S_2[i]=REF(i, LOW,1, S_2);
S_3[i]=((S_1[i] - S_2[i]));
PT[i] = S_3[i];
S_4[i]=((S_1[i] + S_2[i]));
S_5[i]=REF(i, CLOSE,1, S_5);
S_6[i]=((S_4[i] + S_5[i]));
S_7[i]=(((S_6)[i] / 3));
CDP[i] = S_7[i];
S_8[i]=((CDP[i] + PT[i]));
S_9[i]=MA(i, S_8,N, S_9);
AH[i] = S_9[i];
S_10[i]=((CDP[i] - PT[i]));
S_11[i]=MA(i, S_10,N, S_11);
AL[i] = S_11[i];
S_12[i]=((2 * CDP[i]));
S_13[i]=((S_12[i] - LOW[i]));
S_14[i]=MA(i, S_13,N, S_14);
NH[i] = S_14[i];
S_15[i]=((2 * CDP[i]));
S_16[i]=((S_15[i] - HIGH[i]));
S_17[i]=MA(i, S_16,N, S_17);
NL[i] = S_17[i];
}
}        
    """,
}