import pygame
import random

# 初始化pygame
pygame.init()
# 设置窗口大小
screen_width = 1200
screen_height = 800
# 设置游戏窗口大小
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("飞盘射击游戏")

mode=1

# mode==1 为鼠标点击模式    2  为自动点击模式

# 加载背景图片
background_image = pygame.image.load("bg.jpeg")

background_image= pygame.transform.scale(background_image, (1200, 800))
disc_img = pygame.image.load("point.png")


radius = 40
x = random.randint(300, 900)
y = random.randint(200,600)



# 设置游戏的时钟
clock = pygame.time.Clock()
fg=0
# 设置倒计时
time_left = 60000  # 一分钟


startgame = False;
# 设置得分
score = 0
miss_score = 0
# 设置计时器变量
start_time = None
shot=0
import datetime
ct=0

# 获取当前时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

# 将鼠标位置和时间写入txt文件
with open('panshow_time' + str(fg) + '.txt', 'a') as f:
    f.write(f'({now}\n')
# 初始化变量
clock = pygame.time.Clock()
positions = []
last_time = pygame.time.get_ticks()
# 主游戏循环
while True:
    # 定义按钮的属性
    button_width = 80
    button_height = 30
    button_color = (0, 0, 0,0)
    button_text = 'Start'
    mouse_pos = pygame.mouse.get_pos()
    # 创建 "Start" 按钮的矩形对象
    start_button_rect = pygame.Rect(
        50,
        10,
        button_width, button_height)

    # 定义按钮的属性
    button_width = 80
    button_height = 30
    button_color = (54, 50, 56, 100)
    button_text = 'Pause'

    # 创建 "Start" 按钮的矩形对象
    pause_button_rect = pygame.Rect(
        150,
        10,
        button_width, button_height)

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 检查鼠标是否点击了按钮
            if start_button_rect.collidepoint(event.pos):
                # 点击了按钮，开始游戏
                print('开始游戏！')
                startgame=True
            if pause_button_rect.collidepoint(event.pos):
                # 点击了按钮，开始游戏
                print('暂停游戏！')
                fg+=1
                startgame=False
                # file.close()
            if (x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2 <= radius ** 2  and startgame  and mode==1:

                    score += 1
                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    with open('pandie_time' + str(fg) + '.txt', 'a') as f:
                        f.write(f'({now}\n')

                    shot = ct
                    ct = 0
                    # 飞盘消失
                    x = -100
                    y = -100
        # elif event.type == pygame.MOUSEBUTTONDOWN:
            # 判断是否点中了飞盘
    if startgame:
        mouse_pos = pygame.mouse.get_pos()

        # 获取当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        # 将鼠标位置和时间写入txt文件
        with open('mouse_position'+str(fg)+'.txt', 'a') as f:
            f.write(f'({x}, {y}) - {now}\n')



        if  (x - mouse_pos[0])**2 + (y - mouse_pos[1])**2 <= radius**2  and  mode==2:
            # 如果还没有开始计时，则开始计时
            if start_time is None:
                start_time = pygame.time.get_ticks()
            else:
                # 如果已经开始计时，则判断是否超过200毫秒
                elapsed_time = pygame.time.get_ticks() - start_time
                if elapsed_time >= 200:
                    score += 1
                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    with open('pandie_time' + str(fg) + '.txt', 'a') as f:
                        f.write(f'({now}\n')

                    shot = ct
                    ct = 0
                    # 飞盘消失
                    x = -100
                    y = -100
                    start_time=None
        else:
            start_time = None




    # 绘制背景

    screen.blit(background_image, (0, 0))

    screen.blit(disc_img , (pygame.mouse.get_pos()[0]-30, pygame.mouse.get_pos()[1]-30))



    # 填充 "Start" 按钮的颜色
    pygame.draw.rect(screen, button_color, start_button_rect)

    # 在 "Start" 按钮上绘制文本
    font = pygame.font.SysFont(None, 24)
    text = font.render("Start", True, (255,255, 255))
    text_rect = text.get_rect(center=start_button_rect.center)
    screen.blit(text, text_rect)



    # # 定义按钮的属性
    # button_width = 80
    # button_height = 30
    # button_color = (0, 0, 0,0)
    # button_text = 'Pause'

    # # 创建 "Start" 按钮的矩形对象
    # start_button_rect = pygame.Rect(
    #     150,
    #     10,
    #     button_width, button_height)

    # 填充 "Start" 按钮的颜色
    pygame.draw.rect(screen, button_color, pause_button_rect)

    # 在 "Start" 按钮上绘制文本
    font = pygame.font.SysFont(None, 24)
    text = font.render(button_text, True, (255,255, 255))
    text_rect = text.get_rect(center=pause_button_rect.center)
    screen.blit(text, text_rect)

    # 绘制击中时间
    font = pygame.font.SysFont("黑体", 18)
    text = font.render("击中时间:" + str(shot)+"ms", True, (255, 255, 255))
    screen.blit(text, (560, 15))
    # 获取鼠标位置
    xw, yw = pygame.mouse.get_pos()
    #
    # 计算鼠标速度
    current_time = pygame.time.get_ticks()
    positions.append((xw, yw, current_time))
    positions = [(x, y, t) for x, y, t in positions if current_time - t < 2000]
    distance = sum(
        ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 for (x1, y1, _), (x2, y2, _) in zip(positions, positions[1:]))
    speed = distance / 2 if positions else 0

    text = font.render(f"speed: {speed:.2f} p/s", True, (255, 255, 255))
    screen.blit(text, (900, 15))
    # 绘制当前时间
    font = pygame.font.SysFont("黑体", 18)
    text = font.render("当前时间:" + str(ct)+"ms", True, (255, 255, 255))
    screen.blit(text, (760, 15))

    # 绘制倒计时
    font = pygame.font.SysFont(None, 30)
    text = font.render("0:" + str(time_left)[:2], True, (255, 255, 255))
    screen.blit(text, (250, 15))
    if startgame:
        # 减少时间
        time_left -= 1
        ct+=1

        # 检查是否时间到了
        if time_left <= 0:
            # 游戏结束
            # 显示分数
            font = pygame.font.SysFont(None, 50)
            text = font.render("Game Over!", True, (255, 0, 0))
            screen.blit(text, (300, 250))
            font = pygame.font.SysFont(None, 30)
            text = font.render("Score: " + str(score), True, (255, 0, 0))
            screen.blit(text, (350, 300))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            quit()

        # 绘制飞盘
        if time_left % 100 == 0:
            # 获取当前时间
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            # 将鼠标位置和时间写入txt文件
            with open('panshow_time' + str(fg) + '.txt', 'a') as f:
                f.write(f'({now}\n')

            x = random.randint(0, 700)
            y = random.randint(50, 400)
         # 绘制圆形



        # pygame.draw.circle(screen, (0, 0, 0), (x, y), radius)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), radius+5, 1)

    # 绘制得分
    miss_score = 60 - int( time_left / 100) -score
    font = pygame.font.SysFont("黑体",18)
    text = font.render("击中个数:" + str(score)+"/"+str(miss_score), True, (255, 255, 255))
    screen.blit(text, (360, 15))

    # 更新屏幕
    pygame.display.update()

    # 设置游戏的帧率
    clock.tick(100)
