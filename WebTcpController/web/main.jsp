<%--
  Created by IntelliJ IDEA.
  User: LMF
  Date: 2023/4/25
  Time: 18:09
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="utf-8">
  <title>智能控制</title>
</head>
<style>
  body {
    padding: 0;
    margin: 0;
  }
  .flexs {
    display: flex;
    margin: 20px;
    overflow: auto;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  }
  div {
    text-align: center;
    color: #8A2BE2;
  }
  h3 {
    text-align: center;
    color: #ff4141;
  }
  a {
    float: left;
    color: #606266;
    font-size: 16px;
    font-weight: 550;
  }
  img {
    float: left;
    height: 20px;
    width: 20px;
    margin: 6px 0;
    margin-left: 10px;
  }
  input[type="button"] {
    height: 28px;
    line-height: 28px;
    float: right;
    box-sizing: border-box;
    margin: 2px 0;
    margin-left: 8px;
    cursor: pointer;
  }
  .four {
    float: right;
    height: 28px;
    line-height: 28px;
    box-sizing: border-box;
    margin: 2px 0;
    margin-left: 10px;
    width: 60px;
  }
  .led {
    float: right;
    height: 28px;
    line-height: 28px;
    box-sizing: border-box;
    margin: 2px 0;
    width: 280px;
  }
  span {
    float: right;
    margin-right: 10px;
    color: #101010;
    font-size: 15px;
  }
  .title {
    position: absolute;
    top: 0;
    left: 0;
    height: 28px;
    width: auto;
    padding: 0 10px;
    line-height: 28px;
    border-radius: 4px;
    background: #101010;
    color: #fff;
    font-size: 14px;
    font-weight: 600;
  }
  .commom {
    flex: 1;
    position: relative;
    /* background: #EBEEF5; */
    height: auto;
    margin: 0 1px;
    padding: 30px 0;
    border-right: 1px solid #DCDFE6;
    /* border-radius: 4px; */
    /* box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); */
    text-align: center;
  }
  .item {
    height: 32px;
    padding-left: 8px;
    line-height: 32px;
    margin: 5px 15px;
    text-align: left;
    transition: .4s;
    color: #101010;
    background: #fff;
    border-radius: 4px;
  }
  .item:hover {
    background: #E4E7ED;
  }
  .borders {
    border-bottom: 1px solid #EBEEF5;
  }
</style>
<script>
  // 网页加载主函数入口
  function main() {
    console.log("网页启动");
    //循环执行，每隔3秒钟执行一次showalert（）
    window.setInterval(showalert,5000);
    //线程延时运行执行获取传感器数据
    setTimeout(function () {
      httpGet("http://localhost:8080/WebTcpController/getSensorData");
    },400);
    //线程延时运行执行获取安防传感器数据
    setTimeout(function (){
      httpGet("http://localhost:8080/WebTcpController/getSecurityData");
    },700);
  }
  //循环线程
  function showalert() {
    //线程延时运行执行获取传感器数据
    setTimeout(function (){
      httpGet("http://localhost:8080/WebTcpController/getSensorData");
    },400);
    //线程延时运行执行获取安防传感器数据
    setTimeout(function () {
      httpGet("http://localhost:8080/WebTcpController/getSecurityData");
    },700);
  }
  //控制函数 传入控制指令
  function control(string) {
    console.log(string)
    var url="http://localhost:8080/WebTcpController/control?control="+string;
    httpGet(url);
  }
  //数码管监听
  function text_Dig() {
    var d1 = document.getElementById("text_dig1");
    var d2 = document.getElementById("text_dig2");
    var d3 = document.getElementById("text_dig3");
    var d4 = document.getElementById("text_dig4");
    console.log(d1.value + d2.value + d3.value + d4.value);
    var url="http://localhost:8080/WebTcpController/control?control=DIG_"+
            d1.value+"_"+d2.value+"_"+d3.value+"_"+d4.value;
    httpGet(url);
  }
  //LED监听
  function text_Led() {
    var oText = document.getElementById("text_led");
    console.log(oText.value);
    var url="http://localhost:8080/WebTcpController/control?control=LED_"+oText.value;
    httpGet(url);
  }
  //HTTP GET方法
  function httpGet(url) {
    const http = new XMLHttpRequest();
    http.open("GET", url);
    http.send();
    http.onreadystatechange = (e) => {
      var res = http.response;
      //解析采集传感器数据
      if(res.split("_")[0]=="SENSOR"){
        var json=res.split("_")[1];
        var obj=JSON.parse(json);
        document.getElementById("s_temp").textContent=obj.TEMP;
        document.getElementById("s_hum").textContent=obj.HUM;
        document.getElementById("s_light").textContent=obj.LIGHT;
        document.getElementById("s_air").textContent=obj.AIR;
        document.getElementById("s_pressure").textContent=obj.PR;
        document.getElementById("s_xyz").textContent=obj.XYZ;
      }
      //解析安防传感器数据
      if (res.split("_")[0]=="SECURITY"){
        var json=res.split("_")[1];
        var obj=JSON.parse(json);
        document.getElementById("s_smoke").textContent=obj.SMOKE;
        document.getElementById("s_fire").textContent=obj.FIRE;
        document.getElementById("s_infrared").textContent=obj.IR;
        document.getElementById("s_body").textContent=obj.BODY;
        document.getElementById("s_magnet").textContent=obj.MAG;
      }
    }
  }
