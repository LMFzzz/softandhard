package com.example.androidcontrollersystem;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;


import com.example.androidcontrollersystem.bean.SecurityBean;
import com.example.androidcontrollersystem.bean.SensorBean;
import com.example.androidcontrollersystem.tool.IntentSkip;
import com.example.androidcontrollersystem.tool.TCPSocket;
import com.google.gson.Gson;

import java.net.Socket;


public class MainActivity extends AppCompatActivity {
    //单前对象
    private AppCompatActivity ac;
    //Tcp网络对象
    public static TCPSocket tcpSocket;
    //组件
    private ImageView bt_wifi,img_sate;
    private LinearLayout bt_ex1,bt_ex2,bt_ex3,bt_ex4;
    //实体类
    public static SecurityBean securityBean;
    public static SensorBean sensorBean;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().hide();
        init();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        tcpSocket.closeConnet();
        tcpSocket=null;
    }
    private void init(){
        ac=this;
        tcpSocket=new TCPSocket();
        tcpSocket.setListener(new TcpListener());
        bt_wifi=findViewById(R.id.bt_wifi);
        img_sate=findViewById(R.id.img_state);
        bt_ex1=findViewById(R.id.bt_ex1);
        bt_ex2=findViewById(R.id.bt_ex2);
        bt_ex3=findViewById(R.id.bt_ex3);
        bt_ex4=findViewById(R.id.bt_ex4);
        BtListener l =new BtListener();
        bt_wifi.setOnClickListener(l);
        bt_ex1.setOnClickListener(l);
        bt_ex2.setOnClickListener(l);
        bt_ex3.setOnClickListener(l);
        bt_ex4.setOnClickListener(l);
    }
    private void showTcpDialog(){
        AlertDialog.Builder builder=new AlertDialog.Builder(ac);
        View dialogView= LayoutInflater.from(ac).inflate(R.layout.edit_tcp,null);
        builder.setTitle("网络连接");
        builder.setView(dialogView);
        builder.setNegativeButton("取消",null);
        builder.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                EditText edit_ip=dialogView.findViewById(R.id.edit_ip);
                EditText edit_port=dialogView.findViewById(R.id.edit_port);
                String ip=edit_ip.getText().toString();
                int port=Integer.parseInt(edit_port.getText().toString());
                tcpSocket.connet(ip,port);
            }
        });
        builder.show();
    }
    private class TcpListener implements TCPSocket.OnReadListener{

        @Override
        public void onConneting() {

        }

        @Override
        public void onConnetSuccess(String ip) {
            img_sate.setImageResource(R.mipmap.img_yes);
        }

        @Override
        public void onConnetTimeOut() {
            img_sate.setImageResource(R.mipmap.img_no);
        }

        @Override
        public void onConnetLost() {
            img_sate.setImageResource(R.mipmap.img_no);
        }

        @Override
        public void onRead(byte[] b, int len, Socket so) {
            String msg=new String(b,0,len);
            Gson gson=new Gson();
            try {
                String [] split=msg.split("_");
                //安防协议
                if (split[0].equals("SECURITY")){
                    securityBean=gson.fromJson(split[1],SecurityBean.class);
                }
                if (split[0].equals("SENSOR")){
                    sensorBean=gson.fromJson(split[1],SensorBean.class);
                }
            }catch (Exception e){
                Log.e("MSG","解析错误:"+e.getMessage());
            }
        }
    }
    private class BtListener implements View.OnClickListener{

        @Override
        public void onClick(View v) {
            if (v==bt_wifi){
                showTcpDialog();
            }
            if (!tcpSocket.isConnet){
                Toast.makeText(ac, "请点击右上角先连接", Toast.LENGTH_SHORT).show();
                return;
            }
            if (v==bt_ex1){
                IntentSkip.toActivity(ac,Ex1Activity.class);
                return;
            }
            if (v==bt_ex2){
                IntentSkip.toActivity(ac,Ex2Activity.class);
                return;
            }
            if (v==bt_ex3){
                IntentSkip.toActivity(ac,Ex3Activity.class);
                return;
            }
            if (v==bt_ex4){
                IntentSkip.toActivity(ac,Ex4Activity.class);
            }
        }
    }
}