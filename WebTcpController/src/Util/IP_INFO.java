package Util;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class IP_INFO {
    //获取本机IP信息
    public static String getIP_INFO(){
       InetAddress ip4=null;
        try {
             ip4=Inet4Address.getLocalHost();
        }catch (UnknownHostException e){
            e.printStackTrace();
        }
            return ip4.getHostAddress();
    }
}