</script>
<body onload="main()">
<div class="flexs">
  <div class="commom">
    <div class="title">智能控制</div>
    <div class="item">
      <a>风扇</a>
      <img src="./img/icon/fengshan.svg">
      <input type="button" value="关闭" onclick="control('FAN_CLOSE')" />
      <input type="button" value="打开" onclick="control('FAN_OPEN')" />
    </div>
    <div class="item">
      <a>窗帘</a>
      <img src="./img/icon/chuanglian.svg" alt="">
      <input type="button" value="关闭" onclick="control('CURTAIN_CLOSE')" />
      <input type="button" value="打开" onclick="control('CURTAIN_OPEN')" />
    </div>
    <div class="item">
      <a>音乐</a>
      <img src="img/icon/music-note-beamed.svg" />
      <input type="button" value="关闭" onclick="control('MUSIC_CLOSE')" />
      <input type="button" value="打开" onclick="control('MUSIC_OPEN')" />
    </div>
    <div class="item">
      <a>插座</a>
      <img src="./img/icon/chazuo.svg" alt="">
      <input type="button" value="关闭" onclick="control('SOCKET_CLOSE')" />
      <input type="button" value="打开" onclick="control('SOCKET_OPEN')" />
    </div>
  </div>
  <div class="commom">
    <div class="title">显示传感</div>
    <div class="item">
      <a style="margin-right: 10px;">数码管</a>
      <img src="./img/icon/zu.svg">
      <input type="button" value="发送" onclick="text_Dig()" />
      <input class="four" type="text" id="text_dig4" />
      <input class="four" type="text" id="text_dig3" />
      <input class="four" type="text" id="text_dig2" />
      <input class="four" type="text" id="text_dig1" />
    </div>
    <div class="item">
      <a>LED屏幕</a>
      <img src="./img/icon/w_pingmu.svg">
      <input type="button" value="发送" onclick="text_Led()" />
      <input class="led" type="text" id="text_led" />
    </div>
  </div>
</div>
<div class="flexs">
  <div class="commom">
    <div class="title">采集传感</div>
    <div class="item borders">
      <a>温度</a>
      <img src="./img/icon/wendu.svg">
      <span id="s_temp">暂无数据</span>
    </div>
    <div class="item borders">
      <a>湿度</a>
      <img src="./img/icon/wenshiduchuanganqi_o.svg">
      <span id="s_hum">暂无数据</span>
    </div>
    <div class="item borders">
      <a>光照</a>
      <img src="./img/icon/guangzhao.svg">
      <span id="s_light">暂无数据</span>
    </div>
    <div class="item borders">
      <a>空气</a>
      <img src="./img/icon/kongqizhiliangfenxi.svg">
      <span id="s_air">暂无数据</span>
    </div>
    <div class="item borders">
      <a>气压</a>
      <img src="./img/icon/qiya.svg">
      <span id="s_pressure">暂无数据</span>
    </div>
    <div class="item borders">
      <a>陀螺仪</a>
      <img src="./img/icon/tuoluoyi.svg">
      <span id="s_xyz">暂无数据</span>
    </div>
  </div>
  <div class="commom">
    <div class="title">安防传感</div>
    <div class="item borders">
      <a>烟雾</a>
      <img src="./img/icon/yanwubaojingqi.svg">
      <span id="s_smoke">暂无数据</span>
    </div>
    <div class="item borders">
      <a>火焰</a>
      <img src="./img/icon/huo.svg">
      <span id="s_fire">暂无数据</span>
    </div>
    <div class="item borders">
      <a>红外</a>
      <img src="./img/icon/hongwaijiance_1.svg">
      <span id="s_infrared">暂无数据</span>
    </div>
    <div class="item borders">
      <a>人体</a>
      <img src="./img/icon/rentiganying.svg">
      <span id="s_body">暂无数据</span>
    </div>
    <div class="item borders">
      <a>磁铁</a>
      <img src="./img/icon/citie.svg">
      <span id="s_magnet">暂无数据</span>
    </div>
  </div>
</div>
</body>
</html>
