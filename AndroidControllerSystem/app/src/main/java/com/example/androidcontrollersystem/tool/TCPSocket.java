package com.example.androidcontrollersystem.tool;

import android.os.Handler;
import android.util.Log;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class TCPSocket {
    private Handler handler;
    private Socket so;
    public boolean isConnet=false;
    public boolean isConneting=false;
    private InputStream in;
    private OutputStream out;
    public OnReadListener listener;
    private String ip;
    private int port;

    public TCPSocket() { this.handler=new Handler();}
    //连接模块
    public void connet(final String dstName,final int dstPort){
        if (!isConnet && !isConneting){
            isConneting=true;
            new Thread(new ConnetThread(dstName, dstPort)).start();
        }
    }
    public Socket getSocket(){
        if (so!=null){
            return so;
        }
        return null;
    }
    public void setListener(OnReadListener listener){this.listener=listener;}
    //发信息到服务器
    public void sendDataToServer(final byte[] data){
        new Thread(new Runnable() {
            @Override
            public void run() {
                if (out!=null){
                    try {
                        out.write(data);
                        out.flush();
                        Log.e("MSG","发送Success");
                    }catch (IOException e){
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }
    //连接服务器的线程
    private class ConnetThread implements Runnable{
        public ConnetThread(String dstName,int dstPort){
            ip=dstName;
            port=dstPort;
        }

        @Override
        public void run() {
            try {
                try {
                    Thread.sleep(500);
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
                Log.e("DATA","正在连接到IP:"+ip);
                if (listener!=null){
                    handler.post(new MainThread(400));
                }
                so=new Socket();
                InetSocketAddress isa=new InetSocketAddress(ip,port);
                so.connect(isa,2000);
                out=so.getOutputStream();
                in=so.getInputStream();
                isConnet=true;
                if (listener!=null){
                    handler.post(new MainThread(300));
                }
                byte[] b =new byte[6666];
                int hasRead=0;
                while ((hasRead=in.read(b))>0){
                    if (listener!=null){
                        int finalHashRead=hasRead;
                        handler.post(new Runnable() {
                            @Override
                            public void run() {
                                listener.onRead(b,finalHashRead,so);
                            }
                        });
                    }
                }
            }catch (UnknownHostException e){
                handler.post(new MainThread(100));
            }catch (IOException e){
                String err=e.getMessage();
                if (err.contains("Socket closed")){
                    handler.post(new MainThread(200));
                } else if (err.contains("failed to connect")) {
                    handler.post(new MainThread(100));
                }else {
                    e.printStackTrace();
                }
            }finally {
                if (so!=null){
                    if (!isConneting){
                        handler.post(new MainThread(200));
                    }
                    try {
                        so.close();
                        isConnet=false;
                        if (out!=null){
                            out.close();
                        }
                        if (in!=null){
                            in.close();
                        }
                        so=null;
                        out=null;
                        in=null;
                        isConneting=false;
                    }catch (IOException e){
                        e.printStackTrace();
                    }
                }
            }
        }
    }
    //发信息到服务器
    public void sendDataToServer(final String data){
        new Thread(new Runnable() {
            @Override
            public void run() {
                if (out!=null){
                    try {
                        Log.e("MSG","发送："+data);
                        out.write(data.getBytes());
                        out.flush();
                    }catch (IOException e){
                        System.out.println(e.getMessage());
                        if (e.getMessage().contains("Socket closed")){
                            handler.post(new MainThread(200));
                        }
                    }
                }
            }
        }).start();
    }
    //连接主线程
    private class MainThread implements Runnable{
        int what;

        public MainThread(int what) {
            this.what = what;
        }

        @Override
        public void run() {
            if (listener==null){
                return;
            }
            switch (what){
                case 100:
                    Log.e("DATA","连接超时或者未知地址");
                    listener.onConnetTimeOut();
                    break;
                case 200:
                    Log.e("DATA","与服务器断开了");
                    listener.onConneting();
                    break;
                case 300:
                    Log.e("DATA","连接成功");
                    listener.onConnetSuccess(ip);
                    break;
                case 400:
                    Log.e("DATA","连接中");
                    listener.onConneting();
                    break;
            }
            isConneting=false;
        }
    }
    public void closeConnet(){
        this.isConneting=false;
    }
    public interface OnReadListener{
        //连接回调，由主线程回调
        public void onConneting();
        //连接成功回调由于线程问题
        public void onConnetSuccess(String ip);
        public void onConnetTimeOut();
        public void onConnetLost();
        public void onRead(byte[] b,int len,Socket so);
    }

}
