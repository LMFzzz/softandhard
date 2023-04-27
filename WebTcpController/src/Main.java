import Controller.WebServer;
import Util.IP_INFO;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
//程序主入口
public class Main implements ServletContextListener {
    //创建
    @Override
    public void contextInitialized(ServletContextEvent servletContextEvent) {
        System.out.println("华软智能系统-服务器启动");
        //创建服务器IP端口
        WebServer.openServer();
        System.out.println("本地IP地址:"+ IP_INFO.getIP_INFO());
    }
    //销毁
    @Override
    public void contextDestroyed(ServletContextEvent servletContextEvent) {
        System.out.println("华软智能系统-服务器关闭");
    }
}
