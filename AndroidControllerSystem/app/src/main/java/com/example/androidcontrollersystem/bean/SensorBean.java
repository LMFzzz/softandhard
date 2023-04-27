package com.example.androidcontrollersystem.bean;

public class SensorBean {
    public String TEMP;
    public String HUM;
    public String LIGHT;
    public String AIR;
    public String PR;
    public String XYZ;

    @Override
    public String toString() {
        return "SensorBean{" +
                "TEMP='" + TEMP + '\'' +
                ", HUM='" + HUM + '\'' +
                ", LIGHT='" + LIGHT + '\'' +
                ", AIR='" + AIR + '\'' +
                ", PR='" + PR + '\'' +
                ", XYZ='" + XYZ + '\'' +
                '}';
    }
}
