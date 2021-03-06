FORMATED_SALARY = {
    0: '面议',
    1: '1k-3k',
    2: '3k-5k',
    3: '5k-8k',
    4: '8k-10k',
    5: '10k-12k',
    6: '12k-15k',
    7: '15k-20k',
    8: '20k-30k',
    9: '30k+'
}

SALARY = {
    "面议": 0,
    "1k-3k": 1,
    "3k-5k": 2,
    "5k-8k": 3,
    "8k-10k": 4,
    "10k-12k": 5,
    "12k-15k": 6,
    "15k-20k": 7,
    "20k-30k": 8,
    "30k+": 9
}

WELFARE ={
    '五险': 1,  # 81771
    '带薪年假': 2,  # 52742
    '节日福利': 3,  # 49626
    '绩效奖金': 4,  # 40350
    '住房公积金': 5,  # 38522
    '全勤奖': 6,  # 29369
    '员工旅游': 7,  # 27132
    '年终双薪': 8,  # 25987
    '专业培训': 9,  # 24629
    '餐饮补贴': 10,  # 20374
    '商业保险': 11,  # 19718
    '加班补贴': 12,  # 18803
    '出差补贴': 13,  # 18664
    '定期体检': 14,  # 16639
    '每年多次调薪': 15,  # 14616
    '高温补贴': 16,  # 14112
    '交通补贴': 17,  # 13840
    '包吃': 18,  # 13241
    '工作制服': 19,  # 12838
    '通讯补贴': 20,  # 12596
    '包住': 21,  # 11199
    '年终分红': 22,  # 10018
    '弹性工作': 23,  # 8071
    '住房补贴': 24,  # 7611
    '出国机会': 25,  # 7225
    '免费班车': 26,  # 7010
    '不加班': 27,  # 5069
    '股票期权': 28,  # 2248
    '三险': 29,  # 2090
    '探亲假': 30,  # 1157
    '无试用期': 31,  # 796
    '免息房贷': 32,  # 537
    '采暖补贴': 33,  # 346
}

SCHEDULE = {
    '正常白班': 1,  # 40742
    '8.0小时/天': 2,  # 38882
    '5天/周': 3,  # 36721
    '7.5小时/天': 4,  # 16831
    '6天/周': 5,  # 16574
    '5.5天/周': 6,  # 9093
    '7.0小时/天': 7,  # 7960
    '2班倒': 8,  # 2592
    '大小周': 9,  # 1738
    '不定时工作制': 10,  # 789
    '6.5小时/天': 11,  # 691
    '10.0小时/天': 12,  # 628
    '12.0小时/天': 13,  # 591
    '9.0小时/天': 14,  # 552
    '8.5小时/天': 15,  # 364
    '3班倒': 16,  # 343
    '6.5天/周': 17,  # 333
    '11.0小时/天': 18,  # 271
    # '0.0小时/天': 19,  # 266
    '10.5小时/天': 20,  # 262
    '7天/周': 21,  # 247
    '6.0小时/天': 22,  # 244
    '正常晚班': 23,  # 115
    '7.3小时/天': 24,  # 96
    '5.5小时/天': 25,  # 83
    '5.0小时/天': 26,  # 65
    '9.5小时/天': 27,  # 52
    '正常夜班': 28,  # 44
    '7.2小时/天': 29,  # 35
    '4天/周': 30,  # 35
    '2天/周': 31,  # 31
    '7.6小时/天': 32,  # 28
    '4.5天/周': 33,  # 28
    '1天/周': 34,  # 26
    '7.8小时/天': 35,  # 24
    '11.5小时/天': 36,  # 24
    '3天/周': 37,  # 21
    '4.0小时/天': 38,  # 21
    '4班倒': 39,  # 20
    # '40.0小时/天': 40,  # 18
    '6.7小时/天': 41,  # 15
    '2.0小时/天': 42,  # 13
    '4.5小时/天': 43,  # 11
    '0.8小时/天': 44,  # 11
    '3.5天/周': 45,  # 10
    '2.5天/周': 46,  # 8
    '3.0小时/天': 47,  # 7
    '6.8小时/天': 48,  # 7
    '1.0小时/天': 49,  # 6
    '7.7小时/天': 50,  # 5
    '1.5天/周': 51,  # 5
    '24.0小时/天': 52,  # 5
    '7.4小时/天': 53,  # 4
    # '75.0小时/天': 54,  # 4
    '37.5小时/天': 55,  # 3
    '14.0小时/天': 56,  # 2
    '26.0小时/天': 57,  # 2
    '7.1小时/天': 58,  # 2
    # '80.0小时/天': 59,  # 2
    # '88.0小时/天': 60,  # 1
    '8.3小时/天': 61,  # 1
    '8.1小时/天': 62,  # 1
    '10.3小时/天': 63,  # 1
    '7.9小时/天': 64,  # 1
    '36.0小时/天': 65,  # 1
    '8.8小时/天': 66,  # 1
    '12.5小时/天': 67,  # 1
    # '70.0小时/天': 68,  # 1
    # '44.0小时/天': 69,  # 1
    # '38.0小时/天': 70,  # 1
    '1.5小时/天': 71,  # 1
    '16.0小时/天': 72,  # 1
    # '735.0小时/天': 73,  # 1
    # '45.0小时/天': 74,  # 1
    '3.5小时/天': 75,  # 1
    # '30.0小时/天': 76,  # 1
    '2.5小时/天': 77,  # 1
    '6.6小时/天': 78,  # 1
    '5.2小时/天': 79,  # 1
}
WORK_NATURE = {
    '全职': 1,
    '实习': 2,
    '兼职': 3,
    '临时': 4
}
EXPERIENCE = {
    '不限': 0,  # 53358
    '一年工作经验以上': 1,  # 13561
    '二年工作经验以上': 2,  # 11657
    '三年工作经验以上': 3,  # 11555
    '四年工作经验以上': 4,  # 733
    '五年工作经验以上': 5,  # 5101
    '六年工作经验以上': 6,  # 343
    '七年工作经验以上': 7,  # 95
    '八年工作经验以上': 8,  # 697
    '九年工作经验以上': 9,  # 11
    '十年工作经验以上': 10,  # 511
    '十二年工作经验以上': 12,  # 4
    '十五年工作经验以上': 15,  # 27
    '有工作经验者优先': 16,  # 2
    '应届生': 17,  # 1910

}
EDUCATION = {
    '不限': 0,  # 23699
    '小学以上': 1,  # 573
    '初中以上': 2,  # 4238
    '高中以上': 3,  # 6407
    '中专以上': 4,  # 9189
    '本科以上': 5,  # 17781
    '大专以上': 6,  # 38583
    '硕士研究生以上': 7,  # 506
    '博士研究生以上': 8,  # 52
}

