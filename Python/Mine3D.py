from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import copy
import math


def drawFunc():
    # glLoadIdentity()
    # 清楚之前画面
    # glClear(GL_COLOR_BUFFER_BIT)
    # glRotatef(0.1, 3, 2, 1)  # (角度,x,y,z)
    # glutWireTetrahedron()
    # 刷新显示
    glFlush()
    pass


def keyboard(key, x, y):
    if key == b'\x1b' or key == b'q':
        exit(0)
    print(key, x, y)


def mouse(button, state, x, y):
    global last
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_UP:
            last = copy.deepcopy([x, y])


def mouse_xy(x, y):
    global last
    glLoadIdentity()
    target = x - last[0], y - last[1]
    target = [target[0] / 256, target[1] / 256]
    target = [math.sin(target[0]), math.cos(target[1])]
    glClear(GL_COLOR_BUFFER_BIT)
    # glRotatef(target[0], 0, 1, 0)
    # glRotatef(target[1], 1, 0, 0)
    # 第一组eyex, eyey,eyez 相机在世界坐标的位置
    # 第二组centerx,centery,centerz 相机镜头对准的物体在世界坐标的位置
    # 第三组upx,upy,upz 相机向上的方向在世界坐标中的方向
    gluLookAt(target[0], target[1], 0.1,
              0, 0, 0,
              0, 1, 0)
    # int AmbientLight[4]={1,1,1,1};
    # glLightfv(GL_LIGHT0,  GL_AMBIENT,  AmbientLight);
    # glEnable(GL_LIGHT0);      //允许0#灯使用
    # glEnable(GL_LIGHTING);   //开灯
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glutSolidTeapot(1)
    # 刷新显示
    glFlush()
    last = copy.deepcopy(target)


last = [0, 0]

# 使用glut初始化OpenGL
glutInit()
# 显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# 窗口位置及大小-生成
glutInitWindowPosition(0, 0)
glutInitWindowSize(400, 400)
glutCreateWindow("first")
# 调用函数绘制图像
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)

glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
glutMotionFunc(mouse_xy)

glShadeModel(GL_SMOOTH)
# 阴影模式
# glClearColor(0.0, 0.0, 0.0, 0.0)
# 深度缓存设置和测试
# glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
# 让系统修正透视
glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)

# 主循环
glutMainLoop()