package Util;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

//服务器工具类
public class TcpServer {
    //TCP服务端
    protected ServerSocket tcpServer;
    //服务器数据监听类
    protected OnTcpReceiveListener tcpListen;
    //Socket客户List列表
    protected List<Socket> listSocket;
    //实例化传入端口号
    public TcpServer(int tcpPort){
        createTcpConnet(tcpPort);
    }
    //创建TCP客户端，传入端口号
    private void createTcpConnet(int tcpPort){
        try {
            tcpServer=new ServerSocket(tcpPort);
            listSocket=new ArrayList<Socket>();
            System.out.println("服务器创建");
            //监听连接的客户
            new Thread(new AcceptSocketThread()).start();
            //开启心跳包线程
            new Thread(new MonitorThread()).start();
        }catch (IOException e){
            System.out.println("创建TCP服务器时出错");
            e.printStackTrace();
        }
    }
    //发送数据到已链接的Socket端口
    public static void sendDataTo(Socket so,byte[] data){
        if (so!=null&&data!=null){
            if (!so.isClosed()){
                try {
                    OutputStream out=so.getOutputStream();
                    out.write(data);
                    out.flush();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }
    //发送数据到已链接的Socket端口
    public static void sendDataTo(Socket so,String msg){
        if (so!=null&&msg!=null){
            if (!so.isClosed()){
                try {
                    System.out.println("发送"+msg);
                    OutputStream out=so.getOutputStream();
                    out.write(msg.getBytes());
                    out.flush();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }
    //获取TCPSocket连接对象列表
    public List<Socket> getListSocket(){
        return listSocket;
    }
    //设置TCP数据返回的监听事件，tcpListen监听接口
    public void setOnTcpListener(OnTcpReceiveListener tcpListen){
        this.tcpListen=tcpListen;
    }
    //监听Socket连接的线程类
    private class AcceptSocketThread implements Runnable{

        @Override
        public void run() {
            while (true){
                try {
                    if (tcpServer!=null){
                        //监听连接进来的Socket
                        Socket so= tcpServer.accept();
                        listSocket.add(so);
                        System.out.println("IP:"+so.getInetAddress().getHostName()+"连接");
                        new Thread(new ReadDataThread(so)).start();
                    }
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }
    //处理已连接对象的数据的线程
    private class ReadDataThread implements Runnable{
        private Socket so;
        public ReadDataThread(Socket so){
            this.so=so;
        }

        @Override
        public void run() {
            byte[] b=new byte[20000];
            int len =0;
            InputStream in=null;
            try {
                in=so.getInputStream();
            }catch (IOException e){
                e.printStackTrace();
            }
            try {
                while ((len=in.read(b))!=-1){
                    if (len>0){
                        if (tcpListen!=null){
                            tcpListen.onReceive(b,len,so);
                        }
                    }
                }
            }catch (Exception e){
                e.printStackTrace();
            }
            try {
                if (!so.isClosed()){
                    so.close();
                    tcpListen.onClose(so);
                }
            }catch (IOException e){
                e.printStackTrace();
            }
        }
    }
    //每5秒回调函数的监听(用于心跳包或者其他用途)
    private class MonitorThread implements Runnable{

        @Override
        public void run() {
            while (true){
                for (int i=0;i<listSocket.size();i++){
                    Socket so=listSocket.get(i);
                    if (so.isConnected()){
                        if (tcpListen!=null){
                            tcpListen.onMonitor(so);
                        }
                    }else {
                        System.err.println(so.getInetAddress().getHostName()+"离线了");
                        try {
                            if (!so.isClosed()){
                                so.close();
                                listSocket.remove(so);
                                tcpListen.onClose(so);
                            }
                        }catch (IOException e1){
                            e1.printStackTrace();
                        }
                    }
                }
                    //休眠5秒
                    try {
                        Thread.sleep(5000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
            }
        }
    }
    //监听TCP接收到的数据的监听
    public interface OnTcpReceiveListener{
        //接收到数据信息的监听
        void onReceive(byte[] b,int len,Socket so);
        //每过5秒回调的监听
        void onMonitor(Socket so);
        //通讯关闭了的监听
        void onClose(Socket so);
    }
}
