import pygame

# 1. 기본 초기화(반드시 해야됨)
pygame.init()
#   화면 크기 설정
screen_width = 1200  # 가로
screen_height = 1000  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
#   화면 타이틀
pygame.display.set_caption("Battle Chess")
#   Frame Per Second
clock = pygame.time.Clock()

# 2. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도)
#   cell size
margin_dashboard = 200
cell = 100

# 피스 위치 좌표
default_player = 0
default_enemy = 9
piece_x = 0
piece_y = 0
player_location = [piece_x, piece_y]
enemy_location = [piece_x, piece_y]
king_location = [piece_x, piece_y]

# 클릭 좌표 값
click_pos = 0

# 이동전 보여주기용 (현재 사용하지 않음)
# move_preview = False

# 방향키 값
key = 0

# 스테이지 움직임 제한
stage_count = 30

# 폰트 설정
game_font = pygame.font.Font(None,150)
game_font2 = pygame.font.Font(None, 80)

# 색상값
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 게임 화면 분기
start = False

king_count = 1

#   체스 보드
board = pygame.image.load('img/ChessBoard.png')
#   플레이어 피스
player = pygame.image.load('img/Player.png')
player_size = player.get_size()
player_width = player_size[0]
player_height = player_size[1]
player_x = margin_dashboard + (player_location[0] * cell) + (cell - player_width) / 2
player_y = (player_location[1] * cell) + (cell - player_height) / 2
player_button = pygame.Rect(player_x, player_y, player_width, player_height)
#   에너미 피스
enemy = pygame.image.load('img/Enemy.png')
enemy_size = enemy.get_size()
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
enemy_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
enemy_button = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

enemy2_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
enemy2_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
enemy2_button = pygame.Rect(enemy2_x, enemy2_y, enemy_width, enemy_height)

enemy3_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
enemy3_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
enemy3_button = pygame.Rect(enemy3_x, enemy3_y, enemy_width, enemy_height)

enemy4_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
enemy4_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
enemy4_button = pygame.Rect(enemy4_x, enemy4_y, enemy_width, enemy_height)

# 킹 피스
king = pygame.image.load('img/King.png')
king_size = king.get_size()
king_width = king_size[0]
king_height = king_size[1]
king_x = margin_dashboard + (king_location[0] * cell) + (cell - king_width) / 2
king_y = (king_location[1] * cell) + (cell - king_height) / 2
king_button = pygame.Rect(king_x, king_y, king_width, king_height)

# 게임스타트 버튼
game_start_button = pygame.Rect(150, 500, 1000, 200)

#   킹 피스
king = pygame.image.load('img/King.png')
#   일시정지 아이콘
pause = pygame.image.load('img/Pause.png')
#   대시보드 테두리
gray = pygame.image.load('img/DarkGray.png')
#   대시보드 설명 테두리
whitegray = pygame.image.load('img/grayback.png')
#   타이틀 이미지
title = pygame.image.load('img/Title.png')
#   일시정지 테두리
wood = pygame.image.load('img/wood.png')
#   스테이지
stage_1 = pygame.image.load('img/Stage_1.png')
stage_2 = pygame.image.load('img/Stage_2.png')
stage_3 = pygame.image.load('img/Stage_3.png')
stage_4 = pygame.image.load('img/Stage_4.png')
stage_5 = pygame.image.load('img/Stage_5.png')
turn = pygame.image.load('img/TURN.png')
item = pygame.image.load('img/ITEM.png')
move = pygame.image.load('img/move.png')
title_screen = pygame.image.load('img/title_screen.jpg')

