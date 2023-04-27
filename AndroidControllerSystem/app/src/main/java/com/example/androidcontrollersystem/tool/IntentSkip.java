package com.example.androidcontrollersystem.tool;

import static android.os.Build.VERSION_CODES.R;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;

public class IntentSkip {
    public static void toActivity(final Context packageContext,final Class<?> cls ){
        final Activity ac=(Activity) packageContext;
        ac.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                ac.overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out);
                Intent intent=new Intent(packageContext,cls);
                ac.startActivity(intent);
            }
        });
    }
}
