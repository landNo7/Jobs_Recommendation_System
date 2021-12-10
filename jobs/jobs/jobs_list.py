# -!- coding: utf-8 -!-
from lxml import etree

html ='''
    <div class="filter">
        <div class="tg">全部招聘职位</div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/houduankaifa/"><strong>后端开发</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/gaojiruanjian/">高级软件工程师</a><a href="https://jobs.51job.com/ruanjian/">软件工程师</a><a href="https://jobs.51job.com/erp-jishukaifa/">ERP技术开发</a><a href="https://jobs.51job.com/phpkaifa/">PHP开发工程师</a><a href="https://jobs.51job.com/javakaifa/">Java开发工程师</a><a href="https://jobs.51job.com/cyuyankaifa/">C/C++开发工程师</a><a href="https://jobs.51job.com/xitongfenxi/">系统分析员</a><a href="https://jobs.51job.com/pythonkaifa/">Python开发工程师</a><a href="https://jobs.51job.com/netkaifa/">.NET开发工程师</a><a href="https://jobs.51job.com/qukuailian/">区块链开发</a><a href="https://jobs.51job.com/hadoopkaifa/">Hadoop工程师</a><a href="https://jobs.51job.com/dashujukaifa/">大数据开发工程师</a><a href="https://jobs.51job.com/pachongkaifa/">爬虫开发工程师</a><a href="https://jobs.51job.com/jiaobenkaifa/">脚本开发工程师</a><a href="https://jobs.51job.com/duomeitikaifa/">多媒体开发工程师</a><a href="https://jobs.51job.com/jsjrj-others/">其他</a><a href="https://jobs.51job.com/xitongjiagou/">系统架构设计师</a><a href="https://jobs.51job.com/jishuwenyuan/">技术文员/助理</a><a href="https://jobs.51job.com/wendanggongchengshi/">技术文档工程师</a><a href="https://jobs.51job.com/rubykaifa/">Ruby开发工程师</a><a href="https://jobs.51job.com/gokaifa/">Go开发工程师</a><a href="https://jobs.51job.com/csharpkaifa/">C#开发工程师</a><a href="https://jobs.51job.com/quanzhangongchengshi/">全栈工程师</a><a href="https://jobs.51job.com/gisgongchengshi/">GIS工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/xiaoshouguanli/"><strong>销售管理</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/xiaoshouzongjian/">销售总监</a><a href="https://jobs.51job.com/xiaoshoujingli/">销售经理</a><a href="https://jobs.51job.com/xiaoshouzhuguan/">销售主管</a><a href="https://jobs.51job.com/qudaofenxiaojingli/">渠道/分销经理</a><a href="https://jobs.51job.com/kehujingli/">客户经理/主管</a><a href="https://jobs.51job.com/qudaofenxiaozhuguan/">渠道/分销主管</a><a href="https://jobs.51job.com/quyuxiaoshoujingli/">区域销售经理</a><a href="https://jobs.51job.com/quyuxiaoshouzongjian/">区域销售总监</a><a href="https://jobs.51job.com/xsgl-others/">其他</a><a href="https://jobs.51job.com/yewutuozhan/">业务拓展主管/经理</a><a href="https://jobs.51job.com/qudaofenxiaozongjian/">渠道/分销总监</a><a href="https://jobs.51job.com/tuangoujingli/">团购经理/主管</a><a href="https://jobs.51job.com/dakehuguanli/">大客户管理</a><a href="https://jobs.51job.com/quyuxiaoshouzhuguan/">区域销售主管</a><a href="https://jobs.51job.com/chengshijingli/">城市经理</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/shichangyingxiao/"><strong>市场/营销</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/mkt-tuozhanzongjian/">市场/营销/拓展总监</a><a href="https://jobs.51job.com/mkt-tuozhanjingli/">市场/营销/拓展经理</a><a href="https://jobs.51job.com/mkt-tuozhanzhuguan/">市场/营销/拓展主管</a><a href="https://jobs.51job.com/mkt-tuozhanzhuanyuan/">市场/营销/拓展专员</a><a href="https://jobs.51job.com/shichangzhuli/">市场助理</a><a href="https://jobs.51job.com/chanpinpinpaijingli/">产品/品牌经理</a><a href="https://jobs.51job.com/chanpinpinpaizhuguan/">产品/品牌主管</a><a href="https://jobs.51job.com/shichangtonglu/">市场通路经理/主管</a><a href="https://jobs.51job.com/cuxiaojingli/">促销经理</a><a href="https://jobs.51job.com/shichangfenxi/">市场分析/调研人员</a><a href="https://jobs.51job.com/scyx-others/">其他</a><a href="https://jobs.51job.com/pinpaizhuanyuan/">产品/品牌专员</a><a href="https://jobs.51job.com/shichangtongluzhuanyuan/">市场通路专员</a><a href="https://jobs.51job.com/shichangqihuajingli/">市场企划经理/主管</a><a href="https://jobs.51job.com/shichangqihuazhuanyuan/">市场企划专员</a><a href="https://jobs.51job.com/xindiankaifa/">选址拓展/新店开发</a><a href="https://jobs.51job.com/hulianwangyingxiaoshi/">互联网营销师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/caiwushenji/"><strong>财务/审计/税务</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/caiwuzongjian/">财务总监</a><a href="https://jobs.51job.com/caiwujingli/">财务经理</a><a href="https://jobs.51job.com/caiwuzhuguan/">财务主管/总账主管</a><a href="https://jobs.51job.com/kuaijijingli/">会计经理/会计主管</a><a href="https://jobs.51job.com/kuaiji/">会计</a><a href="https://jobs.51job.com/caiwufenxijingli/">财务分析经理/主管</a><a href="https://jobs.51job.com/caiwufenxiyuan/">财务分析员</a><a href="https://jobs.51job.com/chengbenjingli/">成本经理/成本主管</a><a href="https://jobs.51job.com/chengbenguanli/">成本管理员</a><a href="https://jobs.51job.com/shenjijingli/">审计经理/主管</a><a href="https://jobs.51job.com/shuiwujingli/">税务经理/税务主管</a><a href="https://jobs.51job.com/shuiwuzhuanyuan/">税务专员/助理</a><a href="https://jobs.51job.com/chunayuan/">出纳员</a><a href="https://jobs.51job.com/shenjizhuli/">审计专员/助理</a><a href="https://jobs.51job.com/caiwuzhuli/">财务助理/财务文员</a><a href="https://jobs.51job.com/cwsj-others/">其他</a><a href="https://jobs.51job.com/cfo-shouxicaiwu/">首席财务官 CFO</a><a href="https://jobs.51job.com/caiwuguwen/">财务顾问</a><a href="https://jobs.51job.com/tongjiyuan/">统计员</a><a href="https://jobs.51job.com/gudingzichankuaiji/">固定资产会计</a><a href="https://jobs.51job.com/zijinjingli/">资金经理/主管</a><a href="https://jobs.51job.com/zijinzhuanyuan/">资金专员</a><a href="https://jobs.51job.com/kuaijizhuli/">会计助理</a><a href="https://jobs.51job.com/caiwuzhuanyuan/">财务专员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/gongchengjixie/"><strong>工程/机械/能源</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jishuyanfajingli/">技术研发经理/主管</a><a href="https://jobs.51job.com/jishuyanfa/">技术研发工程师</a><a href="https://jobs.51job.com/shiyanshifuzeren/">实验室负责人/工程师</a><a href="https://jobs.51job.com/gongchengshebeijingli/">工程/设备经理</a><a href="https://jobs.51job.com/gongchengshebeizhuguan/">工程/设备主管</a><a href="https://jobs.51job.com/gongchengshebei/">工程/设备工程师</a><a href="https://jobs.51job.com/gongchengjixiehuitu/">工程/机械绘图员</a><a href="https://jobs.51job.com/weixiugongchengshi/">维修工程师</a><a href="https://jobs.51job.com/jixiegongchengshi/">机械工程师</a><a href="https://jobs.51job.com/jidiangongchengshi/">机电工程师</a><a href="https://jobs.51job.com/chanpingongyi/">产品工艺/制程工程师</a><a href="https://jobs.51job.com/mojugongchengshi/">模具工程师</a><a href="https://jobs.51job.com/chanpinguihua/">产品规划工程师</a><a href="https://jobs.51job.com/gongyegongchengshi/">工业工程师</a><a href="https://jobs.51job.com/jiegougongchengshi/">结构工程师</a><a href="https://jobs.51job.com/zhuzaoduanzao/">铸造/锻造工程师/技师</a><a href="https://jobs.51job.com/zhusugongchengshi/">注塑工程师/技师</a><a href="https://jobs.51job.com/hanjiegongchengshi/">焊接工程师/技师</a><a href="https://jobs.51job.com/jiajugongchengshi/">夹具工程师/技师</a><a href="https://jobs.51job.com/cnc-gongchengshi/">CNC工程师</a><a href="https://jobs.51job.com/chongyagongchengshi/">冲压工程师/技师</a><a href="https://jobs.51job.com/guolugongchengshi/">锅炉工程师/技师</a><a href="https://jobs.51job.com/dianligongchengshi/">电力工程师/技术员</a><a href="https://jobs.51job.com/guangyuanzhaoming/">光源与照明工程</a><a href="https://jobs.51job.com/qimogongchengshi/">汽车/摩托车工程师</a><a href="https://jobs.51job.com/chuanbogongchengshi/">船舶工程师</a><a href="https://jobs.51job.com/feixingqisheji/">飞行器设计与制造</a><a href="https://jobs.51job.com/gcjx-others/">其他</a><a href="https://jobs.51job.com/guidaojiaotong/">轨道交通工程师/技术员</a><a href="https://jobs.51job.com/feijiweixiu/">飞机维修机械师</a><a href="https://jobs.51job.com/shuilishuidian/">水利/水电工程师</a><a href="https://jobs.51job.com/shiyoutianranqijishu/">石油天然气技术人员</a><a href="https://jobs.51job.com/kuangchandizhikantan/">矿产勘探/地质勘测工程师</a><a href="https://jobs.51job.com/weixiujingli/">维修经理/主管</a><a href="https://jobs.51job.com/zhuangpeigongchengshi/">装配工程师/技师</a><a href="https://jobs.51job.com/cailiaogongchengshi/">材料工程师</a><a href="https://jobs.51job.com/guangfuxitong/">光伏系统工程师</a><a href="https://jobs.51job.com/xiangmuguanli/">项目管理</a><a href="https://jobs.51job.com/kongtiaoreneng/">空调/热能工程师</a><a href="https://jobs.51job.com/jixiesheji/">机械设计</a><a href="https://jobs.51job.com/mujusheji/">模具设计</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/renliziyuan/"><strong>人力资源</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/renshizongjian/">人事总监</a><a href="https://jobs.51job.com/renshijingli/">人事经理</a><a href="https://jobs.51job.com/renshizhuguan/">人事主管</a><a href="https://jobs.51job.com/renshizhuanyuan/">人事专员</a><a href="https://jobs.51job.com/renshizhuli/">人事助理</a><a href="https://jobs.51job.com/zhaopinjingli/">招聘经理/主管</a><a href="https://jobs.51job.com/xinzifulijingli/">薪资福利经理/主管</a><a href="https://jobs.51job.com/xinzifulizhuanyuan/">薪资福利专员/助理</a><a href="https://jobs.51job.com/peixunjingli/">培训经理/主管</a><a href="https://jobs.51job.com/peixunzhuanyuan/">培训专员/助理/培训师</a><a href="https://jobs.51job.com/hrbp/">HRBP</a><a href="https://jobs.51job.com/rlzy-others/">其他</a><a href="https://jobs.51job.com/zhaopinzhuli/">招聘专员/助理</a><a href="https://jobs.51job.com/jixiaokaohejingli/">绩效考核经理/主管</a><a href="https://jobs.51job.com/jixiaokaohezhuli/">绩效考核专员/助理</a><a href="https://jobs.51job.com/qiyewenhua/">企业文化/员工关系/工会管理</a><a href="https://jobs.51job.com/renliziyuanxinxi/">人力资源信息系统专员</a><a href="https://jobs.51job.com/laowupaiqian/">劳务派遣专员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/gaojiguanli/"><strong>高级管理</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/ceo-zongcai/">首席执行官CEO/总裁/总经理</a><a href="https://jobs.51job.com/fuzongcai/">副总经理/副总裁</a><a href="https://jobs.51job.com/zongcaizhuli/">总裁助理/总经理助理</a><a href="https://jobs.51job.com/hehuoren/">合伙人</a><a href="https://jobs.51job.com/zongjian/">总监/部门经理</a><a href="https://jobs.51job.com/gjgl-others/">其他</a><a href="https://jobs.51job.com/coo-yunyingguan/">首席运营官COO</a><a href="https://jobs.51job.com/shouxidaibiao/">办事处首席代表</a><a href="https://jobs.51job.com/fengongsijingli/">办事处/分公司/分支机构经理</a><a href="https://jobs.51job.com/fazhanzongjian/">策略发展总监</a><a href="https://jobs.51job.com/qiyemishu/">企业秘书/董事会秘书</a><a href="https://jobs.51job.com/touziguanxi/">投资者关系</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/wuliucangchu/"><strong>物流/仓储</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/wuliujingli/">物流经理</a><a href="https://jobs.51job.com/wuliuzhuguan/">物流主管</a><a href="https://jobs.51job.com/wuliaojingli/">物料经理</a><a href="https://jobs.51job.com/wuliaozhuguan/">物料主管/专员</a><a href="https://jobs.51job.com/cangkujingli/">仓库经理/主管</a><a href="https://jobs.51job.com/cangkuguanliyuan/">仓库管理员</a><a href="https://jobs.51job.com/yunshujingli/">运输经理/主管</a><a href="https://jobs.51job.com/baoguan/">报关与报检</a><a href="https://jobs.51job.com/danzhengyuan/">单证员</a><a href="https://jobs.51job.com/kuaidiyuan/">快递员</a><a href="https://jobs.51job.com/wuliuzhuli/">物流专员/助理</a><a href="https://jobs.51job.com/wuliuyunshu/">船务/空运陆运操作</a><a href="https://jobs.51job.com/cangchulihuoyuan/">仓储理货员</a><a href="https://jobs.51job.com/wlcc-others/">其他</a><a href="https://jobs.51job.com/gongyinglianjingli/">供应链经理</a><a href="https://jobs.51job.com/gongyinglianzhuguan/">供应链主管/专员</a><a href="https://jobs.51job.com/wuliuzongjian/">物流总监</a><a href="https://jobs.51job.com/gongyinglianzongjian/">供应链总监</a><a href="https://jobs.51job.com/huoyundaili/">货运代理</a><a href="https://jobs.51job.com/jizhuangxiangyewu/">集装箱业务</a><a href="https://jobs.51job.com/diaoduyuan/">调度员</a><a href="https://jobs.51job.com/haiguanshiwu/">海关事务管理</a><a href="https://jobs.51job.com/wlxiangmujingli/">项目经理/主管</a><a href="https://jobs.51job.com/dingdanchuli/">订单处理员</a><a href="https://jobs.51job.com/anjianyuan/">安检员</a><a href="https://jobs.51job.com/banyungong/">搬运工</a><a href="https://jobs.51job.com/wuliuxiaoshou/">物流销售</a><a href="https://jobs.51job.com/fenjianyuan/">分拣员</a><a href="https://jobs.51job.com/zhuangxiegong/">装卸工</a><a href="https://jobs.51job.com/cangkuwenyuan/">仓库文员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/gongyeyishusheji/"><strong>工业/艺术设计</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/gongyesheji/">工业设计/产品设计</a><a href="https://jobs.51job.com/gongyipinsheji/">工艺品/珠宝设计鉴定</a><a href="https://jobs.51job.com/yssj-others/">其他</a><a href="https://jobs.51job.com/zhanlansheji/">展览/展示/店面设计</a><a href="https://jobs.51job.com/baozhuangsheji/">包装设计</a><a href="https://jobs.51job.com/wanjusheji/">玩具设计</a><a href="https://jobs.51job.com/zhaomingsheji/">照明设计</a><a href="https://jobs.51job.com/chenliesheji/">陈列设计</a><a href="https://jobs.51job.com/jiajuleisheji/">家具设计</a><a href="https://jobs.51job.com/jiajuchanpinsheji/">家居设计</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/keyan/"><strong>科研</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/keyanrenyuan/">科研人员</a><a href="https://jobs.51job.com/keyanguanli/">科研管理人员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/lvshifawu/"><strong>律师/法务/合规</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/lvshifalvguwen/">律师/法律顾问</a><a href="https://jobs.51job.com/fawuzhuguan/">法务主管/专员</a><a href="https://jobs.51job.com/lvshizhuli/">律师助理</a><a href="https://jobs.51job.com/lsfw-others/">其他</a><a href="https://jobs.51job.com/fawujingli/">法务经理</a><a href="https://jobs.51job.com/fawuzhuli/">法务助理</a><a href="https://jobs.51job.com/zhishichanquan/">知识产权/专利/商标</a><a href="https://jobs.51job.com/heguijingli/">合规经理</a><a href="https://jobs.51job.com/heguizhuguan/">合规主管/专员</a><a href="https://jobs.51job.com/fawuzongjian/">法务总监</a><a href="https://jobs.51job.com/qiyemaoyihegui/">企业贸易合规师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jiaoshi/"><strong>教师</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jiangshi/">讲师/助教</a><a href="https://jobs.51job.com/jiajiao/">家教</a><a href="https://jobs.51job.com/js-others/">其他</a><a href="https://jobs.51job.com/youjiao/">幼教</a><a href="https://jobs.51job.com/daxuejiaoshou/">大学教授</a><a href="https://jobs.51job.com/xiaoxuejiaoshi/">小学教师</a><a href="https://jobs.51job.com/jianzhijiaoshi/">兼职教师</a><a href="https://jobs.51job.com/zhijijiaoshi/">职业技术教师</a><a href="https://jobs.51job.com/qitawaiyulaoshi/">其他外语老师</a><a href="https://jobs.51job.com/tiyujiaoshi/">体育教师</a><a href="https://jobs.51job.com/zaixianfudao/">在线辅导老师</a><a href="https://jobs.51job.com/yingyulaoshi/">英语老师</a><a href="https://jobs.51job.com/shuxuelaoshi/">数学老师</a><a href="https://jobs.51job.com/yuwenlaoshi/">语文老师</a><a href="https://jobs.51job.com/wulilaoshi/">物理老师</a><a href="https://jobs.51job.com/huaxuelaoshi/">化学老师</a><a href="https://jobs.51job.com/riyulaoshi/">日语老师</a><a href="https://jobs.51job.com/zaojiaolaoshi/">早教老师</a><a href="https://jobs.51job.com/yinyuelaoshi/">音乐老师</a><a href="https://jobs.51job.com/meishulaoshi/">美术老师</a><a href="https://jobs.51job.com/chuzhongjiaoshi/">初中教师</a><a href="https://jobs.51job.com/gaozhongjiaoshi/">高中教师</a><a href="https://jobs.51job.com/gangqinlaoshi/">钢琴老师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yiliao/"><strong>医院/医疗/护理</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/neike/">内科医生</a><a href="https://jobs.51job.com/yiyuanguanli/">医院管理人员</a><a href="https://jobs.51job.com/yaokuzhuren/">药库主任/药剂师</a><a href="https://jobs.51job.com/hushi/">护士/护理人员</a><a href="https://jobs.51job.com/mazui/">麻醉医生</a><a href="https://jobs.51job.com/xinli/">心理医生</a><a href="https://jobs.51job.com/yixuejianyan/">医学检验</a><a href="https://jobs.51job.com/yl-others/">其他</a><a href="https://jobs.51job.com/zhenjiutuina/">针灸/推拿</a><a href="https://jobs.51job.com/yingyangshi/">营养师</a><a href="https://jobs.51job.com/shouyi/">兽医</a><a href="https://jobs.51job.com/waike/">外科医生</a><a href="https://jobs.51job.com/zhuanke/">专科医生</a><a href="https://jobs.51job.com/yake/">牙科医生</a><a href="https://jobs.51job.com/zhengxing/">美容整形师</a><a href="https://jobs.51job.com/liliaoshi/">理疗师</a><a href="https://jobs.51job.com/zhongyike/">中医科医生</a><a href="https://jobs.51job.com/jibingkongzhi/">公共卫生/疾病控制</a><a href="https://jobs.51job.com/hulizhuren/">护理主任/护士长</a><a href="https://jobs.51job.com/erke/">儿科医生</a><a href="https://jobs.51job.com/yanguangshi/">验光师</a><a href="https://jobs.51job.com/chaoshengyingxiang/">超声影像/放射科医师</a><a href="https://jobs.51job.com/zonghemenzhen/">综合门诊/全科医生</a><a href="https://jobs.51job.com/yimeizixun/">医美咨询</a><a href="https://jobs.51job.com/jiankangguanli/">健康管理师</a><a href="https://jobs.51job.com/hesuanjiance/">核酸检测员</a><a href="https://jobs.51job.com/fangyiyuan/">防疫员</a><a href="https://jobs.51job.com/xiaoduyuan/">消毒员</a><a href="https://jobs.51job.com/xinlizixunshi/">心理咨询师</a><a href="https://jobs.51job.com/daoyi/">导医</a><a href="https://jobs.51job.com/fuchanke/">妇产科医生</a><a href="https://jobs.51job.com/yanke/">眼科医生</a><a href="https://jobs.51job.com/yixueguwen/">医学顾问</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/zixunguwen/"><strong>咨询/顾问</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/zhuanyeguwen/">专业顾问</a><a href="https://jobs.51job.com/zixunzongjian/">咨询总监</a><a href="https://jobs.51job.com/zixunjingli/">咨询经理</a><a href="https://jobs.51job.com/zixunyuan/">咨询员</a><a href="https://jobs.51job.com/zxgw-others/">其他</a><a href="https://jobs.51job.com/zhuanyepeixun/">专业培训师</a><a href="https://jobs.51job.com/xinxifenxi/">情报信息分析人员</a><a href="https://jobs.51job.com/lietou/">猎头/人才中介</a><a href="https://jobs.51job.com/diaoyanyuan/">调研员</a><a href="https://jobs.51job.com/guanlizixunshi/">管理咨询师</a><a href="https://jobs.51job.com/hangyeyanjiuyuan/">行业研究员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/zhengfufeiyinglijigou/"><strong>政府/非盈利机构</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/gongwuzp/">公务员</a><a href="https://jobs.51job.com/zhiyuanzhe/">志愿者/社会工作者</a><a href="https://jobs.51job.com/chengshiguanliwanggeyuan/">城市管理网格员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/zaixiaoxuesheng/"><strong>在校学生</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/zhongzhuanzhixiao/">中专/职校生</a><a href="https://jobs.51job.com/daxueyingjie/">大学/大专应届毕业生</a><a href="https://jobs.51job.com/zxxs-others/">其他</a><a href="https://jobs.51job.com/yanjiusheng/">研究生</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/peixunshixi/"><strong>储备干部/培训生/实习生</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/peixunsheng/">培训生</a><a href="https://jobs.51job.com/chubeiganbu/">储备干部</a><a href="https://jobs.51job.com/shixisheng/">实习生</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jiaotongyunshu/"><strong>交通运输服务</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/chengwuyuan/">乘务员</a><a href="https://jobs.51job.com/shangwusiji/">商务司机</a><a href="https://jobs.51job.com/feijijizhang/">飞机机长/副机长</a><a href="https://jobs.51job.com/kongcheng/">空乘人员</a><a href="https://jobs.51job.com/diqinrenyuan/">地勤人员</a><a href="https://jobs.51job.com/liechechezhang/">列车/地铁车长</a><a href="https://jobs.51job.com/liechesiji/">列车/地铁司机</a><a href="https://jobs.51job.com/chuanzhang/">船长/副船长</a><a href="https://jobs.51job.com/chuanyuan/">船员</a><a href="https://jobs.51job.com/jtys-others/">其他</a><a href="https://jobs.51job.com/keyunsiji/">客运司机</a><a href="https://jobs.51job.com/huoyunsiji/">货运司机</a><a href="https://jobs.51job.com/chuzuchesiji/">出租车司机</a><a href="https://jobs.51job.com/banchesiji/">班车司机</a><a href="https://jobs.51job.com/tezhongchesiji/">特种车司机</a><a href="https://jobs.51job.com/jiaxiaojiaolian/">驾校教练</a><a href="https://jobs.51job.com/daijia/">代驾</a><a href="https://jobs.51job.com/zhanwurenyuan/">站务人员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/fanyi/"><strong>翻译</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/yingyufanyi/">英语翻译</a><a href="https://jobs.51job.com/riyufanyi/">日语翻译</a><a href="https://jobs.51job.com/deyufanyi/">德语翻译</a><a href="https://jobs.51job.com/fayufanyi/">法语翻译</a><a href="https://jobs.51job.com/eyufanyi/">俄语翻译</a><a href="https://jobs.51job.com/xibanyayufanyi/">西班牙语翻译</a><a href="https://jobs.51job.com/hanyufanyi/">韩语/朝鲜语翻译</a><a href="https://jobs.51job.com/qitafanyi/">其他语种翻译</a><a href="https://jobs.51job.com/alaboyufanyi/">阿拉伯语翻译</a><a href="https://jobs.51job.com/yidaliyufanyi/">意大利语翻译</a><a href="https://jobs.51job.com/putaoyayufanyi/">葡萄牙语翻译</a><a href="https://jobs.51job.com/taiyufanyi/">泰语翻译</a><a href="https://jobs.51job.com/fangyanfanyi/">中国方言翻译</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jianzhugongcheng/"><strong>建筑工程与装潢</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jianzhugongchengshi/">建筑工程师</a><a href="https://jobs.51job.com/jiegoutumu/">结构/土木/土建工程师</a><a href="https://jobs.51job.com/jianzhujidian/">建筑机电工程师</a><a href="https://jobs.51job.com/geipaishuinuantong/">给排水/暖通工程</a><a href="https://jobs.51job.com/gongchengzaojia/">工程造价师/预结算经理</a><a href="https://jobs.51job.com/jianzhugongchengzp/">建筑工程管理/项目经理</a><a href="https://jobs.51job.com/gongchengjianli/">工程监理</a><a href="https://jobs.51job.com/jianzhuanzhuang/">建筑安装施工员</a><a href="https://jobs.51job.com/xiaofanganquan/">消防安全</a><a href="https://jobs.51job.com/jzsz-others/">其他</a><a href="https://jobs.51job.com/daolugongcheng/">公路/桥梁/港口/隧道工程</a><a href="https://jobs.51job.com/yantugongcheng/">岩土工程</a><a href="https://jobs.51job.com/cehuiceliang/">测绘/测量</a><a href="https://jobs.51job.com/gongchengyanshou/">建筑工程验收</a><a href="https://jobs.51job.com/muqianggongchengshi/">幕墙工程师</a><a href="https://jobs.51job.com/gaojijianzhugongchengshi/">高级建筑工程师/总工</a><a href="https://jobs.51job.com/yujiesuanyuan/">预结算员</a><a href="https://jobs.51job.com/louyuzidonghua/">楼宇自动化</a><a href="https://jobs.51job.com/zonghebuxian/">智能大厦/综合布线/安防/弱电</a><a href="https://jobs.51job.com/kaifabaojian/">开发报建</a><a href="https://jobs.51job.com/hetongguanli/">合同管理</a><a href="https://jobs.51job.com/anquanyuan/">安全员</a><a href="https://jobs.51job.com/ziliaoyuan/">资料员</a><a href="https://jobs.51job.com/shizhenggongcheng/">市政工程师</a><a href="https://jobs.51job.com/jianzhuxiangmuzhuli/">建筑项目助理</a><a href="https://jobs.51job.com/qizhugong/">砌筑工</a><a href="https://jobs.51job.com/wagong/">瓦工</a><a href="https://jobs.51job.com/hunningtugong/">混凝土工</a><a href="https://jobs.51job.com/jiaozhugong/">浇注工</a><a href="https://jobs.51job.com/gangjingong/">钢筋工</a><a href="https://jobs.51job.com/mugongzp/">木工</a><a href="https://jobs.51job.com/youqigong/">油漆工</a><a href="https://jobs.51job.com/diantigong/">电梯工</a><a href="https://jobs.51job.com/mohuigong/">抹灰工</a><a href="https://jobs.51job.com/shigongkailiao/">施工开料工</a><a href="https://jobs.51job.com/guandaonuantong/">管道/暖通</a><a href="https://jobs.51job.com/gongzhang/">工长</a><a href="https://jobs.51job.com/jingzhuangxiugongchengshi/">精装修工程师</a><a href="https://jobs.51job.com/fangxiugongchengshi/">房修工程师</a><a href="https://jobs.51job.com/cailiaoyuan/">材料员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yinhang/"><strong>银行</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/xingzhang/">行长/副行长</a><a href="https://jobs.51job.com/zichanpinggu/">资产评估/分析</a><a href="https://jobs.51job.com/fengxiankongzhi/">风险控制</a><a href="https://jobs.51job.com/jinchukoujiesuan/">进出口/信用证结算</a><a href="https://jobs.51job.com/qingsuanrenyuan/">清算人员</a><a href="https://jobs.51job.com/waihuijiaoyi/">外汇交易</a><a href="https://jobs.51job.com/gaojikehujingli/">高级客户经理/客户经理</a><a href="https://jobs.51job.com/kehuzhuguan/">客户主管/专员</a><a href="https://jobs.51job.com/xindaiguanli/">信贷管理</a><a href="https://jobs.51job.com/yinxingguiyuan/">银行柜员</a><a href="https://jobs.51job.com/yh-others/">其他</a><a href="https://jobs.51job.com/xinyongkaxiaoshou/">信用卡销售</a><a href="https://jobs.51job.com/gerenyewubumenjingli/">个人业务部门经理/主管</a><a href="https://jobs.51job.com/gerenyewukehujingli/">个人业务客户经理</a><a href="https://jobs.51job.com/gongsiyewubumenjingli/">公司业务部门经理/主管</a><a href="https://jobs.51job.com/gongsiyewukehujingli/">公司业务客户经理</a><a href="https://jobs.51job.com/zongheyewujingli/">综合业务经理/主管</a><a href="https://jobs.51job.com/zongheyewuzhuanyuan/">综合业务专员</a><a href="https://jobs.51job.com/xinshenhecha/">信审核查</a><a href="https://jobs.51job.com/yingyebujingli/">营业部大堂经理</a><a href="https://jobs.51job.com/yinhangkehuzongjian/">银行客户总监</a><a href="https://jobs.51job.com/hujiaozhongxinkefu/">呼叫中心客服</a><a href="https://jobs.51job.com/licaijingli/">理财经理</a><a href="https://jobs.51job.com/xiaoweixindaiyuan/">小微信贷专员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/xingzhenghouqin/"><strong>行政/后勤</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/xingzhengzongjian/">行政总监</a><a href="https://jobs.51job.com/xingzhengjingli/">行政经理/主管/办公室主任</a><a href="https://jobs.51job.com/xingzhengzhuli/">行政专员/助理</a><a href="https://jobs.51job.com/jinglizhuli/">经理助理/秘书</a><a href="https://jobs.51job.com/qiantaijiedai/">前台接待/总机/接待生</a><a href="https://jobs.51job.com/houqin/">后勤</a><a href="https://jobs.51job.com/ziliaoguanli/">图书管理员/资料管理员</a><a href="https://jobs.51job.com/diannaocaozuo/">电脑操作员/打字员</a><a href="https://jobs.51job.com/xzhq-others/">其他</a><a href="https://jobs.51job.com/danggongtuanganshi/">党工团干事</a><a href="https://jobs.51job.com/wenyuan/">文员</a><a href="https://jobs.51job.com/danganguanliyuan/">档案管理员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jishuguanli/"><strong>技术管理</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jishuzongjian/">技术总监/经理</a><a href="https://jobs.51job.com/itxiangmuzongjian/">项目总监</a><a href="https://jobs.51job.com/itxiangmujingli/">项目经理</a><a href="https://jobs.51job.com/xiangmuzhuguan/">项目主管</a><a href="https://jobs.51job.com/xiangmuzhixing/">项目执行/协调人员</a><a href="https://jobs.51job.com/jishuguanli-others/">其他</a><a href="https://jobs.51job.com/xiangmuzhuli/">项目助理</a><a href="https://jobs.51job.com/shouxijishuzhixingguan/">首席技术执行官CTO</a><a href="https://jobs.51job.com/shouxixinxiguan/">首席信息官CIO</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/ceshi/"><strong>测试</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/biaozhunhuagongchengshi/">标准化工程师</a><a href="https://jobs.51job.com/ceshijingli/">测试经理</a><a href="https://jobs.51job.com/xitongceshi/">系统测试</a><a href="https://jobs.51job.com/ruanjianceshi/">软件测试工程师</a><a href="https://jobs.51job.com/cs-others/">其他</a><a href="https://jobs.51job.com/gongnengceshi/">功能测试</a><a href="https://jobs.51job.com/xingnengceshi/">性能测试</a><a href="https://jobs.51job.com/zidonghuaceshi/">自动化测试</a><a href="https://jobs.51job.com/yidongduanceshi/">移动端测试</a><a href="https://jobs.51job.com/ceshikaifa/">测试开发</a><a href="https://jobs.51job.com/ceshizhuguan/">测试主管</a><a href="https://jobs.51job.com/anquanceshi/">安全测试</a><a href="https://jobs.51job.com/ceshigongchengshi/">测试工程师</a><a href="https://jobs.51job.com/ceshizongjian/">测试总监</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/tongxinjishukaifa/"><strong>通信技术开发及应用</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/tongxinjishu/">通信技术工程师</a><a href="https://jobs.51job.com/youxianchuanshu/">有线传输工程师</a><a href="https://jobs.51job.com/wuxiantongxin/">无线通信工程师</a><a href="https://jobs.51job.com/dianxinjiaohuan/">电信交换工程师</a><a href="https://jobs.51job.com/shujutongxin/">数据通信工程师</a><a href="https://jobs.51job.com/tongxinwangluo/">通信网络工程师</a><a href="https://jobs.51job.com/tongxindianyuan/">通信电源工程师</a><a href="https://jobs.51job.com/txjs-others/">其他</a><a href="https://jobs.51job.com/tongxinwendang/">通信文档工程师</a><a href="https://jobs.51job.com/tongxinchanpinjingli-gongchengshi/">通信产品经理/产品工程师</a><a href="https://jobs.51job.com/guangtongxin/">光通信工程师</a><a href="https://jobs.51job.com/shepingongchengshi/">射频工程师</a><a href="https://jobs.51job.com/tongxinceshi/">通信测试工程师</a><a href="https://jobs.51job.com/tongxinxiaoshou/">通信销售工程师</a><a href="https://jobs.51job.com/jizhan/">基站工程师</a><a href="https://jobs.51job.com/hexinwang/">核心网工程师</a><a href="https://jobs.51job.com/tongxinshebei/">通信设备工程师</a><a href="https://jobs.51job.com/tongxinxiangmuguanli/">通信项目管理</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/dianzi/"><strong>电子/电器/仪器仪表</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/dianzigongcheng/">电子工程师/技术员</a><a href="https://jobs.51job.com/dianqigongcheng/">电气工程师/技术员</a><a href="https://jobs.51job.com/dianlugongcheng/">电路工程师/技术员(模拟/数字)</a><a href="https://jobs.51job.com/dianshenggongcheng/">电声/音响工程师/技术员</a><a href="https://jobs.51job.com/zidongkongzhi/">自动控制工程师/技术员</a><a href="https://jobs.51job.com/dianziruanjian/">电子软件开发(ARM/MCU...)</a><a href="https://jobs.51job.com/qianrushiruanjian/">嵌入式软件开发(Linux/单片机/PLC/DSP…)</a><a href="https://jobs.51job.com/dianyuankaifa/">电池/电源开发</a><a href="https://jobs.51job.com/dianqiyanfa/">家用电器/数码产品研发</a><a href="https://jobs.51job.com/jiliangfenxi/">仪器/仪表/计量分析师</a><a href="https://jobs.51job.com/dz-others/">其他</a><a href="https://jobs.51job.com/dianzijishuyanfa/">电子技术研发工程师</a><a href="https://jobs.51job.com/guangdianzijishu/">激光/光电子技术</a><a href="https://jobs.51job.com/qianrushiyingjian/">嵌入式硬件开发(主板机…)</a><a href="https://jobs.51job.com/dianqiweixiu/">电子/电器维修工程师/技师</a><a href="https://jobs.51job.com/cidiangongchengshi/">变压器与磁电工程师</a><a href="https://jobs.51job.com/anfangxitong/">安防系统工程师</a><a href="https://jobs.51job.com/dianzigongyi/">电子工艺工程师</a><a href="https://jobs.51job.com/dianxixiaoshou/">电子销售工程师</a><a href="https://jobs.51job.com/dianziwendang/">电子文档工程师</a><a href="https://jobs.51job.com/dianzichanpinjingli/">电子产品经理/产品工程师</a><a href="https://jobs.51job.com/yingjian/">硬件工程师</a><a href="https://jobs.51job.com/gaojiyingjian/">高级硬件工程师</a><a href="https://jobs.51job.com/yingjianceshi/">硬件测试工程师</a><a href="https://jobs.51job.com/jilianggongchengshi/">计量工程师</a><a href="https://jobs.51job.com/dianzishebei/">电子设备工程师</a><a href="https://jobs.51job.com/dianziyuanqijian/">电子元器件工程师</a><a href="https://jobs.51job.com/jiqirentiaoshi/">机器人调试工程师</a><a href="https://jobs.51job.com/pcbgongchengshi/">PCB工程师</a><a href="https://jobs.51job.com/smtgongchengshi/">SMT工程师</a><a href="https://jobs.51job.com/plcgongchengshi/">PLC工程师</a><a href="https://jobs.51job.com/fuwujiqiren/">服务机器人应用技术员</a><a href="https://jobs.51job.com/zhinengyingjian/">智能硬件装调员</a><a href="https://jobs.51job.com/gongyeshijue/">工业视觉系统运维员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/xiaoshourenyuan/"><strong>销售人员</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/xiaoshoudaibiao/">销售代表</a><a href="https://jobs.51job.com/fenxiaozhuanyuan/">渠道/分销专员</a><a href="https://jobs.51job.com/kehudaibiao/">客户代表</a><a href="https://jobs.51job.com/xiaoshougongchengshi/">销售工程师</a><a href="https://jobs.51job.com/dianhuaxiaoshou/">电话销售</a><a href="https://jobs.51job.com/jingxiaoshang/">经销商</a><a href="https://jobs.51job.com/xs-others/">其他</a><a href="https://jobs.51job.com/tuangouyewuyuan/">团购业务员</a><a href="https://jobs.51job.com/dakehuxiaoshou/">大客户销售</a><a href="https://jobs.51job.com/wangluoxiaoshouzaixianxiaoshou/">网络销售/在线销售</a><a href="https://jobs.51job.com/huijiguwen/">会籍顾问</a><a href="https://jobs.51job.com/xiaoshouzhuli/">销售助理</a><a href="https://jobs.51job.com/zhiboxiaoshou/">直播销售</a><a href="https://jobs.51job.com/quyuxiaoshoudaibiao/">区域销售代表</a><a href="https://jobs.51job.com/haiwaixiaoshou/">海外销售</a><a href="https://jobs.51job.com/mendianxiaoshou/">门店销售</a><a href="https://jobs.51job.com/dituizhuanyuan/">地推专员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/xiaoshouxingzheng/"><strong>销售行政及商务</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/xiaoshouxingzhengjingli/">销售行政经理/主管</a><a href="https://jobs.51job.com/xiaoshouxingzhengzhuanyuan/">销售行政专员</a><a href="https://jobs.51job.com/shangwujingli/">商务经理</a><a href="https://jobs.51job.com/shangwuzhuguan/">商务主管/专员</a><a href="https://jobs.51job.com/shangwuzhuli/">商务助理</a><a href="https://jobs.51job.com/xiaoshouxingzhengzp/">销售行政助理</a><a href="https://jobs.51job.com/xsxz-others/">其他</a><a href="https://jobs.51job.com/yewufenxijingli/">业务分析经理/主管</a><a href="https://jobs.51job.com/yewufenxizhuli/">业务分析专员/助理</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/kefuzhichi/"><strong>客服及支持</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/kefuzongjian/">客服总监</a><a href="https://jobs.51job.com/kefujingli/">客服经理</a><a href="https://jobs.51job.com/kefuzhuguan/">客服主管</a><a href="https://jobs.51job.com/kefuzhuanyuan/">客服专员/助理</a><a href="https://jobs.51job.com/shouqianhoujishuzhichijingli/">售前/售后技术支持经理</a><a href="https://jobs.51job.com/shouqianhoujishuzhichizhuguan/">售前/售后技术支持主管</a><a href="https://jobs.51job.com/shouqianhoujishuzhichi/">售前/售后技术支持工程师</a><a href="https://jobs.51job.com/zixunrexian/">咨询热线/呼叫中心服务人员</a><a href="https://jobs.51job.com/kf-others/">其他</a><a href="https://jobs.51job.com/kehuguanxijingli/">客户关系经理/主管</a><a href="https://jobs.51job.com/tousuzhuanyuan/">投诉专员</a><a href="https://jobs.51job.com/vip-zhuanyuan/">VIP专员</a><a href="https://jobs.51job.com/zaixiankefu/">网络/在线客服</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jinrongzhengquan/"><strong>金融/证券/期货/投资</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/zhengquanqihuo/">证券/期货/外汇经纪人</a><a href="https://jobs.51job.com/zhengquanfenxishi/">证券分析师</a><a href="https://jobs.51job.com/caopanshou/">股票/期货操盘手</a><a href="https://jobs.51job.com/jingjiyanjiuyuan/">金融/经济研究员</a><a href="https://jobs.51job.com/touziyinhangyewu/">投资银行业务</a><a href="https://jobs.51job.com/rongzijingli/">融资经理/融资主管</a><a href="https://jobs.51job.com/rongzizhuanyuan/">融资专员</a><a href="https://jobs.51job.com/diandangyewu/">拍卖/担保/典当业务</a><a href="https://jobs.51job.com/jr-others/">其他</a><a href="https://jobs.51job.com/jinrongchanpinjingli/">金融产品经理</a><a href="https://jobs.51job.com/touziyinhangcaiwufenxi/">投资银行财务分析</a><a href="https://jobs.51job.com/fengxianguanli/">风险管理/控制</a><a href="https://jobs.51job.com/jinrongxiaoshou/">金融产品销售</a><a href="https://jobs.51job.com/lianghuafenxi/">量化研究</a><a href="https://jobs.51job.com/jigouyewuxiaoshou/">机构业务销售</a><a href="https://jobs.51job.com/yingyebuzongjingli/">营业部总经理/副总经理</a><a href="https://jobs.51job.com/qihuofenxi/">期货分析师</a><a href="https://jobs.51job.com/zhengquanjiaoyi/">证券交易员</a><a href="https://jobs.51job.com/gongsijinrong/">公司金融顾问</a><a href="https://jobs.51job.com/touzizongjian/">投资总监</a><a href="https://jobs.51job.com/jinrongtouzijingli/">投资经理</a><a href="https://jobs.51job.com/zichanguanli/">资产管理</a><a href="https://jobs.51job.com/jinrongtouziguwen/">投资顾问</a><a href="https://jobs.51job.com/jinronglicaiguwen/">理财顾问</a><a href="https://jobs.51job.com/cuishou/">催收</a><a href="https://jobs.51job.com/jijinjingli/">基金经理</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/baoxian/"><strong>保险</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/baoxianjingsuanshi/">保险精算师</a><a href="https://jobs.51job.com/baoxianchanpinkaifa/">保险产品开发/项目策划</a><a href="https://jobs.51job.com/baoxianyewujingli/">保险业务经理/主管</a><a href="https://jobs.51job.com/baoxianjingji/">保险经纪人/保险代理</a><a href="https://jobs.51job.com/licaiguwen/">理财顾问/财务规划师</a><a href="https://jobs.51job.com/chubeijingliren/">储备经理人</a><a href="https://jobs.51job.com/baoxianhebao/">保险核保</a><a href="https://jobs.51job.com/baoxianlipei/">保险理赔</a><a href="https://jobs.51job.com/baoxiankehufuwu/">保险客户服务/续期管理</a><a href="https://jobs.51job.com/baoxianpeixunshi/">保险培训师</a><a href="https://jobs.51job.com/baoxianneiqin/">保险内勤</a><a href="https://jobs.51job.com/bx-others/">其他</a><a href="https://jobs.51job.com/qiyueguanli/">契约管理</a><a href="https://jobs.51job.com/baoxiandianxiao/">保险电销</a><a href="https://jobs.51job.com/baoxianyewutuidong/">保险业务推动/督导</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/shengchanyingyun/"><strong>生产/营运</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/gongzhangjingli/">工厂经理/厂长</a><a href="https://jobs.51job.com/zonggongchengshi/">总工程师/副总工程师</a><a href="https://jobs.51job.com/xiangmujingli/">项目经理/主管</a><a href="https://jobs.51job.com/xiangmugongchengshi/">项目工程师</a><a href="https://jobs.51job.com/yingyunjingli/">营运经理</a><a href="https://jobs.51job.com/yingyunzhuguan/">营运主管</a><a href="https://jobs.51job.com/shengchanjingli/">生产经理/车间主任</a><a href="https://jobs.51job.com/shengchanjihua/">生产计划/物料管理(PMC)</a><a href="https://jobs.51job.com/shengchanzhuguan/">生产主管</a><a href="https://jobs.51job.com/huayanyuan/">化验员</a><a href="https://jobs.51job.com/scyy-others/">其他</a><a href="https://jobs.51job.com/shengchanwenyuan/">生产文员</a><a href="https://jobs.51job.com/xiangmuzongjian/">项目总监</a><a href="https://jobs.51job.com/shengchanzongjian/">生产总监</a><a href="https://jobs.51job.com/shengchanlingban/">生产领班/组长</a><a href="https://jobs.51job.com/shebeizhuguan/">设备主管</a><a href="https://jobs.51job.com/changwu/">厂务</a><a href="https://jobs.51job.com/shengchangendan/">生产跟单</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/zhilianganquan/"><strong>质量安全</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/ceshijingliqc/">质量管理/测试经理(QA/QC经理)</a><a href="https://jobs.51job.com/ceshizhuguanqc/">质量管理/测试主管(QA/QC主管)</a><a href="https://jobs.51job.com/ceshigongchengshiqc/">质量管理/测试工程师(QA/QC工程师)</a><a href="https://jobs.51job.com/zhijianyuanceshiyuan/">质检员/测试员(QC)</a><a href="https://jobs.51job.com/kekaodugongchengshi/">可靠度工程师</a><a href="https://jobs.51job.com/guzhangfenxi/">故障分析工程师</a><a href="https://jobs.51job.com/renzhenggongchengshi/">认证工程师</a><a href="https://jobs.51job.com/tixigongchengshi/">体系工程师</a><a href="https://jobs.51job.com/anquanjingli/">环境/健康/安全经理/主管（EHS）</a><a href="https://jobs.51job.com/anquangongchengshi/">环境/健康/安全工程师（EHS）</a><a href="https://jobs.51job.com/gongyingshangguanli/">供应商管理</a><a href="https://jobs.51job.com/caigouzhiliangguanli/">采购材料、设备质量管理</a><a href="https://jobs.51job.com/zlaq-others/">其他</a><a href="https://jobs.51job.com/anquanyuanzp/">安全员</a><a href="https://jobs.51job.com/shenheyuan/">审核员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jigongpugong/"><strong>技工普工</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jigongzp/">技工</a><a href="https://jobs.51job.com/hangong/">焊工</a><a href="https://jobs.51job.com/diangong/">电工</a><a href="https://jobs.51job.com/chachesijichanchesiji/">叉车司机/铲车司机</a><a href="https://jobs.51job.com/kongdiaogong/">空调工</a><a href="https://jobs.51job.com/shuigong/">水工</a><a href="https://jobs.51job.com/pugong/">普工/操作工</a><a href="https://jobs.51job.com/jg-others/">其他</a><a href="https://jobs.51job.com/zuzhuanggong/">组装工</a><a href="https://jobs.51job.com/baozhuanggong/">包装工</a><a href="https://jobs.51job.com/yahuhangong/">氩弧焊工</a><a href="https://jobs.51job.com/dianlixianlugong/">电力线路工</a><a href="https://jobs.51job.com/xuanyagong/">旋压工</a><a href="https://jobs.51job.com/yibiaogong/">仪表工</a><a href="https://jobs.51job.com/diandonggong/">电镀工</a><a href="https://jobs.51job.com/pensugong/">喷塑工</a><a href="https://jobs.51job.com/mugong/">木工</a><a href="https://jobs.51job.com/qigong/">漆工</a><a href="https://jobs.51job.com/diantigongzp/">电梯工</a><a href="https://jobs.51job.com/guolugong/">锅炉工</a><a href="https://jobs.51job.com/xuetugong/">学徒工</a><a href="https://jobs.51job.com/diaochesiji/">吊车司机</a><a href="https://jobs.51job.com/wajuejisiji/">挖掘机司机</a><a href="https://jobs.51job.com/3ddayincaozuo/">3D打印操作员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/fuzhuangfangzhi/"><strong>服装/纺织/皮革</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/fuzhuangsheji/">服装/纺织设计</a><a href="https://jobs.51job.com/mianliaofuliao/">面料辅料开发</a><a href="https://jobs.51job.com/mianliaocaigou/">面料辅料采购</a><a href="https://jobs.51job.com/fuzhuanggendan/">服装/纺织/皮革跟单</a><a href="https://jobs.51job.com/fuzhuangfangzhizhijianyuan/">服装纺织质检员(QA/QC)</a><a href="https://jobs.51job.com/digechugeshi/">板房/楦头/底格出格师</a><a href="https://jobs.51job.com/dayangzhiban/">打样/制版</a><a href="https://jobs.51job.com/zhiyangshi/">纸样师/车板工</a><a href="https://jobs.51job.com/caichuang/">裁床</a><a href="https://jobs.51job.com/fz-others/">其他</a><a href="https://jobs.51job.com/fangmayuan/">电脑放码员</a><a href="https://jobs.51job.com/fuzhuangshejizongjian/">服装/纺织设计总监</a><a href="https://jobs.51job.com/pigegongyishi/">服装/纺织/皮革工艺师</a><a href="https://jobs.51job.com/fuzhuanglingban/">服装领班</a><a href="https://jobs.51job.com/caijiangong/">裁剪工</a><a href="https://jobs.51job.com/caifengyinfang/">缝纫工</a><a href="https://jobs.51job.com/shoufenggong/">手缝工</a><a href="https://jobs.51job.com/tanggong/">烫工</a><a href="https://jobs.51job.com/yangyigong/">样衣工</a><a href="https://jobs.51job.com/fangzhigong/">纺织工</a><a href="https://jobs.51job.com/zhenzhigong/">针织工</a><a href="https://jobs.51job.com/peisegong/">配色工</a><a href="https://jobs.51job.com/yinrangong/">印染工</a><a href="https://jobs.51job.com/piaorangong/">漂染工</a><a href="https://jobs.51job.com/dangchegong/">挡车工</a><a href="https://jobs.51job.com/zhengjinggong/">整经工</a><a href="https://jobs.51job.com/xishagong/">细纱工</a><a href="https://jobs.51job.com/jiangshagong/">浆纱工</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/caigou/"><strong>采购</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/caigouzongjian/">采购总监</a><a href="https://jobs.51job.com/caigoujingli/">采购经理</a><a href="https://jobs.51job.com/caigouzhuguan/">采购主管</a><a href="https://jobs.51job.com/caigouyuan/">采购员</a><a href="https://jobs.51job.com/caigouzhuli/">采购助理</a><a href="https://jobs.51job.com/cg-othersd/">其他</a><a href="https://jobs.51job.com/maishou/">买手</a><a href="https://jobs.51job.com/gongyingshangkaifa/">供应商开发</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/maoyi/"><strong>贸易</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/waimaojingli/">贸易/外贸经理/主管</a><a href="https://jobs.51job.com/waimaozhuanyuan/">贸易/外贸专员/助理</a><a href="https://jobs.51job.com/guoneimaoyirenyuan/">国内贸易人员</a><a href="https://jobs.51job.com/yewugendanjingli/">业务跟单经理</a><a href="https://jobs.51job.com/gaojiyewugendan/">高级业务跟单</a><a href="https://jobs.51job.com/yewugendan/">业务跟单</a><a href="https://jobs.51job.com/zhuliyewugendan/">助理业务跟单</a><a href="https://jobs.51job.com/my-others/">其他</a><a href="https://jobs.51job.com/waimaoxiaoshou/">外贸销售</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/shengwuzhiyao/"><strong>生物/制药/医疗器械</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/shengwuzhiyaozp/">生物工程/生物制药</a><a href="https://jobs.51job.com/yiyaoxiaoshourenyuan/">医药销售人员</a><a href="https://jobs.51job.com/yiyaoyanfaguanli/">医药技术研发管理人员</a><a href="https://jobs.51job.com/yiyaoyanfa/">医药技术研发人员</a><a href="https://jobs.51job.com/linchuangyanjiu/">临床研究员</a><a href="https://jobs.51job.com/linchuangxietiao/">临床协调员</a><a href="https://jobs.51job.com/yaopinzhuce/">药品注册</a><a href="https://jobs.51job.com/yaopinshengchan/">药品生产/质量管理</a><a href="https://jobs.51job.com/yaopintuiguangjingli/">药品市场推广经理</a><a href="https://jobs.51job.com/yaopintuiguangzhuguan/">药品市场推广主管/专员</a><a href="https://jobs.51job.com/yiyaoxiaoshoujingli/">医药销售经理/主管</a><a href="https://jobs.51job.com/yiyaodaibiao/">医药代表</a><a href="https://jobs.51job.com/yiliaoqixietuiguang/">医疗器械市场推广</a><a href="https://jobs.51job.com/yiliaoqixiexiaoshou/">医疗器械销售代表</a><a href="https://jobs.51job.com/swzy-others/">其他</a><a href="https://jobs.51job.com/huaxuefenxi/">化学分析测试员</a><a href="https://jobs.51job.com/yiliaoqixiezhuce/">医疗器械注册</a><a href="https://jobs.51job.com/yiliaoqixieshengchan/">医疗器械生产/质量管理</a><a href="https://jobs.51job.com/yiliaoqixieweixiu/">医疗器械维修人员</a><a href="https://jobs.51job.com/yiyaozhaoshang/">医药招商</a><a href="https://jobs.51job.com/zhengfushiwu/">政府事务管理</a><a href="https://jobs.51job.com/zhaotoubiao/">招投标管理</a><a href="https://jobs.51job.com/linchuangshuju/">临床数据分析员</a><a href="https://jobs.51job.com/yiliaoqixieyanfa/">医疗器械研发</a><a href="https://jobs.51job.com/yiliaoqixiexiaoshoujingli/">医疗器械销售经理/主管</a><a href="https://jobs.51job.com/yiyaoxueshutuiguang/">医药学术推广</a><a href="https://jobs.51job.com/linchuangjiancha/">临床监查员</a><a href="https://jobs.51job.com/shijiyanfajingli/">试剂研发经理</a><a href="https://jobs.51job.com/shijiyanfagongchengshi/">试剂研发工程师</a><a href="https://jobs.51job.com/zhijiyanjiu/">制剂研究员</a><a href="https://jobs.51job.com/yaowufenxi/">药物分析研究员</a><a href="https://jobs.51job.com/yaoliyanjiu/">药理研究员</a><a href="https://jobs.51job.com/bingliyanjiu/">病理研究员</a><a href="https://jobs.51job.com/yaowuhecheng/">药物合成/有机合成研究员</a><a href="https://jobs.51job.com/xibaopeiyang/">细胞培养技术员</a><a href="https://jobs.51job.com/yaowujingrongjingli/">药物警戒经理</a><a href="https://jobs.51job.com/yaowujingrongzhuanyuan/">药物警戒专员</a><a href="https://jobs.51job.com/dongwushiyan/">动物实验技术员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/guanggao/"><strong>广告</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/guanggaokehuzongjian/">广告客户总监/副总监</a><a href="https://jobs.51job.com/guanggaokehujingli/">广告客户经理</a><a href="https://jobs.51job.com/guanggaokehuzhuguan/">广告客户主管/专员</a><a href="https://jobs.51job.com/guanggaochuangyi/">广告创意/设计经理</a><a href="https://jobs.51job.com/guanggaochuangyizongjian/">广告创意总监</a><a href="https://jobs.51job.com/shejizhuguan/">广告创意/设计主管/专员</a><a href="https://jobs.51job.com/wenancehua/">文案/策划</a><a href="https://jobs.51job.com/yewufazhanjingli/">企业/业务发展经理</a><a href="https://jobs.51job.com/qiyecehua/">企业策划人员</a><a href="https://jobs.51job.com/gg-others/">其他</a><a href="https://jobs.51job.com/meishuzhidao/">美术指导</a><a href="https://jobs.51job.com/guanggaozhixing/">广告制作执行</a><a href="https://jobs.51job.com/guanggaoxiaoshou/">广告销售</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/gongguanmeijie/"><strong>公关/媒介</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/gongguanjingli/">公关经理</a><a href="https://jobs.51job.com/gongguanzhuguan/">公关主管</a><a href="https://jobs.51job.com/gongguanzhuanyuan/">公关专员</a><a href="https://jobs.51job.com/huizhanjingli/">会务/会展经理</a><a href="https://jobs.51job.com/huizhanzhuguan/">会务/会展主管</a><a href="https://jobs.51job.com/huizhanzhuanyuan/">会务/会展专员</a><a href="https://jobs.51job.com/meijiejingli/">媒介经理</a><a href="https://jobs.51job.com/meijiezhuguan/">媒介主管</a><a href="https://jobs.51job.com/meijiezhuanyuan/">媒介专员</a><a href="https://jobs.51job.com/meijiezhuli/">公关/媒介助理</a><a href="https://jobs.51job.com/gsmj-others/">其他</a><a href="https://jobs.51job.com/meijiexiaoshou/">媒介销售</a><a href="https://jobs.51job.com/huodongcehua/">活动策划</a><a href="https://jobs.51job.com/huodongzhixing/">活动执行</a><a href="https://jobs.51job.com/gongguanzongjian/">公关总监</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yingshimeiti/"><strong>影视/媒体</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/yingshicehua/">影视策划/制作人员</a><a href="https://jobs.51job.com/daoyanbiandao/">导演/编导</a><a href="https://jobs.51job.com/yishuzongjian/">艺术/设计总监</a><a href="https://jobs.51job.com/jingjiren/">经纪人/星探</a><a href="https://jobs.51job.com/zhubozhuchiren/">主播/主持人</a><a href="https://jobs.51job.com/sheyingshi/">摄影师/摄像师</a><a href="https://jobs.51job.com/yinxiaoshi/">音效师</a><a href="https://jobs.51job.com/peiyinyuan/">配音员</a><a href="https://jobs.51job.com/ysmt-others/">其他</a><a href="https://jobs.51job.com/houqizhizuo/">后期制作</a><a href="https://jobs.51job.com/fangyingjingli/">放映经理/主管</a><a href="https://jobs.51job.com/fangyingyuan/">放映员</a><a href="https://jobs.51job.com/yishuzhidao/">艺术指导/舞台美术设计</a><a href="https://jobs.51job.com/dengguangshi/">灯光师</a><a href="https://jobs.51job.com/shipinjianji/">视频剪辑</a><a href="https://jobs.51job.com/bianju/">编剧</a><a href="https://jobs.51job.com/zhipianren/">制片人</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/bianjichuban/"><strong>编辑出版</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/zongbian/">总编/副总编</a><a href="https://jobs.51job.com/bianji/">编辑</a><a href="https://jobs.51job.com/jizhe/">记者</a><a href="https://jobs.51job.com/meishubianji/">美术编辑</a><a href="https://jobs.51job.com/paibansheji/">排版设计</a><a href="https://jobs.51job.com/chubanfaxing/">出版/发行</a><a href="https://jobs.51job.com/xzcb-others/">其他</a><a href="https://jobs.51job.com/dianhuacaibian/">电话采编</a><a href="https://jobs.51job.com/zhuangaoren/">作家/撰稿人</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/fangdichankaifa/"><strong>房地产开发</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/fangdichancehuajingli/">房地产项目/策划经理</a><a href="https://jobs.51job.com/fangdichancehuazhuanyuan/">房地产项目/策划主管/专员</a><a href="https://jobs.51job.com/fangchanpeitao/">房产项目配套工程师</a><a href="https://jobs.51job.com/fangdichantouziguanli/">房地产投资管理</a><a href="https://jobs.51job.com/fdc-others/">其他</a><a href="https://jobs.51job.com/fangdichanzhaotoubiao/">房地产项目招投标</a><a href="https://jobs.51job.com/fangdichantouzifenxi/">房地产投资分析</a><a href="https://jobs.51job.com/fangdichanzichanguanli/">房地产资产管理</a><a href="https://jobs.51job.com/jiancharenyuan/">监察人员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/wuyeguanlishangyexiezilou/"><strong>物业管理</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/gaojiwuyeguwen/">高级物业顾问/物业顾问</a><a href="https://jobs.51job.com/wuyeguanlijingli/">物业管理经理</a><a href="https://jobs.51job.com/wuyeguanlizhuli/">物业管理专员/助理</a><a href="https://jobs.51job.com/xiezilouzhaoshang/">招商/租赁/租售</a><a href="https://jobs.51job.com/wuyesheshiguanli/">物业设施管理人员</a><a href="https://jobs.51job.com/wuyeweixiu/">物业维修员</a><a href="https://jobs.51job.com/wygl-others/">其他</a><a href="https://jobs.51job.com/wuyejidian/">物业机电工程师</a><a href="https://jobs.51job.com/tingcheguanli/">停车管理员</a><a href="https://jobs.51job.com/baoanjingli/">保安经理</a><a href="https://jobs.51job.com/baoanrenyuan/">保安人员</a><a href="https://jobs.51job.com/baojie/">保洁</a><a href="https://jobs.51job.com/lvhuagong/">绿化工</a><a href="https://jobs.51job.com/wuyeguanlizhuguan/">物业管理主管</a><a href="https://jobs.51job.com/wuyejidianweixiu/">物业机电维修工</a><a href="https://jobs.51job.com/qianjiegongchengshi/">前介工程师</a><a href="https://jobs.51job.com/changzugongyu/">长租公寓管家/养老专员</a><a href="https://jobs.51job.com/xiezilouyunying/">写字楼运营</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/canyinfuwu/"><strong>餐饮服务</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/canyindianzhangjingli/">餐饮店长/经理</a><a href="https://jobs.51job.com/cantinglingban/">餐厅领班</a><a href="https://jobs.51job.com/canyinfuwuyuan/">餐饮服务员</a><a href="https://jobs.51job.com/liyi/">礼仪/迎宾</a><a href="https://jobs.51job.com/xingzhengzhuchu/">行政主厨/厨师长</a><a href="https://jobs.51job.com/zhongcanchushi/">中餐厨师</a><a href="https://jobs.51job.com/diaojiushi/">调酒师/侍酒师/吧台员</a><a href="https://jobs.51job.com/chayishi/">茶艺师</a><a href="https://jobs.51job.com/cyyl-others/">其他</a><a href="https://jobs.51job.com/chuancaizhuguan/">传菜主管</a><a href="https://jobs.51job.com/chushizhuli/">厨师助理/学徒</a><a href="https://jobs.51job.com/peicai/">配菜/打荷</a><a href="https://jobs.51job.com/xiwangong/">洗碗工</a><a href="https://jobs.51job.com/songcanyuan/">送餐员</a><a href="https://jobs.51job.com/kafeishi/">咖啡师</a><a href="https://jobs.51job.com/zagong/">杂工</a><a href="https://jobs.51job.com/canyinshouyinyuan/">餐饮收银员</a><a href="https://jobs.51job.com/canyindatangjinglizp/">餐饮大堂经理</a><a href="https://jobs.51job.com/xicanchushi/">西餐厨师</a><a href="https://jobs.51job.com/rishichushi/">日式厨师</a><a href="https://jobs.51job.com/miandianshi/">面点师</a><a href="https://jobs.51job.com/xidianshizp/">西点师</a><a href="https://jobs.51job.com/canyinyudingyuan/">餐饮预订员</a><a href="https://jobs.51job.com/chuancaiyuan/">传菜员</a><a href="https://jobs.51job.com/tiaoyinshi/">调饮师</a><a href="https://jobs.51job.com/shipinanquan/">食品安全管理师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jiudianlvyou/"><strong>酒店旅游</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/binguanjingli/">酒店/宾馆经理</a><a href="https://jobs.51job.com/jiudianxiaoshou/">酒店/宾馆销售</a><a href="https://jobs.51job.com/jiudiandatangjingli/">酒店大堂经理</a><a href="https://jobs.51job.com/loumianjingli/">楼面经理</a><a href="https://jobs.51job.com/jiudianqiantai/">酒店前台</a><a href="https://jobs.51job.com/kefangfuwu/">客房服务员/楼面服务员</a><a href="https://jobs.51job.com/xingliyuan/">行李员</a><a href="https://jobs.51job.com/qingjiefuwu/">清洁服务人员</a><a href="https://jobs.51job.com/daoyou/">导游/旅行顾问</a><a href="https://jobs.51job.com/piaowu/">票务</a><a href="https://jobs.51job.com/jdly-others/">其他</a><a href="https://jobs.51job.com/yanhuiguanli/">宴会管理</a><a href="https://jobs.51job.com/jichangdaibiao/">机场代表</a><a href="https://jobs.51job.com/guanjiabujingli/">管家部经理/主管</a><a href="https://jobs.51job.com/binkefuwujingli/">宾客服务经理</a><a href="https://jobs.51job.com/yudingzhuguan/">预订主管</a><a href="https://jobs.51job.com/yudingyuanzp/">预订员</a><a href="https://jobs.51job.com/jianshenfuwu/">健身房服务</a><a href="https://jobs.51job.com/lvyouchanpinxiaoshou/">旅游产品销售</a><a href="https://jobs.51job.com/xingchengguanli/">行程管理/计调</a><a href="https://jobs.51job.com/qianzhengzhuanyuan/">签证专员</a><a href="https://jobs.51job.com/yanxuexiangmu/">研学项目主管/经理</a><a href="https://jobs.51job.com/lvyoucehua/">旅游策划师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/meirongbaojian/"><strong>美容保健</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/meirongguwen/">美容顾问</a><a href="https://jobs.51job.com/meirongzhuli/">美容助理</a><a href="https://jobs.51job.com/shoushenguwen/">瘦身顾问</a><a href="https://jobs.51job.com/faxingshi/">发型师</a><a href="https://jobs.51job.com/faxingzhuli/">发型助理/学徒</a><a href="https://jobs.51job.com/meijiashi/">美甲师</a><a href="https://jobs.51job.com/anmo/">按摩</a><a href="https://jobs.51job.com/chongwuhuli/">宠物护理/美容</a><a href="https://jobs.51job.com/mrjs-others/">其他</a><a href="https://jobs.51job.com/caizhuangpeixunshi/">彩妆培训师</a><a href="https://jobs.51job.com/caizhuangguwen/">专柜彩妆顾问(BA)</a><a href="https://jobs.51job.com/meirongpeixunshi/">美容培训师/导师</a><a href="https://jobs.51job.com/meitishi/">美体师</a><a href="https://jobs.51job.com/meirongdianzhang/">美容店长</a><a href="https://jobs.51job.com/meirongshi/">美容师</a><a href="https://jobs.51job.com/huazhuangshi/">化妆师</a><a href="https://jobs.51job.com/zaoxingshi/">造型师</a><a href="https://jobs.51job.com/meifadianzhang/">美发店长</a><a href="https://jobs.51job.com/spajishi/">SPA 技师</a><a href="https://jobs.51job.com/zuliao/">足疗</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/baihuolingshou/"><strong>百货零售</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/mendianjingli/">门店经理/店长</a><a href="https://jobs.51job.com/yingyeyuan/">店员/营业员</a><a href="https://jobs.51job.com/shouyinzhuguan/">收银主管</a><a href="https://jobs.51job.com/chenlieyuan/">陈列员</a><a href="https://jobs.51job.com/cuxiaoyuandaogouyuan/">促销员/导购员</a><a href="https://jobs.51job.com/jianzhidianyuan/">兼职店员</a><a href="https://jobs.51job.com/bhls-others/">其他</a><a href="https://jobs.51job.com/fangsunyuan/">防损员/内保</a><a href="https://jobs.51job.com/xidianshi/">西点师/面包糕点加工</a><a href="https://jobs.51job.com/shengxianjiagong/">生鲜食品加工/处理</a><a href="https://jobs.51job.com/shushijiagong/">熟食加工</a><a href="https://jobs.51job.com/pinleiguanli/">品类管理</a><a href="https://jobs.51job.com/anfangzhuguan/">安防主管</a><a href="https://jobs.51job.com/liansuozhaoshang/">品牌/连锁招商管理</a><a href="https://jobs.51job.com/shechipinyewu/">奢侈品业务</a><a href="https://jobs.51job.com/zhubaoxiaoshou/">珠宝销售顾问</a><a href="https://jobs.51job.com/xundian/">促销主管/督导/巡店</a><a href="https://jobs.51job.com/shouyinyuanzp/">收银员</a><a href="https://jobs.51job.com/shouhuoyuan/">收货员</a><a href="https://jobs.51job.com/lihuoyuanzp/">理货员</a><a href="https://jobs.51job.com/dianzhangzhuli/">店长助理</a><a href="https://jobs.51job.com/daogouguanli/">导购管理</a><a href="https://jobs.51job.com/chenlieguanli/">陈列管理</a><a href="https://jobs.51job.com/shangpinguanli/">商品管理</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jiazhengbaojie/"><strong>家政保洁</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/baobiao/">保镖</a><a href="https://jobs.51job.com/xunhuyuan/">寻呼员/话务员</a><a href="https://jobs.51job.com/qingjiegong/">清洁工</a><a href="https://jobs.51job.com/jiazhengfuwu/">家政服务/保姆</a><a href="https://jobs.51job.com/jzba-others/">其他</a><a href="https://jobs.51job.com/yuesao/">月嫂</a><a href="https://jobs.51job.com/yuyingshi/">育婴师/保育员</a><a href="https://jobs.51job.com/hugong/">护工</a><a href="https://jobs.51job.com/zhongdiangong/">钟点工</a><a href="https://jobs.51job.com/xiyigong/">洗衣工</a><a href="https://jobs.51job.com/songshuigong/">送水工</a><a href="https://jobs.51job.com/kongdiaoweixiu/">空调维修</a><a href="https://jobs.51job.com/jiadianweixiu/">家电维修</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jianzhi/"><strong>兼职</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jianzhizp/">兼职</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/qichezhizao/"><strong>汽车制造</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/qichezhiliang/">汽车质量工程师</a><a href="https://jobs.51job.com/qichezhuangpei/">汽车装配工艺工程师</a><a href="https://jobs.51job.com/qczz-others/">其他</a><a href="https://jobs.51job.com/gongyingshangzhilianggongchengshi/">供应商质量工程师</a><a href="https://jobs.51job.com/qianqizhilianggongchengshi/">前期质量工程师</a><a href="https://jobs.51job.com/guochengzhilianggongchengshi/">过程质量工程师</a><a href="https://jobs.51job.com/kehuzhilianggongchengshi/">客户质量工程师</a><a href="https://jobs.51job.com/zongzhanggongchengshi/">总装工程师</a><a href="https://jobs.51job.com/hanjiegongyigongchengshi/">焊接工艺工程师</a><a href="https://jobs.51job.com/chongyagongyigongchengshi/">冲压工艺工程师</a><a href="https://jobs.51job.com/tuzhuanggongyigongchengshi/">涂装工艺工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/huagong/"><strong>化工</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/huagongjishu/">化工技术应用/化工工程师</a><a href="https://jobs.51job.com/huagongyanjiu/">化工实验室研究员/技术员</a><a href="https://jobs.51job.com/tuliaoyanfa/">涂料研发工程师</a><a href="https://jobs.51job.com/peisejishuyuan/">配色技术员</a><a href="https://jobs.51job.com/suliaogongchengshi/">塑料工程师</a><a href="https://jobs.51job.com/huazhuangpinyanfa/">化妆品研发</a><a href="https://jobs.51job.com/shipinyinliaoyanfa/">食品/饮料研发</a><a href="https://jobs.51job.com/hg-others/">其他</a><a href="https://jobs.51job.com/zaozhiyanfa/">造纸研发</a><a href="https://jobs.51job.com/jiutishejishi/">酒体设计师</a><a href="https://jobs.51job.com/youjihecheng/">有机合成研究员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/huanbao/"><strong>环保</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/huanbaozp/">环保工程师</a><a href="https://jobs.51job.com/shuichuli/">水处理工程师</a><a href="https://jobs.51job.com/hb-others/">其他</a><a href="https://jobs.51job.com/huanjingyingxiang/">环境影响评价工程师</a><a href="https://jobs.51job.com/huanbaojiance/">环保检测</a><a href="https://jobs.51job.com/shuizhijianceyuan/">水质检测员</a><a href="https://jobs.51job.com/gufeigongchengshi/">固废工程师</a><a href="https://jobs.51job.com/feiqichuli/">废气处理工程师</a><a href="https://jobs.51job.com/shengtaizhili/">生态治理/规划</a><a href="https://jobs.51job.com/tanpaifangguanli/">碳排放管理员</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/peixun/"><strong>培训</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/peixundudao/">培训督导</a><a href="https://jobs.51job.com/peixunjiangshi/">培训讲师</a><a href="https://jobs.51job.com/peixuncehua/">培训策划</a><a href="https://jobs.51job.com/peixunzhuli/">培训助理</a><a href="https://jobs.51job.com/px-others/">其他</a><a href="https://jobs.51job.com/peixunchanpin/">培训产品开发</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/nonglinmuyu/"><strong>农/林/牧/渔</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/yangzhizhuguan/">养殖部主管</a><a href="https://jobs.51job.com/changzhang/">场长(农/林/牧/渔业)</a><a href="https://jobs.51job.com/nongyishi/">农艺师</a><a href="https://jobs.51job.com/xumushi/">畜牧师</a><a href="https://jobs.51job.com/siyangyuan/">饲养员</a><a href="https://jobs.51job.com/dongwuyingyang/">动物营养/饲料研发</a><a href="https://jobs.51job.com/nlmy-others/">其他</a><a href="https://jobs.51job.com/nongyejishuyuan/">农业技术员</a><a href="https://jobs.51job.com/xunshoushi/">驯兽师/助理驯兽师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/qichexiaoshou/"><strong>汽车销售与服务</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/4sdianjingli/">4S店经理/维修站经理</a><a href="https://jobs.51job.com/shouhoufuwu/">售后服务/客户服务</a><a href="https://jobs.51job.com/qichexiaoshouzp/">汽车销售/经纪人</a><a href="https://jobs.51job.com/2shouchepinggu/">二手车评估师</a><a href="https://jobs.51job.com/qichejianyan/">汽车检验/检测</a><a href="https://jobs.51job.com/qichezhuangshi/">汽车装饰美容</a><a href="https://jobs.51job.com/qichexiuligong/">汽车修理工</a><a href="https://jobs.51job.com/xichegong/">洗车工</a><a href="https://jobs.51job.com/jiayouzhan/">加油站工作员</a><a href="https://jobs.51job.com/qcxs-others/">其他</a><a href="https://jobs.51job.com/qichediangong/">汽车电工</a><a href="https://jobs.51job.com/qichebanjin/">汽车钣金</a><a href="https://jobs.51job.com/qichepenqi/">汽车喷漆</a><a href="https://jobs.51job.com/chexiandingsun/">车险定损/理赔</a><a href="https://jobs.51job.com/qichejinrongxiaoshou/">汽车金融销售</a><a href="https://jobs.51job.com/qichejinrongzhuanyuan/">汽车金融专员</a><a href="https://jobs.51job.com/qichejinrongjingli/">汽车金融经理</a><a href="https://jobs.51job.com/ershouchejingjiren/">二手车经纪人</a><a href="https://jobs.51job.com/qichejiuyuan/">汽车救援员</a><a href="https://jobs.51job.com/qichefuwuguwen/">汽车服务顾问</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/fangdichanxiaoshou/"><strong>房地产销售与中介</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/fangchanzhongjie/">房地产中介/置业顾问</a><a href="https://jobs.51job.com/fangdichanpinggu/">房地产评估</a><a href="https://jobs.51job.com/fangdichandianzhang/">房地产店长/经理</a><a href="https://jobs.51job.com/fangdichankefu/">房地产客服</a><a href="https://jobs.51job.com/fangchanneiqin/">房地产内勤</a><a href="https://jobs.51job.com/fczj-others/">其他</a><a href="https://jobs.51job.com/fangchanxiaoshoujingli/">房地产销售经理/主管</a><a href="https://jobs.51job.com/fangchanxiaoshou/">房地产销售</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/dianzishangwu/"><strong>电子商务</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/wangdiandianzhang/">网店店长</a><a href="https://jobs.51job.com/wangdianyunying/">电商运营</a><a href="https://jobs.51job.com/wangdianguanli/">网店店铺管理员</a><a href="https://jobs.51job.com/wangdiankefu/">网店客服</a><a href="https://jobs.51job.com/dianputuiguang/">店铺推广</a><a href="https://jobs.51job.com/wangdianmote/">网店模特</a><a href="https://jobs.51job.com/wdtb-others/">其他</a><a href="https://jobs.51job.com/dianzishangwuzhuanyuan/">电商专员</a><a href="https://jobs.51job.com/dianzishangwujingli/">电商经理/电商主管</a><a href="https://jobs.51job.com/dianzishangwuzongjian/">电商总监</a><a href="https://jobs.51job.com/kuajingdianshangyunying/">跨境电商运营</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jixiejichuang/"><strong>机械机床</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/shukongcaoji/">数控操机</a><a href="https://jobs.51job.com/shukongbiancheng/">数控编程</a><a href="https://jobs.51job.com/jixiugongzp/">机修工</a><a href="https://jobs.51job.com/zhewangong/">折弯工</a><a href="https://jobs.51job.com/chegong/">车工</a><a href="https://jobs.51job.com/mogong/">磨工</a><a href="https://jobs.51job.com/xigong/">铣工</a><a href="https://jobs.51job.com/chongyagong/">冲压工</a><a href="https://jobs.51job.com/paogong/">刨工</a><a href="https://jobs.51job.com/qiangong/">钳工</a><a href="https://jobs.51job.com/zuangong/">钻工</a><a href="https://jobs.51job.com/tanggongzp/">镗工</a><a href="https://jobs.51job.com/maogong/">铆工</a><a href="https://jobs.51job.com/banjingong/">钣金工</a><a href="https://jobs.51job.com/paoguanggong/">抛光工</a><a href="https://jobs.51job.com/qiegejigong/">切割技工</a><a href="https://jobs.51job.com/mojugong/">模具工</a><a href="https://jobs.51job.com/lianjiaogong/">炼胶工</a><a href="https://jobs.51job.com/liuhuagong/">硫化工</a><a href="https://jobs.51job.com/chuimogong/">吹膜工</a><a href="https://jobs.51job.com/zhusugong/">注塑工</a><a href="https://jobs.51job.com/jxjc-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yinshuabaozhuang/"><strong>印刷包装</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/yinshuagong/">印刷工</a><a href="https://jobs.51job.com/xiaoduiluru/">校对/录入</a><a href="https://jobs.51job.com/tiaoseyuan/">调色员</a><a href="https://jobs.51job.com/tangjingong/">烫金工</a><a href="https://jobs.51job.com/shaibanpinban/">晒版员</a><a href="https://jobs.51job.com/yinshuapaiban/">印刷排版/制版</a><a href="https://jobs.51job.com/zhuangdinggong/">装订工</a><a href="https://jobs.51job.com/yinshuajizhang/">印刷机械机长</a><a href="https://jobs.51job.com/shumazhiyin/">数码直印/菲林输出</a><a href="https://jobs.51job.com/tiaomojishi/">调墨技师</a><a href="https://jobs.51job.com/dianfen/">电分操作员</a><a href="https://jobs.51job.com/dagaojicaozuo/">打稿机操作员</a><a href="https://jobs.51job.com/qiezhijicaozuo/">切纸机操作工</a><a href="https://jobs.51job.com/biaojiaogong/">裱胶工</a><a href="https://jobs.51job.com/yahengong/">压痕工</a><a href="https://jobs.51job.com/fujuangong/">复卷工</a><a href="https://jobs.51job.com/ysbz-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yundongjianshen/"><strong>运动健身</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jianshenguwen/">健身顾问/教练</a><a href="https://jobs.51job.com/yujialaoshi/">瑜伽老师</a><a href="https://jobs.51job.com/wudaolaoshi/">舞蹈老师</a><a href="https://jobs.51job.com/youyongjiaolian/">游泳教练</a><a href="https://jobs.51job.com/jiushengyuan/">救生员</a><a href="https://jobs.51job.com/gaoerfujiaolian/">高尔夫教练</a><a href="https://jobs.51job.com/tiyujiaolian/">体育运动教练</a><a href="https://jobs.51job.com/ydjs-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/xiuxianyule/"><strong>休闲娱乐</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/siyi/">司仪</a><a href="https://jobs.51job.com/qingdiancehua/">婚礼/庆典策划服务</a><a href="https://jobs.51job.com/dj/">DJ</a><a href="https://jobs.51job.com/zhuchang/">驻唱/歌手</a><a href="https://jobs.51job.com/wudaoyanyuan/">舞蹈演员</a><a href="https://jobs.51job.com/mote/">模特</a><a href="https://jobs.51job.com/yanyuan/">演员/群众演员</a><a href="https://jobs.51job.com/xxyl-others/">其他</a><a href="https://jobs.51job.com/yulelingban/">娱乐领班</a><a href="https://jobs.51job.com/yulefuwuyuan/">娱乐服务员</a><a href="https://jobs.51job.com/qiantaiyingbin/">前台迎宾</a><a href="https://jobs.51job.com/wangluozhubo/">网络主播</a><a href="https://jobs.51job.com/zhubozhuli/">主播助理</a><a href="https://jobs.51job.com/daihuozhubo/">带货主播</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/chanpin/"><strong>产品</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/chanpinzhuanyuan/">产品专员</a><a href="https://jobs.51job.com/chanpinjingli/">产品经理/主管</a><a href="https://jobs.51job.com/chanpinzhuli/">产品助理</a><a href="https://jobs.51job.com/chanpinzongjian/">产品总监</a><a href="https://jobs.51job.com/hulianwangchanpinjingli/">互联网产品经理</a><a href="https://jobs.51job.com/yidongchanpinjingli/">移动产品经理</a><a href="https://jobs.51job.com/yonghuchanpinjingli/">用户产品经理</a><a href="https://jobs.51job.com/dianshangchanpinjingli/">电商产品经理</a><a href="https://jobs.51job.com/xuqiugongchengshi/">需求工程师</a><a href="https://jobs.51job.com/chanpin-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/bandaoti-xinpian/"><strong>半导体/芯片</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jichengdianlu/">集成电路IC设计/应用工程师</a><a href="https://jobs.51job.com/ic-yanzheng/">IC验证工程师</a><a href="https://jobs.51job.com/bandaotijishu/">半导体技术</a><a href="https://jobs.51job.com/fae-xianchangyingyong/">FAE 现场应用工程师</a><a href="https://jobs.51job.com/bantusheji/">版图设计工程师</a><a href="https://jobs.51job.com/gongyigongchengshi/">半导体工艺工程师</a><a href="https://jobs.51job.com/xinpianjiagou/">芯片架构工程师</a><a href="https://jobs.51job.com/fpga-kaifa/">FPGA开发工程师</a><a href="https://jobs.51job.com/mems/">MEMS工程师</a><a href="https://jobs.51job.com/shepinxinpiansheji/">射频芯片设计</a><a href="https://jobs.51job.com/monixinpian/">模拟芯片工程师</a><a href="https://jobs.51job.com/monibantu/">模拟版图工程师</a><a href="https://jobs.51job.com/shuziqianduan/">数字前端工程师</a><a href="https://jobs.51job.com/fpga-yuanxingyanzheng/">FPGA原型验证工程师</a><a href="https://jobs.51job.com/eda/">EDA工程师</a><a href="https://jobs.51job.com/keceshixingsheji/">可测性设计工程师(DFT)</a><a href="https://jobs.51job.com/shuzihouduan/">数字后端工程师</a><a href="https://jobs.51job.com/xinpianceshi/">芯片测试工程师</a><a href="https://jobs.51job.com/bandaotishebei/">半导体设备工程师</a><a href="https://jobs.51job.com/gongyizhenghe/">工艺整合工程师(PIE)</a><a href="https://jobs.51job.com/shixiaofenxi/">失效分析工程师(FA)</a><a href="https://jobs.51job.com/fengzhuangyanfa/">封装研发工程师</a><a href="https://jobs.51job.com/xinpianxiaoshou/">芯片销售工程师</a><a href="https://jobs.51job.com/bandaotiwendang/">半导体文档工程师</a><a href="https://jobs.51job.com/bandaotichanpinjingli/">半导体产品经理/产品工程师</a><a href="https://jobs.51job.com/ic-others/">其他</a><a href="https://jobs.51job.com/bandaoticeshi/">半导体测试工程师</a><a href="https://jobs.51job.com/fengzhuang/">封装工程师</a><a href="https://jobs.51job.com/bandaotiqijian/">半导体器件工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jianzhuguihuayusheji/"><strong>建筑规划与设计</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/shineisheji/">室内设计</a><a href="https://jobs.51job.com/ruanzhuangsheji/">软装设计</a><a href="https://jobs.51job.com/jingzhuangsheji/">精装设计</a><a href="https://jobs.51job.com/guihuasheji/">规划与设计</a><a href="https://jobs.51job.com/jianzhusheji/">建筑设计师</a><a href="https://jobs.51job.com/gangjiegousheji/">钢结构设计</a><a href="https://jobs.51job.com/muqiangsheji/">幕墙设计</a><a href="https://jobs.51job.com/jianzhujiegosheji/">建筑结构设计</a><a href="https://jobs.51job.com/jianzhuzhitu/">建筑制图/模型/渲染</a><a href="https://jobs.51job.com/jianzhujidiansheji/">建筑机电设计</a><a href="https://jobs.51job.com/nuantongsheji/">暖通设计</a><a href="https://jobs.51job.com/jipaishuisheji/">给排水设计</a><a href="https://jobs.51job.com/chengshiguihuasheji/">城市规划设计</a><a href="https://jobs.51job.com/yuanlinsheji/">园艺/园林/景观设计</a><a href="https://jobs.51job.com/jzghysj-others/">其他</a><a href="https://jobs.51job.com/bimgongchengshi/">BIM工程师</a><a href="https://jobs.51job.com/shineishejishizhuli/">室内设计师助理</a><a href="https://jobs.51job.com/shineishejijinglizhuguan/">室内设计经理/主管</a><a href="https://jobs.51job.com/shineishejizongjian/">室内设计总监</a><a href="https://jobs.51job.com/jiazhuangguwen/">家装顾问</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/qicheyanfasheji/"><strong>汽车研发设计</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/qichexiangmu/">汽车项目管理</a><a href="https://jobs.51job.com/qichesheji/">汽车设计工程师</a><a href="https://jobs.51job.com/cheshenzaoxingsheji/">车身/造型设计</a><a href="https://jobs.51job.com/qichejigou/">汽车结构工程师</a><a href="https://jobs.51job.com/neiwaishigongchengshi/">内外饰工程师</a><a href="https://jobs.51job.com/qichedianzi/">汽车电子工程师</a><a href="https://jobs.51job.com/dianqigongchengshi/">电气/电器工程师</a><a href="https://jobs.51job.com/fujianxitonggongchengshi/">附件系统工程师</a><a href="https://jobs.51job.com/donglizongchenggongchengshi/">动力总成工程师</a><a href="https://jobs.51job.com/fadongjigongchengshi/">发动机工程师</a><a href="https://jobs.51job.com/dipangongchengshi/">底盘工程师</a><a href="https://jobs.51job.com/qicheanquan/">汽车安全性能工程师</a><a href="https://jobs.51job.com/qicheshiyangongchengshi/">汽车试验工程师</a><a href="https://jobs.51job.com/xinnengyuandianchi/">新能源电池工程师</a><a href="https://jobs.51job.com/xinnengyuandiankong/">新能源电控工程师</a><a href="https://jobs.51job.com/xinnengyuandianji/">新能源电机工程师</a><a href="https://jobs.51job.com/qichebiaodinggongchengshi/">汽车标定工程师</a><a href="https://jobs.51job.com/fadongjipipeigongchengshi/">发动机匹配工程师</a><a href="https://jobs.51job.com/chelianwanggongchengshi/">车联网工程师</a><a href="https://jobs.51job.com/zhinengjiashigongchengshi/">智能驾驶工程师</a><a href="https://jobs.51job.com/yanfazongjian/">研发总监/部长/专家</a><a href="https://jobs.51job.com/qcyf-others/">其他</a><a href="https://jobs.51job.com/wurenjiashiceshi/">智能驾驶测试工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/qianduankaifa/"><strong>前端开发</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/webqianduankaifa/">Web前端开发</a><a href="https://jobs.51job.com/html5kaifa/">HTML5开发工程师</a><a href="https://jobs.51job.com/qdkf-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/rengongzhineng/"><strong>人工智能</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/jiqixuexi/">机器学习工程师</a><a href="https://jobs.51job.com/shengduxuexi/">深度学习工程师</a><a href="https://jobs.51job.com/tuxiangsuanfa/">图像算法工程师</a><a href="https://jobs.51job.com/tuxiangchuli/">图像处理工程师</a><a href="https://jobs.51job.com/tuxiangshibie/">图像识别工程师</a><a href="https://jobs.51job.com/yuyinshibie/">语音识别工程师</a><a href="https://jobs.51job.com/jiqishijue/">机器视觉工程师</a><a href="https://jobs.51job.com/ziranyuyanchuli/">自然语言处理(NLP)</a><a href="https://jobs.51job.com/suanfagongchengshi/">算法工程师</a><a href="https://jobs.51job.com/tuijiansuanfa/">推荐算法工程师</a><a href="https://jobs.51job.com/sousuosuanfa/">搜索算法工程师</a><a href="https://jobs.51job.com/rgzn-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/shijuejiaohusheji/"><strong>视觉/交互设计</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/wangyeshejishi/">网页设计师</a><a href="https://jobs.51job.com/jiaohushejishi/">交互设计师</a><a href="https://jobs.51job.com/shijueshejishi/">视觉设计师</a><a href="https://jobs.51job.com/yonghutiyansheji/">用户体验（UE/UX）设计师</a><a href="https://jobs.51job.com/wangzhanjiagousheji/">网站架构设计师</a><a href="https://jobs.51job.com/flashsheji/">Flash设计师</a><a href="https://jobs.51job.com/texiaoshejishi/">特效设计师</a><a href="https://jobs.51job.com/yinxiaoshejishi/">音效设计师</a><a href="https://jobs.51job.com/jisuanjifuzhusheji/">计算机辅助设计工程师</a><a href="https://jobs.51job.com/fangzhenyingyong/">仿真应用工程师</a><a href="https://jobs.51job.com/sheji-others/">其他</a><a href="https://jobs.51job.com/uishejishi/">UI设计师</a><a href="https://jobs.51job.com/pingmiansheji/">平面设计师</a><a href="https://jobs.51job.com/duomeitisheji/">多媒体设计</a><a href="https://jobs.51job.com/huihua/">绘画</a><a href="https://jobs.51job.com/yuanhuashi/">原画师</a><a href="https://jobs.51job.com/meigongdianshangshejishi/">美工/电商设计师</a><a href="https://jobs.51job.com/pingmianshejizongjian/">平面设计总监</a><a href="https://jobs.51job.com/pingmianshejijingli/">平面设计经理/主管</a><a href="https://jobs.51job.com/3dsheji/">动画/3D设计</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/shuju/"><strong>数据</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/shujufenxishi/">数据分析师</a><a href="https://jobs.51job.com/shujufenxijingli/">数据分析经理/主管</a><a href="https://jobs.51job.com/etlkaifa/">ETL开发工程师</a><a href="https://jobs.51job.com/bigongchengshi/">BI工程师</a><a href="https://jobs.51job.com/shujucangku/">数据仓库工程师</a><a href="https://jobs.51job.com/shujucaiji/">数据采集工程师</a><a href="https://jobs.51job.com/shujujianmo/">数据建模工程师</a><a href="https://jobs.51job.com/shujuzhili/">数据治理工程师</a><a href="https://jobs.51job.com/shuju-others/">其他</a><a href="https://jobs.51job.com/dianzishujuquzheng/">电子数据取证分析师</a><a href="https://jobs.51job.com/mimajishu/">密码技术应用员</a><a href="https://jobs.51job.com/shujubiaozhushi/">数据标注师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yidongkaifa/"><strong>移动开发</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/androidkaifa/">Android开发工程师</a><a href="https://jobs.51job.com/ioskaifa/">iOS开发工程师</a><a href="https://jobs.51job.com/yidongkaifagongchengshi/">移动开发工程师</a><a href="https://jobs.51job.com/hdkf-others/">其他</a><a href="https://jobs.51job.com/xiaochengxukaifagongchengshi/">小程序开发工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/youxi/"><strong>游戏</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/youxicehua/">游戏策划师</a><a href="https://jobs.51job.com/youxixitongcehua/">游戏系统策划</a><a href="https://jobs.51job.com/youxishuzhicehua/">游戏数值策划</a><a href="https://jobs.51job.com/youxiguanqiacehua/">游戏关卡策划</a><a href="https://jobs.51job.com/youxiwenanjuqingcehua/">游戏文案策划/剧情策划</a><a href="https://jobs.51job.com/youxijiemian/">游戏界面设计师</a><a href="https://jobs.51job.com/youxiyuanhuashi/">游戏原画师</a><a href="https://jobs.51job.com/youxidonghuashi/">游戏动画师</a><a href="https://jobs.51job.com/youxikaifa/">游戏开发工程师</a><a href="https://jobs.51job.com/Cocos2d-xkaifa/">Cocos2d-x开发工程师</a><a href="https://jobs.51job.com/Unity3dkaifa/">Unity3d开发工程师</a><a href="https://jobs.51job.com/youxikehuduankaifa/">游戏客户端开发工程师</a><a href="https://jobs.51job.com/youxifuwuduankaifa/">游戏服务端开发工程师</a><a href="https://jobs.51job.com/youxiyunying/">游戏运营</a><a href="https://jobs.51job.com/dianzijingjiyunying/">电子竞技运营</a><a href="https://jobs.51job.com/youxi-others/">其他</a><a href="https://jobs.51job.com/youxitexiaosheji/">游戏特效设计师</a><a href="https://jobs.51job.com/youxidongzuosheji/">游戏动作设计师</a><a href="https://jobs.51job.com/youxichangjingsheji/">游戏场景设计师</a><a href="https://jobs.51job.com/youxijuesesheji/">游戏角色设计师</a><a href="https://jobs.51job.com/youxiceshi/">游戏测试</a><a href="https://jobs.51job.com/ue4texiaoshi/">UE4特效师</a><a href="https://jobs.51job.com/ue4kaifa/">UE4开发工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yunweijishuzhichi/"><strong>运维/技术支持</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/yunweigongchengshi/">运维工程师</a><a href="https://jobs.51job.com/xitong/">系统工程师</a><a href="https://jobs.51job.com/shujukugongchengshi/">数据库工程师(DBA)</a><a href="https://jobs.51job.com/xitongjicheng/">系统集成工程师</a><a href="https://jobs.51job.com/erp-shishi/">ERP实施顾问</a><a href="https://jobs.51job.com/wangluoanquan/">网络安全工程师</a><a href="https://jobs.51job.com/wangzhanweihu/">网站维护工程师</a><a href="https://jobs.51job.com/weihujingli/">技术支持/维护经理</a><a href="https://jobs.51job.com/weihugongchengshi/">技术支持/维护工程师</a><a href="https://jobs.51job.com/peizhiguanli/">配置管理工程师</a><a href="https://jobs.51job.com/xinxijishujingli/">IT经理/IT主管</a><a href="https://jobs.51job.com/wangluogongchengshi/">网络工程师(IT工程师)</a><a href="https://jobs.51job.com/wangluoguanli/">网络管理(Helpdesk)</a><a href="https://jobs.51job.com/yunweikaifa/">运维开发</a><a href="https://jobs.51job.com/wangluoweixiu/">网络维修</a><a href="https://jobs.51job.com/shoujiweixiu/">手机维修</a><a href="https://jobs.51job.com/diannaoweixiu/">电脑维修</a><a href="https://jobs.51job.com/yunwei-others/">其他</a><a href="https://jobs.51job.com/zidonghuayunwei/">自动化运维工程师</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/yunying/"><strong>运营</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/wangzhanyunyingjingli/">网站运营经理/主管</a><a href="https://jobs.51job.com/wangzhancehua/">网站策划</a><a href="https://jobs.51job.com/wangzhanbianji/">网站编辑</a><a href="https://jobs.51job.com/xinmeitiyunying/">新媒体运营</a><a href="https://jobs.51job.com/yunying-others/">其他</a><a href="https://jobs.51job.com/wangzhanyunying/">网站运营专员</a><a href="https://jobs.51job.com/seo/">SEO/SEM</a><a href="https://jobs.51job.com/wangzhanyunyingzongjian/">网站运营总监</a><a href="https://jobs.51job.com/wangluotuiguangzongjian/">网络推广总监</a><a href="https://jobs.51job.com/wangluotuiguangjingli/">网络推广经理/主管</a><a href="https://jobs.51job.com/wangluotuiguangzhuanyuan/">网络推广专员</a><a href="https://jobs.51job.com/yonghuyunying/">用户运营</a><a href="https://jobs.51job.com/huodongyunying/">活动运营</a><a href="https://jobs.51job.com/neirongyunying/">内容运营</a><a href="https://jobs.51job.com/shujuyunying/">数据运营</a><a href="https://jobs.51job.com/xianxiayunying/">线下运营</a><a href="https://jobs.51job.com/xinxiliuyouhua/">信息流优化师</a><a href="https://jobs.51job.com/yunyingzhuanyuan/">运营专员</a><a href="https://jobs.51job.com/yunyingzhuguan/">运营主管</a><a href="https://jobs.51job.com/yunyingjingli/">运营经理</a><a href="https://jobs.51job.com/yunyingzongjian/">运营总监</a><a href="https://jobs.51job.com/pinleiyunying/">品类运营</a><a href="https://jobs.51job.com/neirongshenhe/">内容审核</a><a href="https://jobs.51job.com/yunyingzhuli/">运营助理</a><a href="https://jobs.51job.com/weiboyunying/">微博运营</a><a href="https://jobs.51job.com/weixinyunying/">微信运营</a><a href="https://jobs.51job.com/chanpinyunying/">产品运营</a><a href="https://jobs.51job.com/shequyunying/">社区/社群运营</a><a href="https://jobs.51job.com/zhiboyunying/">直播运营</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jiaoyuzixun/"><strong>教育咨询</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/kechengguwen/">课程顾问</a><a href="https://jobs.51job.com/zhaoshenglaoshi/">招生老师</a><a href="https://jobs.51job.com/xuexiguihuashi/">学习规划师</a><a href="https://jobs.51job.com/liuxueguwen/">留学顾问</a><a href="https://jobs.51job.com/kcxs-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><a  href="https://jobs.51job.com/jiaoyuguanli/"><strong>教育管理</strong></a></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/xiaozhang/">校长</a><a href="https://jobs.51job.com/banzhurenfudaoyuan/">班主任/辅导员</a><a href="https://jobs.51job.com/jiaowuguanli/">院校教务管理人员</a><a href="https://jobs.51job.com/yuanzhang/">园长</a><a href="https://jobs.51job.com/jiaoyanzuzhangzhuguan/">教研组长/主管</a><a href="https://jobs.51job.com/jiaoyanyuan/">教研员</a><a href="https://jobs.51job.com/jiaoshipeixunshixun/">教师培训/师训</a><a href="https://jobs.51job.com/jygl-others/">其他</a>                </div>
                <div class="clear"></div>
            </div>
            </div>
    <div class="filter">
        <div class="tg">全部招聘行业</div>
                    <div class="e e5">
                <p><strong>计算机/互联网/通信/电子</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy01/">计算机软件</a><a href="https://jobs.51job.com/hy37/">计算机硬件</a><a href="https://jobs.51job.com/hy38/">计算机服务(系统、数据服务、维修)</a><a href="https://jobs.51job.com/hy31/">通信/电信/网络设备</a><a href="https://jobs.51job.com/hy39/">通信/电信运营、增值服务</a><a href="https://jobs.51job.com/hy32/">互联网/电子商务</a><a href="https://jobs.51job.com/hy40/">网络游戏</a><a href="https://jobs.51job.com/hy02/">电子技术/半导体/集成电路</a><a href="https://jobs.51job.com/hy35/">仪器仪表/工业自动化</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>会计/金融/银行/保险</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy41/">会计/审计</a><a href="https://jobs.51job.com/hy03/">金融/投资/证券</a><a href="https://jobs.51job.com/hy42/">银行</a><a href="https://jobs.51job.com/hy43/">保险</a><a href="https://jobs.51job.com/hy62/">信托/担保/拍卖/典当</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>贸易/消费/制造/营运</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy04/">贸易/进出口</a><a href="https://jobs.51job.com/hy22/">批发/零售</a><a href="https://jobs.51job.com/hy05/">快速消费品(食品、饮料、化妆品)</a><a href="https://jobs.51job.com/hy06/">服装/纺织/皮革</a><a href="https://jobs.51job.com/hy44/">家具/家电/玩具/礼品</a><a href="https://jobs.51job.com/hy60/">奢侈品/收藏品/工艺品/珠宝</a><a href="https://jobs.51job.com/hy45/">办公用品及设备</a><a href="https://jobs.51job.com/hy14/">机械/设备/重工</a><a href="https://jobs.51job.com/hy33/">汽车</a><a href="https://jobs.51job.com/hy65/">汽车零配件</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>制药/医疗</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy08/">制药/生物工程</a><a href="https://jobs.51job.com/hy46/">医疗/护理/卫生</a><a href="https://jobs.51job.com/hy47/">医疗设备/器械</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>广告/媒体</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy12/">广告</a><a href="https://jobs.51job.com/hy48/">公关/市场推广/会展</a><a href="https://jobs.51job.com/hy49/">影视/媒体/艺术/文化传播</a><a href="https://jobs.51job.com/hy13/">文字媒体/出版</a><a href="https://jobs.51job.com/hy15/">印刷/包装/造纸</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>房地产/建筑</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy26/">房地产</a><a href="https://jobs.51job.com/hy09/">建筑/建材/工程</a><a href="https://jobs.51job.com/hy50/">家居/室内设计/装潢</a><a href="https://jobs.51job.com/hy51/">物业管理/商业中心</a><a href="https://jobs.51job.com/hy34/">中介服务</a><a href="https://jobs.51job.com/hy63/">租赁服务</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>专业服务/教育/培训</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy07/">专业服务(咨询、人力资源、财会)</a><a href="https://jobs.51job.com/hy59/">外包服务</a><a href="https://jobs.51job.com/hy52/">检测，认证</a><a href="https://jobs.51job.com/hy18/">法律</a><a href="https://jobs.51job.com/hy23/">教育/培训/院校</a><a href="https://jobs.51job.com/hy24/">学术/科研</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>服务业</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy11/">餐饮业</a><a href="https://jobs.51job.com/hy53/">酒店/旅游</a><a href="https://jobs.51job.com/hy17/">娱乐/休闲/体育</a><a href="https://jobs.51job.com/hy54/">美容/保健</a><a href="https://jobs.51job.com/hy27/">生活服务</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>物流/运输</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy21/">交通/运输/物流</a><a href="https://jobs.51job.com/hy55/">航天/航空</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>能源/环保/化工</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy19/">石油/化工/矿产/地质</a><a href="https://jobs.51job.com/hy16/">采掘业/冶炼</a><a href="https://jobs.51job.com/hy36/">电气/电力/水利</a><a href="https://jobs.51job.com/hy61/">新能源</a><a href="https://jobs.51job.com/hy56/">原材料和加工</a><a href="https://jobs.51job.com/hy20/">环保</a>                </div>
                <div class="clear"></div>
            </div>
                    <div class="e e5">
                <p><strong>政府/非营利组织/其他</strong></p>
                <div class="lkst">
                    <a href="https://jobs.51job.com/hy28/">政府/公共事业</a><a href="https://jobs.51job.com/hy57/">非营利组织</a><a href="https://jobs.51job.com/hy29/">农/林/牧/渔</a><a href="https://jobs.51job.com/hy58/">多元化业务集团公司</a>                </div>
                <div class="clear"></div>
            </div>
            </div>
</div>'''

def get_jobs_list():
	dom = etree.HTML(html)
	return dom.xpath("//div[@class='lkst']//a/text()")
