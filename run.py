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
move_up = 0
move_down = 0
move_left = 0
move_right = 0

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

pygame.mixer.init()
#   배경음
pygame.mixer.music.load('sound/bgm.mp3')
pygame.mixer.music.play(-1)


#   효과음


def set_location_player(piece_x, piece_y):
    global player_location
    player_location = [piece_x, piece_y]
    player_x = margin_dashboard + (player_location[0] * cell) + (cell - player_width) / 2
    player_y = (player_location[1] * cell) + (cell - player_height) / 2
    return [player_x, player_y]


def set_location_enemy(piece_x, piece_y):
    global enemy_location
    enemy_location = [piece_x, piece_y]
    enemy_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
    enemy_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
    return enemy_x, enemy_y


### pos에 해당하는 버튼 확인
def check_buttons(pos):
    if player_button.collidepoint(pos):
        def show_move_pointer():
            global move_up, move_down, move_left, move_right

            move_up += 100
            move_down -= 100
            move_right += 100
            move_left -= 100

            screen.blit(move, (player_x, player_y + move_up))
            screen.blit(move, (player_x, player_y + move_down))
            screen.blit(move, (player_x + move_right, player_y))
            screen.blit(move, (player_x + move_left, player_y + move_up))


#   이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(1)

    #   이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 나가기 버튼을 누르면
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()  # get_pos()으로 클릭한 위치 값 받아오기
            print(click_pos)

    if click_pos:
        check_buttons(click_pos)

    # 3. 게임 캐릭터 위치 정의
    #   좌표 값 넣어서 이동시키기
    player_x = set_location_player(9, 9)[0]
    player_y = set_location_player(9, 9)[1]

    enemy_x = set_location_enemy(1, 1)[0]
    enemy_y = set_location_enemy(1, 1)[1]

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(board, (200, 0))
    screen.blit(title, (0, 0))
    screen.blit(whitegray, (0, 200))
    screen.blit(gray, (0, 300))
    screen.blit(whitegray, (0, 500))
    screen.blit(turn, (60, 530))
    screen.blit(gray, (0, 600))
    screen.blit(whitegray, (0, 800))
    screen.blit(item, (60, 830))
    screen.blit(wood, (0, 900))
    screen.blit(pause, (58, 907))
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy, (enemy_x, enemy_y))

    pygame.display.update()  # 게임 화면을 다시 그리기!

# 게임 종료
pygame.quit()
