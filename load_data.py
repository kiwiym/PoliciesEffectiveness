import numpy as np

# Configuration of Provinces
provs = ["上海市", "北京市", "广东省", "重庆市", "湖北省", "山东省", "福建省",
         "河南省", "陕西省", "海南省", "吉林省", "辽宁省", "山西省", "贵州省",
         "云南省", "内蒙古自治区", "青海省", "宁夏回族自治区", "新疆维吾尔自治区"]

prov_19 = ["上海市", "云南省", "内蒙古自治区", "北京市", "吉林省", 
           "宁夏回族自治区", "山东省", "山西省", "广东省",  "新疆维吾尔自治区",
           "河南省", "海南省", "湖北省", "福建省", "贵州省", 
           "辽宁省", "重庆市", "陕西省", "青海省"]

prov_19_eng = ["Shanghai", "Yunnan", "Inner Mon.", "Beijing", "Jilin",
            "Ningxia", "Shandong", "Shanxi", "Guangdong", "Xinjiang",
            "Henan", "Hainan", "Hubei", "Fujian", "Guizhou",
            "Liaoning", "Chongqing", "Shaanxi", "Qinghai"]

group_1 = ["北京市", "上海市", "广东省"]
group_2 = ["河南省", "重庆市", "湖北省"]
group_3 = ["山东省", "辽宁省", "内蒙古自治区"]
group_4 = ["新疆维吾尔自治区", "宁夏回族自治区", "青海省"]

group_1_eng = ["Beijing", "Shanghai", "Guangdong"]
group_2_eng = ["Henan", "Chongqing", "Hubei"]
group_3_eng = ["Shandong", "Liaoning", "Inner Mongolia"]
group_4_eng = ["Xinjiang", "Ningxia", "Qinghai"]

# Configurations for 13^th Five-Year Plan Data
# Measure Value Calculated by AHP
alphas_16 = np.array([7.853, 34.878, 2.885, 19.504, 34.878]) / 100
alphas_21 = np.array([19.613, 57.238, 4.777, 4.777, 13.595]) / 100

# Average Passenger & Freight Turnover
betas_16 = np.array([[0.275417111,0.494093158,0.23048999],
                    [0.316851693,0,0.683154364],
                    [0.363608415,0.419229411,0.217159525],
                    [0.490140205,0.321060343,0.188809328],
                    [0.409354119,0.227629597,0.363020341],
                    [0.540360497,0.094384128,0.365255375],
                    [0.302504299,0.401466101,0.296038028],
                    [0.553442763,0.054924791,0.391632447],
                    [0.471929408,0.000583632,0.527488411],
                    [0.348936377,0.472789761,0.178273862],
                    [0.562451514,0.000453136,0.437083756],
                    [0.285038294,0.344805358,0.370156348],
                    [0.399352024,0.000149892,0.600484217],
                    [0.622846671,0.018559723,0.358601014],
                    [0.725250143,0.007776291,0.266965482],
                    [0.482792258,0,0.517207742],
                    [0.437878344,0.000319719,0.561801937],
                    [0.645761941,0.000455705,0.353782353],
                    [0.538526224,0,0.461460088]])

betas_21 = np.array([[0.199699586, 0.48713709, 0.313200311],
                    [0.308219905, 0, 0.691780095],
                    [0.194501429, 0.44276744, 0.36273113],
                    [0.364334022, 0.321944634, 0.313721345],
                    [0.266440145, 0.257070826, 0.476489771],
                    [0.437739389, 0.119008972, 0.443251639],
                    [0.179365964, 0.430703355, 0.389946607],
                    [0.478168464, 0.059410283, 0.462420784],
                    [0.347564514, 0.000200013, 0.652235473],
                    [0.238428567, 0.512206887, 0.249419568],
                    [0.54295859, 0.0002156, 0.456823393],
                    [0.411882696, 0.063973069, 0.524144234],
                    [0.376436614, 0, 0.623492508],
                    [0.440508589, 0.009348053, 0.550152066],
                    [0.612232755, 0.003231257, 0.384535988],
                    [0.328575339, 0, 0.671394325],
                    [0.298665667, 0.0003529, 0.700989885],
                    [0.59535208, 0.000715308, 0.403926456],
                    [0.323942613, 0, 0.676057387]])

# We only consider Road and Waterway
betas_16 = betas_16[:, :2] / betas_16[:, :2].sum(axis=1).reshape(-1, 1)
betas_21 = betas_21[:, :2] / betas_21[:, :2].sum(axis=1).reshape(-1, 1)

# Carbon Emission Intensity
intensity_16 = [0.038174381, 0.029632766, 0.023508111, 0.025921685, 0.022969269,
                0.015748219, 0.018325156, 0.011787592, 0.014942417, 0.030022764,
                0.028554949, 0.031766121, 0.025379514, 0.032016989, 0.028937482,
                0.016378903, 0.032305549, 0.019740216, 0.042370752]

intensity_19 = [0.032129632, 0.027268678, 0.019340249, 0.019831851, 0.018745036,
                0.012845415, 0.017654881, 0.010250875, 0.012848442, 0.023175307,
                0.019387009, 0.029294905, 0.017687404, 0.022824628, 0.024298174,
                0.01363358, 0.036722746, 0.019387009, 0.027655955]

