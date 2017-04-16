from snake.body import Direction

BODY_BLOCK = 'x'
CANDY = 'o'


def draw_candy(candy, scr):
    scr.addch(candy.y, candy.x, ord(CANDY))


def draw_body(body, scr):
    for segment in body.segments:
        for pos in range(segment.length):
            if segment.direction == Direction.RIGHT:
                scr.addch(segment.start.y, segment.start.x + pos,
                          ord(BODY_BLOCK))
            elif segment.direction == Direction.LEFT:
                scr.addch(segment.start.y, segment.start.x - pos,
                          ord(BODY_BLOCK))
            elif segment.direction == Direction.UP:
                scr.addch(segment.start.y + pos, segment.start.x,
                          ord(BODY_BLOCK))
            elif segment.direction == Direction.DOWN:
                scr.addch(segment.start.y - pos, segment.start.x,
                          ord(BODY_BLOCK))