# 배경음 세팅
pygame.mixer.init()
#   배경음
pygame.mixer.music.load('sound/bgm.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
#   효과음
sound_move = pygame.mixer.Sound('sound/se_move.wav')
sound_crash = pygame.mixer.Sound('sound/crash.wav')


# 함수
def set_location_player(x, y):
    global player_location, player_button, player_x, player_y
    player_location = [x, y]
    player_x = margin_dashboard + (player_location[0] * cell) + (cell - player_width) / 2
    player_y = (player_location[1] * cell) + (cell - player_height) / 2
    player_button = pygame.Rect(player_x, player_y, player_width, player_height)
    return [player_x, player_y]


def set_location_enemy(x, y):
    global enemy_location
    enemy_location = [x, y]
    enemy_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
    enemy_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
    return enemy_x, enemy_y


def set_location_king(x, y):
    global enemy_location
    enemy_location = [x, y]
    enemy_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
    enemy_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
    return enemy_x, enemy_y


# 피스 초기 좌표 위치 설정
player_x = set_location_player(4, 7)[0]
player_y = set_location_player(4, 7)[1]

enemy_x = set_location_enemy(0, 0)[0]
enemy_y = set_location_enemy(0, 0)[1]

enemy2_x = set_location_enemy(9, 0)[0]
enemy2_y = set_location_enemy(9, 0)[1]

enemy3_x = set_location_enemy(2, 2)[0]
enemy3_y = set_location_enemy(2, 2)[1]

enemy4_x = set_location_enemy(7, 2)[0]
enemy4_y = set_location_enemy(7, 2)[1]

king_x = set_location_enemy(5, 0)[0]
king_y = set_location_enemy(5, 0)[1]


# 플레이어 무브 기능
def player_move(key):
    global player_x, player_y, sound_move, stage_count
    sound_move.play()
    if key == 'up':
        player_y -= 100
        stage_count -= 1

    elif key == 'down':
        player_y += 100
        stage_count -= 1
    elif key == 'left':
        player_x -= 100
        stage_count -= 1
    elif key == 'right':
        player_x += 100
        stage_count -= 1
    else:
        print('잘못된 입력입니다')
    return player_x, player_y, key


def attck_enemy(key):
    # 캐릭터 피스는 이동하려는 모션
    print(f'플레이어 피스가 공격하려 합니다. 공격방향은 {key}')
    global player_x, player_y, sound_crash, stage_count, enemy_x
    sound_crash.play()
    if key == 'up':
        player_y += 100
        enemy_x = -500
    elif key == 'down':
        player_y -= 100
        enemy_x = -500
    elif key == 'left':
        player_x += 100
        enemy_x = -500
    elif key == 'right':
        player_x -= 100
        enemy_x = -500
    else:
        print('잘못된 시도입니다 : attack_enemy()')
    return player_x, player_y


def attck_enemy2(key):
    # 캐릭터 피스는 이동하려는 모션
    print(f'플레이어 피스가 공격하려 합니다. 공격방향은 {key}')
    global player_x, player_y, sound_crash, stage_count, enemy2_x
    sound_crash.play()
    if key == 'up':
        player_y += 100
        enemy2_x = -500
    elif key == 'down':
        player_y -= 100
        enemy2_x = -500
    elif key == 'left':
        player_x += 100
        enemy2_x = -500
    elif key == 'right':
        player_x -= 100
        enemy2_x = -500
    else:
        print('잘못된 시도입니다 : attack_enemy()')
    return player_x, player_y


def attck_enemy3(key):
    # 캐릭터 피스는 이동하려는 모션
    print(f'플레이어 피스가 공격하려 합니다. 공격방향은 {key}')
    global player_x, player_y, sound_crash, stage_count, enemy3_x
    sound_crash.play()
    if key == 'up':
        player_y += 100
        enemy3_x = -500
    elif key == 'down':
        player_y -= 100
        enemy3_x = -500
    elif key == 'left':
        player_x += 100
        enemy3_x = -500
    elif key == 'right':
        player_x -= 100
        enemy3_x = -500
    else:
        print('잘못된 시도입니다 : attack_enemy()')
    return player_x, player_y


def attck_enemy4(key):
    # 캐릭터 피스는 이동하려는 모션
    print(f'플레이어 피스가 공격하려 합니다. 공격방향은 {key}')
    global player_x, player_y, sound_crash, stage_count, enemy4_x
    sound_crash.play()
    if key == 'up':
        player_y += 100
        enemy4_x = -500
    elif key == 'down':
        player_y -= 100
        enemy4_x = -500
    elif key == 'left':
        player_x += 100
        enemy4_x = -500
    elif key == 'right':
        player_x -= 100
        enemy4_x = -500
    else:
        print('잘못된 시도입니다 : attack_enemy()')
    return player_x, player_y


def attck_king(key):
    # 캐릭터 피스는 이동하려는 모션
    print(f'플레이어 피스가 공격하려 합니다. 공격방향은 {key}')
    global player_x, player_y, sound_crash, stage_count, king_x, king_count
    sound_crash.play()
    if key == 'up':
        player_y += 100
        king_x = -500
        king_count = 0
    elif key == 'down':
        player_y -= 100
        king_x = -500
        king_count = 0
    elif key == 'left':
        player_x += 100
        king_x = -500
        king_count = 0
    elif key == 'right':
        player_x -= 100
        king_x = -500
        king_count = 0
    else:
        print('잘못된 시도입니다 : attack_enemy()')
    return player_x, player_y


def display_title():
    screen.blit(title_screen, (0, 0))


def display_game():
    screen.blit(board, (200, 0))
    screen.blit(title, (0, 0))
    screen.blit(whitegray, (0, 200))
    screen.blit(stage_1, (0, 215))
    screen.blit(gray, (0, 300))
    screen.blit(move_timer, (40, 350))
    screen.blit(whitegray, (0, 500))
    screen.blit(turn, (60, 530))
    screen.blit(gray, (0, 600))
    screen.blit(whitegray, (0, 800))
    screen.blit(item, (60, 830))
    screen.blit(wood, (0, 900))
    screen.blit(pause, (58, 907))
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    screen.blit(enemy, (enemy2_x, enemy2_y))
    screen.blit(enemy, (enemy3_x, enemy3_y))
    screen.blit(enemy, (enemy4_x, enemy4_y))
    screen.blit(king, (king_x, king_y))


### pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if game_start_button.collidepoint(pos):
        start = True

    return start


#     if player_button.collidepoint(pos):
#         global move_preview
#
#         # if move_preview == False
#         if not move_preview:
#             move_preview = True
#             move_up = -100
#             move_down = 100
#             move_right = 100
#             move_left = -100
#             # print(move_up,move_down, move_left, move_right)
#             move_up += player_y
#             move_down += player_y
#             move_right += player_x
#             move_left += player_x
#             # print(move_up, move_down, move_left, move_right)
#             screen.blit(move, (player_x, move_up))
#             screen.blit(move, (player_x, move_down))
#             screen.blit(move, (move_left, player_y))
#             screen.blit(move, (move_right, player_y))
#             pygame.display.update()
#             return move_preview
#         else:
#             move_preview = False
#             move_up = -100
#             move_down = 100
#             move_right = 100
#             move_left = -100
#             # print(move_up,move_down, move_left, move_right)
#             move_up += player_y
#             move_down += player_y
#             move_right += player_x
#             move_left += player_x
#             # print(move_up, move_down, move_left, move_right)
#             screen.blit(king, (player_x, move_up))
#             screen.blit(king, (player_x, move_down))
#             screen.blit(king, (move_left, player_y))
#             screen.blit(king, (move_right, player_y))
#             pygame.display.update()
#             return move_preview

def game_over():
    msg = game_font.render('GAME OVER', True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))
    msg2 = game_font2.render('--THANK YOU FOR PLAY--', True, WHITE)
    msg2_rect = msg.get_rect(center=(screen_width / 2 -30, screen_height / 2 + 100))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)
    screen.blit(msg2, msg2_rect)


    global running
    running = False
    print('게임을 진짜 종료합니다')
    return running

