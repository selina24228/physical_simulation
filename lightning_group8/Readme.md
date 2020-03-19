# Group 8

## Topic: 
Lightning

## Introduction and expect achevement:

對閃電的成因進行微觀分析，模擬電子在空氣中的運動
再以巨觀的角度和RRT algorithm 來進行閃電路徑的模擬


## Members
*  b06902064 方淑玲
*  b06902104 吳由由
*  b06902116 高為勳

## Method

*code by vpython

* Free electrons and positively charged ions move through the ionized air between balls.

用兩顆大球模擬帶電氣體團，與幾顆小球模擬離子與電子，

用電場受力的方法使電子與離子接觸放光再電離，直到兩顆大球帶電量不夠為止

* lightning path simulation

Use RRT algorithm製作random tree 來模擬閃電在空氣中找最小路徑的過程

模擬自然閃電、 高壓棒間空氣、 電漿球的找路徑狀況


## Planning and Timeline

5/21~5/31 研讀閃電原理(DBM)與程式實作設計思考

6/1~6/7   初步閃電模擬完成

6/8~6/15  進階原理模擬或初步階段程式強化

6/16~6/18 最後debug與修飾

6/19,6/20 presentation


6/13 討論實作進度
* DBM實作遇到困難 在尋找其他替代方式
*　要做連鎖反應
* 模擬nuon撞開電子的連鎖反應
* 考慮分小部分單一模擬

*後期更新
 
 以RRT algorithm 取代 DBM 做閃電路徑的模擬

## Responsibility

高為勳  
	用程式模擬及介紹兩團帶電氣體團之間的導電情況。
	
	code: Free electrons and positively charged ions move through the ionized air between balls.
	
	video: Free electrons and positively charged ions move through the ionized air between balls.
	
	資料查找

吳由由  
	用 RRT algorithm 模擬閃電的路徑 
	
	code: RRT 模擬閃電路徑 電漿球、一般閃電、高壓棒
	
	video: RRT 模擬閃電路徑 電漿球、一般閃電、高壓棒
        
	資料查找 
	
	影片剪輯 

方淑玲: 資料查找 





## References
* introduction of lightning: 
https://en.wikipedia.org/wiki/Lightning

* dielectric breakdown model: 
https://codepen.io/jllodra/pen/GFswf/

* DBM: 
https://aip.scitation.org/doi/full/10.1063/1.4922437

    http://gamma.cs.unc.edu/FAST_LIGHTNING/lightning_tvcg_2007.pdf  

    https://math.nist.gov/mcsd/savg/parallel/dielectric/index.html  

* RRT
https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree
	
	https://www.cs.cmu.edu/~motionplanning/lecture/lec20.pdf
	
	https://2018.robotix.in/tutorial/pathplanning/rrtplanner/

