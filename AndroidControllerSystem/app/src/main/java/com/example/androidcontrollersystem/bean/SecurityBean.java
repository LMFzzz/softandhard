package com.example.androidcontrollersystem.bean;

public class SecurityBean {
    public String SMOKE;
    public String FIRE;
    public String IR;
    public String BODY;
    public String MAG;

    @Override
    public String toString() {
        return "SecurityBean{" +
                "SMOKE='" + SMOKE + '\'' +
                ", FIRE='" + FIRE + '\'' +
                ", IR='" + IR + '\'' +
                ", BODY='" + BODY + '\'' +
                ", MAG='" + MAG + '\'' +
                '}';
    }
}
