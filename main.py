import curses
# TODO Может сделать отдельно страницу импортов?
from factory.graphics import draw_square, draw_circle
from terrain.level import level
# import terrain.template.level_1 as l1
# level1 = l1.level1
import time




def main(stdscr):
    
    curses.curs_set(0)  # Скрыть курсор
        # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Красный текст на черном фоне
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Зеленый текст на черном фоне
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Синий текст на белом фоне
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)


    

    level1 = []
            

    for _ in range(100):
        level1.append(
            [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)},
            ]
        )

    level1[3] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "Ÿ", "color": curses.color_pair(8)},
                {"symbol": "█", "color": curses.color_pair(6)},   
            ]
    level1[11] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},   
            ]
    level1[12] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},   
            ]
    level1[13] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},   
            ]
    level1[14] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)},   
            ]
    level1[15] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)},
                {"symbol": "█", "color": curses.color_pair(6)}, 
            ]
    
    level1[30] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "⧫", "color": curses.color_pair(4)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)}, 
            ]
    level1[31] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "⧫", "color": curses.color_pair(4)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)}, 
            ]
    level1[32] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "⧫", "color": curses.color_pair(4)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)}, 
            ]        

    level1[55] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)}, 
            ]
    level1[56] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)}, 
            ]
    level1[57] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)}, 
            ]
    level1[66] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "⧫", "color": curses.color_pair(4)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(6)}, 
            ]
    level1[77] = [
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "█", "color": curses.color_pair(7)},
                {"symbol": "Ψ", "color": curses.color_pair(2)},
                {"symbol": "█", "color": curses.color_pair(6)}, 
            ]
    


    for hor in range(0, 100):
        
        stdscr.addch(20, hor+10, level1[hor][0]["symbol"], level1[hor][0]["color"])
        stdscr.addch(21, hor+10, level1[hor][1]["symbol"], level1[hor][1]["color"])
        stdscr.addch(22, hor+10, level1[hor][2]["symbol"], level1[hor][2]["color"])
        stdscr.addch(23, hor+10, level1[hor][3]["symbol"], level1[hor][3]["color"])
    
    hero_position = 13

    while True:
        # stdscr.addstr(20, 10, "#", curses.color_pair(1))
        # stdscr.addstr(21, 10, "#", curses.color_pair(1))






        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            # stdscr.addstr(10, 10, "Left arrow key pressed", curses.color_pair(1))
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(7))
            hero_position -= 1
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(8))
        elif key == curses.KEY_RIGHT:
            # stdscr.addstr(10, 10, "Right arrow key pressed", curses.color_pair(2))
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(7))
            hero_position += 1
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(8))
        elif key == ord(' '):
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(7))
            hero_position += 1
            
            stdscr.addch(21, hero_position, "Ÿ", curses.color_pair(8))
            hero_position += 1
            time.sleep(0.5)
            stdscr.addch(21, hero_position, "Ÿ", curses.color_pair(8))
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(7))
            # stdscr.refresh()
            
            
            hero_position += 3
            stdscr.addch(22, hero_position, "Ÿ", curses.color_pair(8))
        elif key == ord('q') or key == 27:
            break

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)