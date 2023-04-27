package Controller;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.reflect.Method;

@SuppressWarnings("serial")
public abstract class BaseServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doPost(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
      try {
          req.setCharacterEncoding("UTF-8");
          resp.setCharacterEncoding("UTF-8");
      }catch (IOException e){
          e.printStackTrace();
      }
      String path=req.getServletPath();
        System.out.println(path);
        int pos=path.lastIndexOf("/");
        //得到想要跳转的函数的具体方法
        String methodName=path.substring(pos+1,path.length());
        try {
            //用反射跳转到具体方法
            Method m= getClass().getDeclaredMethod(methodName,
                    HttpServletRequest.class,HttpServletResponse.class);
            m.invoke(this,req,resp);
        }catch (Exception e){
            System.out.println("反射出现异常");
            e.printStackTrace();
        }
    }
    public void sendPoseResponse(HttpServletResponse resp,String msg){
        OutputStream os=null;
        try {
            os=resp.getOutputStream();
            os.write(msg.getBytes());
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
