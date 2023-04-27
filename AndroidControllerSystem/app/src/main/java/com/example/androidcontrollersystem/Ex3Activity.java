package com.example.androidcontrollersystem;


import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;



public class Ex3Activity extends AppCompatActivity {
    private boolean isRun=true;
    private TextView text_smoke,text_fire,text_red,text_body,text_magnet;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ex3);
        getSupportActionBar().hide();
        init();
    }
    private void init(){
        text_smoke=findViewById(R.id.text_smoke);
        text_fire=findViewById(R.id.text_fire);
        text_red=findViewById(R.id.text_red);
        text_body=findViewById(R.id.text_body);
        text_magnet=findViewById(R.id.text_magnet);
        //启动数据获取线程
        new Thread(new TimeThread()).start();
    }
    private class TimeThread implements  Runnable{

        @Override
        public void run() {
            while (isRun){
                if (MainActivity.securityBean==null){
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                    continue;
                }
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        //烟雾
                        if (MainActivity.securityBean.SMOKE.equals("1")){
                            text_smoke.setText("警报");
                        }else {
                            text_smoke.setText("无");
                        }
                        //火焰
                        if (MainActivity.securityBean.FIRE.equals("1")){
                            text_fire.setText("警报");
                        }else {
                            text_fire.setText("无");
                        }
                        //红外
                        if (MainActivity.securityBean.IR.equals("1")){
                            text_red.setText("警报");
                        }else {
                            text_red.setText("无");
                        }
                        //人体
                        if (MainActivity.securityBean.BODY.equals("1")){
                            text_body.setText("警报");
                        }else {
                            text_body.setText("无");
                        }
                        //磁铁
                        if (MainActivity.securityBean.MAG.equals("1")){
                            text_magnet.setText("警报");
                        }else {
                            text_magnet.setText("无");
                        }
                    }
                });
                try {
                    Thread.sleep(1000);
                }catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
    }
}