package com.example.androidcontrollersystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;



import java.net.Socket;

public class Ex1Activity extends AppCompatActivity {

    private EditText edit_num1, edit_num2, edit_num3, edit_num4, edit_msg;
    private Button bt_send;
    private ImageView iv_back;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ex1);
        getSupportActionBar().hide();
        init();
    }

    private void init() {
        edit_num1 = findViewById(R.id.edit_num1);
        edit_num2 = findViewById(R.id.edit_num2);
        edit_num3 = findViewById(R.id.edit_num3);
        edit_num4 = findViewById(R.id.edit_num4);
        edit_msg = findViewById(R.id.edit_msg);
        EditListener ed1=new EditListener(edit_num1);
        EditListener ed2=new EditListener(edit_num2);
        EditListener ed3=new EditListener(edit_num3);
        EditListener ed4=new EditListener(edit_num4);
        edit_num1.addTextChangedListener(ed1);
        edit_num2.addTextChangedListener(ed2);
        edit_num3.addTextChangedListener(ed3);
        edit_num4.addTextChangedListener(ed4);
        bt_send = findViewById(R.id.bt_send);
        BtListener l =new BtListener();
        bt_send.setOnClickListener(l);
    }

    private class EditListener implements TextWatcher {
        private EditText e_view;

        public EditListener(EditText e_view) {
            this.e_view = e_view;
        }

        @Override
        public void beforeTextChanged(CharSequence s, int start, int count, int after) {

        }

        @Override
        public void onTextChanged(CharSequence s, int start, int before, int count) {
            Log.d("HSG", s.toString() + "||" + start + "||" + before + "||" + count);
            String msg = "";
            if (s.toString().length() >= 2) {
                String edit = e_view.getText().toString();
                msg = edit.substring(0, 1);
                e_view.setText(msg);
            }
            //发送
            String e1 = "0";
            String e2 = "0";
            String e3 = "0";
            String e4 = "0";
            String edit1 = edit_num1.getText().toString();
            String edit2 = edit_num2.getText().toString();
            String edit3 = edit_num3.getText().toString();
            String edit4 = edit_num4.getText().toString();
            if (!edit1.equals("")) {
                e1 = edit1;
            }
            if (!edit2.equals("")) {
                e2 = edit2;
            }
            if (!edit3.equals("")) {
                e3 = edit3;
            }
            if (!edit4.equals("")) {
                e4 = edit4;
            }
            MainActivity.tcpSocket.sendDataToServer("DIG_" + e1 + "_" + e2 + "_" + e3 + "_" + e4);
        }

        @Override
        public void afterTextChanged(Editable editable) {

        }
    }

    private class BtListener implements View.OnClickListener {

        @Override
        public void onClick(View v) {
            if (v == bt_send) {
                String msg = edit_msg.getText().toString();
                MainActivity.tcpSocket.sendDataToServer("LED_"+msg);
            }
        }
    }
}