def game_clear():
    global running
    msg = game_font.render('STAGE CLEAR!', True, WHITE)
    msg2 = game_font2.render('--THANK YOU FOR PLAY--', True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))

    msg2_rect = msg.get_rect(center=(screen_width / 2 +40, screen_height / 2 + 100))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)
    screen.blit(msg2, msg2_rect)

    running = False


#   이벤트 루프

running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(2)

    #   이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 나가기 버튼을 누르면
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('input K_UP')
                key = player_move('up')[2]
            elif event.key == pygame.K_DOWN:
                print('input K_DOWN')
                key = player_move('down')[2]
            elif event.key == pygame.K_LEFT:
                print('input K_LEFT')
                key = player_move('left')[2]
            elif event.key == pygame.K_RIGHT:
                print('input K_RIGHT')
                key = player_move('right')[2]

        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()  # get_pos()으로 클릭한 위치 값 받아오기
            print(click_pos)

            if click_pos:
                check_buttons(click_pos)

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    player_button = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_button = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemy2_button = pygame.Rect(enemy2_x, enemy2_y, enemy_width, enemy_height)
    enemy3_button = pygame.Rect(enemy3_x, enemy3_y, enemy_width, enemy_height)
    enemy4_button = pygame.Rect(enemy4_x, enemy4_y, enemy_width, enemy_height)
    king_button = pygame.Rect(king_x, king_y, king_width, king_height)

    # print(f'player_button: {player_button}, enemy_button: {enemy_button}')

    #   체스말이 화면 밖으로 나가지 못하게 하기
    if player_x < 200:
        player_x = 207
    elif player_x > 1200:
        player_x = 1107
    elif player_y < 0:
        player_y = 7
    elif player_y > 1000:
        player_y = 907
    #   캐릭터와 충돌하면, 이동을 못하게 막음
    # print(f'플레이어피스: {player_button} 에너미3피스: {enemy3_button}')

    if player_button.colliderect(enemy_button):
        print('피스 충돌')
        attck_enemy(key)
    elif player_button.colliderect(enemy2_button):
        print('피스 충돌')
        attck_enemy2(key)
    elif player_button.colliderect(enemy3_button):
        print('피스 충돌')
        attck_enemy3(key)
    elif player_button.colliderect(enemy4_button):
        print('피스 충돌')
        attck_enemy4(key)
    elif player_button.colliderect(king_button):
        print('피스 충돌')
        attck_king(key)

    # 게임 폰트
    # str.zfill(자릿수) 로 0 채워넣어 모양 만들기
    move_timer = game_font.render(str(stage_count).zfill(2), True, WHITE)

    # 5. 화면에 그리기
    if start:
        display_game()
    else:
        display_title()

    if king_count == 0:
        print('게임클리어 진입')
        game_clear()

    if stage_count == 0:
        print('게임종료 진입')
        game_over()

    pygame.display.update()  # 게임 화면을 다시 그리기!

# 바로 게임이 종료되지 않게 하기
pygame.time.delay(3000)

# 게임 종료
pygame.quit()
