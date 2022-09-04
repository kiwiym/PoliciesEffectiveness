# Policy Effectiveness Evaluation using Linear Regression



### Summary

---

This is a code repositry for Yimeng Gao's dissertation, *Analyse of effectiveness of decarbonisation policies in China’s transport sector in the $13^{th}$ Five-Year Plan and $14^{th}$ Five-Year Plan periods*, of MSc Environmental Technology, Central for Environmental Policy, Imperial College London.

* **Author:** Yimeng Gao

* **Supervisor:** [Dr. Iain Staffell](https://www.imperial.ac.uk/people/i.staffell)



### Abstract

---

Climate change is a significant and urgent global challenge. In order to prevent a global temperature increase of more than 2 °C, countries around the world have proposed a reduction in carbon emissions and introduced a series of initiatives to limit the temperature increase to 1.5 °C. China is the largest contributor to global energy consumption and carbon emissions. As the world's largest developing country and second largest economy, China has taken on the responsibility of decarbonisation and China proposed the "Double Carbon" goal in 2020, aiming to peak $\text{CO}_2$ emissions by 2030 and achieve carbon neutrality by 2060. In China the transport sector accounts for 10.7\% of the country’s final energy consumption; in order to meet the "Double Carbon" goal, transition to a low-carbon economy in the transportation sector is urgently needed. Meanwhile, the year 2020 is the boundary between the $13^{th}$ and the $14^{th}$ Five-Year Plan for National Economic and Social Development ($13^{th}$ and $14^{th}$ Five-Year Plan) of China. The majority of recent studies, however, only compared the $13^{th}$ and $14^{th}$ Five-Year Plans as a whole, with very few analysing and comparing the transport sector in the $13^{th}$ and $14^{th}$ Five-Year Plans. To fill the gap, this paper analyses the effectiveness of transport sector policies in 19 Chinese provinces during the $13^{th}$ and $14^{th}$ Five-Year Periods using a linear regression model and two distinct policy value assessment methods. Based on the result, national and provincial comparisons are made between the $13^{th}$ and $14^{th}$ Five-Year Plans, and policy recommendations are put forward for decarbonising the transport sector in China and each province in terms of economic factors, geographical factors, and carbon intensity.



### Prerequisites

---

```
pip install -r requirements.txt
```



### Execution

---

For model I, please run the following code:

```
python model_1.py
```

For model II, please run the following code:

```
python model_2.py
```



### Results

---

* Prediction of model I on $13^{th}$ Five-Year Plan of 19 Provinces

![](Figs/M1-135.png)

* Prediction of model II on $13^{th}$ Five-Year Plan of 19 Provinces
  
  ![](Figs/M2-135.png)

* Prediction of model I on $14^{th}$ Five-Year Plan of 19 Provinces
  
  ![](Figs/M1-145.png)

* Prediction of model II on $14^{th}$ Five-Year Plan of 19 Provinces
  
  ![](Figs/M2-145.png)