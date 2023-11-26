CLR = tuple[int, int, int]


class COLOR:
    BLACK: CLR = (0, 0, 0)
    GREY: CLR = (128, 128, 128)
    GRAY: CLR = GREY
    WHITE: CLR = (255, 255, 255)
    RED: CLR = (255, 0, 0)
    GREEN: CLR = (0, 255, 0)
    BLUE: CLR = (0, 0, 255)

    def all() -> list[CLR]:
        return list[
            COLOR.BLACK,
            COLOR.GRAY,
            COLOR.WHITE,
            COLOR.RED,
            COLOR.GREEN,
            COLOR.BLUE
        ]
