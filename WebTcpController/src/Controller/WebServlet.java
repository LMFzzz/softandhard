package Controller;

import Bean.Data;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@SuppressWarnings("“serial")
@javax.servlet.annotation.WebServlet(name = "Controller",urlPatterns = {"/control",
        "/getSensorData","/getSecurityData"})
public class WebServlet extends BaseServlet{
    //获取采集类传感器数据
    public void getSensorData(HttpServletRequest req, HttpServletResponse resp){
        System.out.println("HTTP请求-获取采集类传感器数据");
        sendPoseResponse(resp, Data.data_SENSOR);
        System.out.println(Data.data_SENSOR);
    }
    //获取安防数据
    public void getSecurityData(HttpServletRequest req,HttpServletResponse resp){
        System.out.println("HTTP请求-获取传感器安防数据");
        sendPoseResponse(resp,Data.data_SECURITY);
        System.out.println(Data.data_SECURITY);
    }
    //控制设备
    public void control(HttpServletRequest req,HttpServletResponse resp){
        System.out.println("HTTP请求-控制设备");
        String data=req.getParameter("control");
        System.out.println(data);
        if (data.contains("LED")){
            WebServer.sendDataToCustom(data,WebServer.hardwareServer);
            return;
        }
        if (data.contains("DIG")){
            WebServer.sendDataToCustom(data,WebServer.hardwareServer);
            return;
        }
        switch (data){
            case "FAN_OPEN":
                WebServer.sendDataToCustom("C1_OPEN",WebServer.hardwareServer);
                break;
            case "FAN_CLOSE":
                WebServer.sendDataToCustom("C1_CLOSE",WebServer.hardwareServer);
                break;
            case "CURTAIN_OPEN":
                WebServer.sendDataToCustom("C2_OPEN",WebServer.hardwareServer);
                break;
            case "CURTAIN_CLOSE":
                WebServer.sendDataToCustom("C2_CLOSE",WebServer.hardwareServer);
                break;
            case "MUSIC_OPEN":
                WebServer.sendDataToCustom("C3_OPEN",WebServer.hardwareServer);
                break;
            case "MUSIC_CLOSE":
                WebServer.sendDataToCustom("C3_CLOSE",WebServer.hardwareServer);
                break;
            case "SOCKET_OPEN":
                WebServer.sendDataToCustom("C4_OPEN",WebServer.hardwareServer);
                break;
            case "SOCKET_CLOSE":
                WebServer.sendDataToCustom("C4_CLOSE",WebServer.hardwareServer);
                break;
        }
    }
}
