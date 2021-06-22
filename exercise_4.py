import turtle
from functools import partial


def parse_line(line) -> None:
    """
    Parse a line of command

    :param line: line of commands to parse, assumption: command and arg separated by a space
    :return: None
    """
    cmd_lst = line.split(" ")
    arg = None
    if len(cmd_lst) == 1:
        cmd = cmd_lst[0]
    elif len(cmd_lst) == 2:
        cmd, arg = cmd_lst
    else:
        raise NotImplementedError('Command format not accepted! Only accepting "CMD" or "CMD ARG".')
    try:
        func = CMD_FUNC_MAP[cmd]
    except KeyError:
        raise KeyError('Unknown command: ' + cmd)
    if arg is not None:
        func(arg)
    else:
        func()


def pen(size=2):
    turtle.pen(pensize=size)


def draw(distance, to_angle=0):
    turtle.setheading(to_angle=to_angle)
    turtle.forward(distance=int(distance))


CMD_FUNC_MAP = {
    'P': pen,
    'D': turtle.pendown,
    'W': partial(draw, to_angle=180),
    'N': partial(draw, to_angle=90),
    'E': partial(draw, to_angle=0),
    'S': partial(draw, to_angle=270),
    'U': turtle.penup
}


def parse_file(fp):
    with open(fp) as f:
        content = f.read()

    for line in content.split('\n'):
        parse_line(line)


def main():
    parse_file('ex4.txt')


if __name__ == '__main__':
    main()
    input()
