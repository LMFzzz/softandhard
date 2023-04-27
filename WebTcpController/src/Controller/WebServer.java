package Controller;

import Bean.Data;
import Util.TcpServer;

import java.net.Socket;
import java.util.List;

//服务器Socket
public class WebServer {
    //TCP服务器对象
    public static TcpServer hardwareServer,phoneServer;
    //创建客户端服务器
    public static void openServer(){
        //手机端服务端
        phoneServer=new TcpServer(20210);
        phoneServer.setOnTcpListener(new WebPhoneServerListener());
        //硬件端服务端
        hardwareServer=new TcpServer(20211);
        hardwareServer.setOnTcpListener(new WebHardWareServerListener());
        System.out.println("Socket服务器创建");
    }
    //发送数据到客户端
    public static void sendDataToCustom(String msg,TcpServer tcpServer){
        List<Socket> listSocket=tcpServer.getListSocket();
        for (int i=0;i<listSocket.size();i++){
            Socket so= listSocket.get(i);
            TcpServer.sendDataTo(so,msg);
        }
    }
    //发送数据到客户端
    public static void sendDataToCustom(byte[] data,TcpServer tcpServer){
        List<Socket>listSocket=tcpServer.getListSocket();
        for(int i=0;i<listSocket.size();i++){
            Socket so=listSocket.get(i);
            TcpServer.sendDataTo(so,data);
        }
    }
    //手机客户端返回信息的监听类
    public static class WebPhoneServerListener implements TcpServer.OnTcpReceiveListener{

        @Override
        public void onReceive(byte[] b, int len, Socket so) {
            String msg=new String(b,0,len);
            System.out.println("手机客户端数据:"+msg);
            sendDataToCustom(msg,hardwareServer);
        }

        @Override
        public void onMonitor(Socket so) {

        }

        @Override
        public void onClose(Socket so) {

        }
    }
    //硬件端返回信息的监听类
    public static class WebHardWareServerListener implements TcpServer.OnTcpReceiveListener{

        @Override
        public void onReceive(byte[] b, int len, Socket so) {
            String msg=new String(b,0,len);
            System.out.println("硬件端数据:"+msg);
            sendDataToCustom(msg,phoneServer);
            if (msg.contains("SECURITY")){
                Data.data_SECURITY=msg;
            }
            if (msg.contains("SENSOR")){
                Data.data_SENSOR=msg;
            }
        }

        @Override
        public void onMonitor(Socket so) {

        }

        @Override
        public void onClose(Socket so) {

        }
    }

}
