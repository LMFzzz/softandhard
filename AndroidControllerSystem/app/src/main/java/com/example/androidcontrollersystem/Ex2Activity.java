package com.example.androidcontrollersystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class Ex2Activity extends AppCompatActivity {
    private boolean isRun=true;
    private TextView text_tmp,text_hum,text_light,text_air,text_press;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ex2);
        getSupportActionBar().hide();
        text_tmp=findViewById(R.id.text_tmp);
        text_hum=findViewById(R.id.text_hum);
        text_light=findViewById(R.id.text_light);
        text_air=findViewById(R.id.text_air);
        text_press=findViewById(R.id.text_press);
        //启动获取数据线程
        new Thread(new TimeThread()).start();
    }
    private class TimeThread implements Runnable{

        @Override
        public void run() {
            while (isRun){
                if (MainActivity.sensorBean==null){
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
                        //温度
                        text_tmp.setText(MainActivity.sensorBean.TEMP+"℃");
                        //湿度
                        text_hum.setText(MainActivity.sensorBean.HUM+"%");
                        //光照
                        text_light.setText(MainActivity.sensorBean.LIGHT+"");
                        //空气
                        text_air.setText(MainActivity.sensorBean.AIR+"");
                        //气压
                        text_press.setText(MainActivity.sensorBean.PR+" ");

                    }
                });
                try {
                    Thread.sleep(1000);
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
    }
}