COMPANY_NATURE = {
    '民营': 1,  # 7738
    '私营公司': 2,  # 7738
    '私营股份制': 3,  # 1518
    '其他': 4,  # 507
    '台资': 5,  # 484
    '港资': 6,  # 484
    '国营企业': 7,  # 419
    '上市公司': 8,  # 324
    '合资（非欧美）': 9,  # 236
    '外资（非欧美如日资）': 10,  # 174
    '外资（欧美）': 11,  # 172
    '外企代表处': 12,  # 105
    '合资（欧美）': 13,  # 66
    '事业单位': 14,  # 40
}

INDUSTRY = {
    '贸易/进出口': 1,  # 1799
    '互联网/电子商务': 2,  # 1762
    '建筑与工程': 3,  # 1473
    '其他行业': 4,  # 1304
    '机械/设备/重工': 5,  # 1233
    '计算机软件': 6,  # 1095
    '批发/零售': 7,  # 1069
    '电子技术/半导体/集成电路': 8,  # 883
    '计算机服务（系统/数据服务）': 9,  # 747
    '教育/培训': 10,  # 566
    '原材料和加工': 11,  # 554
    '服装/纺织/皮革': 12,  # 550
    '快速消费品(食品，饮料，化妆品)': 13,  # 548
    '仪器仪表/工业自动化': 14,  # 533
    '家居/室内设计/装潢': 15,  # 503
    '汽车及零配件': 16,  # 467
    '家具/家电/工艺品/玩具': 17,  # 458
    '交通/运输/物流 航天/航空': 18,  # 416
    '专业服务（咨询，人力资源）': 19,  # 396
    '环保': 20,  # 393
    '房地产开发': 21,  # 392
    '金融/投资/证券': 22,  # 383
    '通信/电信/网络设备': 23,  # 367
    '多元化业务集团公司': 24,  # 310
    '计算机硬件': 25,  # 304
    '医疗/护理/保健/卫生': 26,  # 302
    '物业管理/商业中心': 27,  # 293
    '医疗设备/器械': 28,  # 284
    '印刷/包装': 29,  # 261
    '影视/媒体/艺术': 30,  # 258
    '广告': 31,  # 237
    '制药/生物工程': 32,  # 217
    '生活服务': 33,  # 207
    '石油/化工/矿产': 34,  # 205
    '酒店/旅游': 35,  # 198
    '会计/审计': 36,  # 196
    '电力/水利': 37,  # 193
    '中介服务': 38,  # 193
    '餐饮业': 39,  # 191
    '公关/市场推广/会展': 40,  # 180
    '娱乐/休闲/体育': 41,  # 165
    '网络游戏': 42,  # 146
    '通信/电信运营/增值服务': 43,  # 137
    '学术/科研': 44,  # 129
    '美容/保健': 45,  # 121
    '农业/渔业/林业': 46,  # 120
    '检测，认证': 47,  # 119
    '法律': 48,  # 90
    '计算机服务（系统': 49,  # 74
    '数据服务）': 50,  # 74
    '保险': 51,  # 64
    '银行': 52,  # 58
    '办公用品及设备': 53,  # 57
    '文字媒体/出版': 54,  # 53
    '非盈利机构': 55,  # 28
    '通信/电信运营': 56,  # 15
    '增值服务': 57,  # 15
    '采掘业/冶炼': 58,  # 15
    '政府': 59,  # 14
    '快速消费品（食品，饮料，化妆品）': 60,  # 7
    '贸易/消费/制造/营运': 61,  # 6
    '计算机/互联网/通信/电子': 62,  # 5
    '物流/运输': 63,  # 3
    '会计/金融/银行/保险': 64,  # 2
}
SCALE = {
    '1-10人': 1,  # 35
    '11-50人': 2,  # 515
    '51-100人': 3,  # 439
    '101-200人': 4,  # 381
    '201-300人': 5,  # 179
    '300-500人': 6,  # 177
    '501-1000人': 7,  # 192
    '1001-2000人': 8,  # 108
    '2001-3000人': 9,  # 29
    '3001-5000人': 10,  # 43
    '5001-10000人': 11,  # 41
    '10000人以上': 12,  # 44
}

