package com.example.androidcontrollersystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Ex4Activity extends AppCompatActivity {
    private Button r1_open,r2_open,r3_open,r4_open,r1_close,r2_close,r3_close,r4_close;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ex4);
        getSupportActionBar().hide();
        init();
    }
    private void init(){
        r1_open=findViewById(R.id.r1_open);
        r1_close=findViewById(R.id.r1_close);
        r2_open=findViewById(R.id.r2_open);
        r2_close=findViewById(R.id.r2_close);
        r3_open=findViewById(R.id.r3_open);
        r3_close=findViewById(R.id.r3_close);
        r4_open=findViewById(R.id.r4_open);
        r4_close=findViewById(R.id.r4_close);
        BtListener l=new BtListener();
        r1_open.setOnClickListener(l);
        r1_close.setOnClickListener(l);
        r2_open.setOnClickListener(l);
        r2_close.setOnClickListener(l);
        r3_open.setOnClickListener(l);
        r3_close.setOnClickListener(l);
        r4_open.setOnClickListener(l);
        r4_close.setOnClickListener(l);
    }
    private class BtListener implements View.OnClickListener{

        @Override
        public void onClick(View v) {
            if (v==r1_open){
                MainActivity.tcpSocket.sendDataToServer("C1_OPEN");
            } else if (v==r1_close) {
                MainActivity.tcpSocket.sendDataToServer("C1_CLOSE");
            } else if (v==r2_open) {
                MainActivity.tcpSocket.sendDataToServer("C2_OPEN");
            } else if (v==r2_close) {
                MainActivity.tcpSocket.sendDataToServer("C2_CLOSE");
            } else if (v==r2_close) {
                MainActivity.tcpSocket.sendDataToServer("R2_CLOSE");
            } else if (v==r3_open) {
                MainActivity.tcpSocket.sendDataToServer("C3_OPEN");
            } else if (v==r3_close) {
                MainActivity.tcpSocket.sendDataToServer("C3_CLOSE");
            } else if (v==r4_open) {
                MainActivity.tcpSocket.sendDataToServer("C4_OPEN");
            } else if (v==r4_close) {
                MainActivity.tcpSocket.sendDataToServer("C4_CLOSE");
            }
        }
    }
}