# Carbon Emission Decrease Rate 2016 ~ 2019
int_dec_rate = [0.158346, 0.160322, 0.167613, 0.079780, 0.267630,
                0.017893, 0.184326, 0.303083, 0.177295, 0.347287,
                0.130367, 0.228076, 0.183908, 0.036577, 0.287109,
                0.077794, 0.234932, 0.140136, -0.136732]

# Extracted Policy Context
# Pathway Classes
p_prov_16 = [
    [3,2,1,4,2,4,2,4,3],
    [3,4,2,2,1,2,3,2,4],
    [5,1,2,4,4,5],
    [1,4,5,1,3,5,4,5,5],
    [1,2,5,4,4],
    [5,4,2,4],
    [2,2,5,2],
    [2,4,1,5,2,1,2,4],
    [5,5,5,5,4,2,2],
    [5,5,4,2,2,2,5,4,5],
    [4,5,4,5,4,5],
    [2,2,5,1],
    [2,1,4],
    [1,5,4,2,5],
    [4,4,5,5,2,1,4],
    [1,2,3,4,5],
    [2,4,5,5,5],
    [1,2,3],
    [5,1,5,4,1,2]
]

p_prov_21 = [
    [3,2,2,2,2,1,2,2,2,2,4,4,5],
    [3,4,1,2,1,2,1,2,3,3,1,2,5,5],
    [3,4,1,4,1,1,2,2,2,5],
    [2,1,1,2,2,2,4,5],
    [2,1,1,5,1,5,2,2],
    [2,1,2,3,4,5,5,1,4,2,5,5,5],
    [1,1,3,2,2,1,5,5,3,1,2,4],
    [3,1,4],
    [1,2,2,2,2,5,1,2],
    [2,3,2,2,2,4,5],
    [2,2,3,5,1,2,5,5,4,1],
    [2,2,3,2,5,2,3],
    [2,2,5,1,3,2,5],
    [2,1,2,2,3,2,5],
    [2,2,2,1,1,3],
    [2,1,2,1,2,4,3],
    [5,5,5,5,4,1,1,5,4,4],
    [3,2,5,3,4,1,2],
    [1,2,4,4,5,4,2,3]
]

# Model of Transport
m_prov_16 = [
    [1,1,1,1,2,1,1,1,1],
    [1,1,1,1,1,1,1,1,1],
    [1,2,1,1,2,1],
    [1,1,2,3,1,2,2,2,1],
    [2,2,1,1,2],
    [1,1,2,1],
    [2,1,2,2],
    [1,1,1,1,1,2,1,1],
    [1,1,1,1,1,1,1],
    [1,1,2,1,1,2,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,2],
    [1,1,1],
    [1,1,1,1,1],
    [1,2,1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1],
    [1,1,1,1,1,1]
]

m_prov_21 = [
    [1,1,1,1,1,1,1,2,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,2,1,2,2,1],
    [1,1,2,1,2,1,1,1],
    [1,2,3,1,1,1,1,2],
    [1,1,1,1,1,1,1,1,1,2,2,1,2],
    [1,2,1,2,1,1,1,2,1,1,1,2],
    [1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,2,2,1,1],
    [1,1,1,1,1,1,2,1,1,1],
    [1,1,1,1,2,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,2,1,1,1],
    [1,2,1,1,2,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1]
]

# Policy Grading (3, 2, 1) -> (2^3, 2^1, 2^0) 
s_prov_16 = [
    [8,8,8,8,2,2,1,2,1],
    [8,8,8,2,2,2,1,1,2],
    [1,2,1,8,8,1],
    [8,8,8,8,1,1,2,1,1],
    [8,8,1,2,2],
    [1,1,1,2],
    [1,1,1,2],
    [8,8,2,2,1,2,1,1],
    [8,2,1,1,2,2,2],
    [8,8,2,2,1,1,1,1,1],
    [8,8,1,1,2,1],
    [2,2,2,2],
    [1,1,1],
    [1,1,2,1,1],
    [8,8,8,1,2,1,1],
    [2,1,1,2,1],
    [8,8,8,1,1],
    [2,2,1],
    [8,2,1,2,2,2]
]

s_prov_21 = [
    [3,3,3,3,3,2,1,1,1,1,2,2,1],
    [3,3,3,3,3,3,1,1,1,2,2,1,1,1],
    [3,3,1,1,2,2,2,2,2,1],
    [3,3,3,3,3,1,2,1],
    [3,2,2,1,1,1,1,1],
    [3,3,3,1,1,1,1,2,1,2,2,1,1],
    [3,3,3,3,1,1,2,2,1,2,1,2],
    [1,1,2],
    [3,3,3,2,2,2,2,1],
    [3,1,2,2,2,1],
    [3,1,1,1,2,2,2,2,2,2],
    [3,3,3,3,2,2,1],
    [3,1,1,2,1,2,1],
    [3,3,2,2,1,2,1],
    [3,3,2,2,2,1],
    [3,2,1,1,2,2,1],
    [3,3,1,1,2,2,1,1,2,1],
    [3,1,1,1,2,2,2],
    [1,2,2,2,1,2,1,1]
]