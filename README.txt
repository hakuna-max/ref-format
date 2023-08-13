# Formatting Reference Information

该程序将zotero上导出的ris文件，如：

```
TY  - JOUR
TI  - Assessing energy vulnerability and its impact on carbon emissions: A global case
AU  - Liu, Yang
AU  - Dong, Kangyin
AU  - Jiang, Qingzhe
T2  - Energy Economics
AB  - Reducing the vulnerability of the energy system can help safeguard the normal functioning of the economy and society and promote the transition to a green, low-carbon system, which in turn has a potential impact on the global greenhouse effect. To explore the causal relationship between energy vulnerability and CO2 emissions, this study first constructs a composite energy vulnerability index (EVI) for empirical analysis based on a balanced panel dataset of 119 countries from 2000 to 2019. The study then examines the potential heterogeneity. Further, to investigate the impact mechanism, this study decomposes the total effect into scale effect, structural effect, and technology effect for detailed discussion. The main findings are: (1) decreased energy vulnerability can help curb CO2 emissions, leading to a “win-win” situation; (2) significant heterogeneity exists in the relationship between EVI and CO2 emissions; (3) decreased energy vulnerability can not only reduce CO2 emissions directly, but also indirectly by lowering the total primary energy supply, promoting renewable energy use, and enhancing energy efficiency. In light of these findings, we offer specific recommendations for reducing energy vulnerability and limiting the greenhouse effect.
DA  - 2023/03/01/
PY  - 2023
DO  - 10.1016/j.eneco.2023.106557
DP  - ScienceDirect
VL  - 119
SP  - 106557
J2  - Energy Economics
LA  - en
SN  - 0140-9883
ST  - Assessing energy vulnerability and its impact on carbon emissions
UR  - https://www.sciencedirect.com/science/article/pii/S0140988323000555
Y2  - 2023/06/09/03:35:07
KW  - CO emissions
KW  - Energy vulnerability
KW  - Global case
KW  - Heterogeneity
KW  - Mediating effects
ER  -
```

转换为如下的格式：

```
[2] 标题：Intersecting near-optimal spaces: European power systems with more resilience to weather variability
作者：Grochowicz, Aleksander; van Greevenbroek, Koen; Benth, Fred Espen; Zeyringer, Marianne
期刊名称：ENERGY ECONOMICS
出版时间：Feb 2023；卷：118，文献号：106496
JCR分区：SSCI一区
引用位置：
引用原句：
```

输出的结果按年份从近到远排序

## 注意事项

- 在使用时请注意修改`main`函数中的文件路径
- 2021jcr信息来源于网络，不保证信息完全正确