JOB_KEYS = {
    "_id": 0,
    "id": 1,
    "name": 1,
    "time": 1,
    "contact": 1,
    "tel": 1,
    "address": 1,
    "company": 1,
    "age": 1,
    "location": 1,
    # "schedule": 1,
    # "welfare": 1,
    "response_and_require": 1,
    "company_id": 1,
    "salary_id": 1,
    "nature_id": 1,
    "education_id": 1,
    "experience_id": 1
}

COMPANY_KEYS = {
    "_id": 0,
    "id": 1,
    "name": 1,
    "info": 1,
    "contact": 1,
    "tel": 1,
    "address": 1,
    "email": 1,
    "scale_id": 1,
    # "logo": 1,
    "nature_id": 1,
    "industry_id": 1
}
DROP_TABLE = "DROP TABLE IF EXISTS {};"

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS {} (
    {}_id INT(2) PRIMARY KEY,
    content CHAR(30) NOT NULL 
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
INSERT_TABLE = """
INSERT INTO {} ({}_id, content) VALUES (%s, %s)
"""
"""
welfare CHAR(255) COMMENT '薪资福利',
schedule CHAR(255) COMMENT '上班时间',
"""
CREATE_TABLES = """
DROP TABLE IF EXISTS job;
CREATE TABLE IF NOT EXISTS job(
    id INT(8) PRIMARY KEY COMMENT '求职信息_id',
    name CHAR (255) COMMENT '职位名称',
    date_lower CHAR(16) COMMENT '招聘期限开始',
    date_upper CHAR(16) COMMENT '招聘期限截止',
    contact CHAR(64) COMMENT '联系人',
    tel CHAR(64) COMMENT '联系电话',
    address CHAR(255) COMMENT '通信地址',
    company CHAR(64) COMMENT '招聘单位',
    age_lower INT(3) COMMENT '年龄要求下限',
    age_upper INT(3) COMMENT '年龄要求上限',
    location CHAR(255) COMMENT '工作地点',
    response_and_require  VARCHAR(4096) COMMENT '职位职责和职位要求',
    company_id INT(8) NOT NULL COMMENT '招聘单位_id',
    salary_id INT(8) COMMENT '参考月薪_id',
    nature_id INT(8) COMMENT '职位性质_id',
    education_id INT(8) COMMENT '职位性质_id',
    experience_id INT(8) COMMENT '工作经验_id'
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
DROP TABLE IF EXISTS company;
CREATE TABLE IF NOT EXISTS company(
    id INT(8) PRIMARY KEY COMMENT '公司_id',
    name CHAR(64) NOT NULL COMMENT '公司名',
    info VARCHAR(4096) COMMENT '公司简介',
    contact CHAR(32) COMMENT '联系人',
    tel CHAR(32) COMMENT '联系电话',
    address CHAR(255) COMMENT '联系地址',
    email CHAR(64) COMMENT '电子邮件',
    scale_id INT(8) COMMENT '公司规模_id',
    nature_id INT(8) COMMENT '公司性质_id',
    industry_id INT(8) COMMENT '公司行业_id'
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

MERGE_TABLE = """
DROP TABLE IF EXISTS job_welfare;
CREATE TABLE IF NOT EXISTS job_welfare(
    id INT(8) AUTO_INCREMENT PRIMARY KEY COMMENT '关联表id',
    job_id INT(8) NOT NULL COMMENT '求职信息_id',
    welfare_id INT(8) NOT NULL COMMENT '薪资待遇_id'
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
DROP TABLE IF EXISTS job_schedule;
CREATE TABLE IF NOT EXISTS job_schedule(
    id INT(8) AUTO_INCREMENT PRIMARY KEY COMMENT '关联表id',
    job_id INT(8) NOT NULL COMMENT '求职信息_id',
    schedule_id INT(8) NOT NULL COMMENT '上班时间_id'
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""