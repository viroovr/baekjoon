class member:
    def __init__(self, num: int, size: str) -> None:
        self.__num = num
        self.__size = size
    
    @property
    def num(self) -> int:
        return self.__num

    @property
    def size(self) -> str:
        return self.__size
    
    def __repr__(self) -> str:
        return "member(%d, '%s')" % (self.__num, self.__size)
    
    def __str__(self) -> str:
        return "배번호: %d\n사이즈: %s" % (self.__num, self.__size)

marvelrun = {
    'ZANZUCCHI Noemie Clara': member(10596, 'M'),
    '강창민': member(10865, 'XL'),
    '곽민성': member(10757, 'L'),
    '곽민철': member(10858, 'XL'),
    '권서현': member(10482, 'S'),
    '권준서': member(10761, 'L'),
    '김가을': member(10947, '3XL'),
    '김기현': member(10490, 'S'),
    '김주성': member(10486, 'S'),
    '김주원': member(10866, 'XL'),
    '김주은': member(10484, 'S'),
    '김채은': member(10595, 'M'),
    '김태원': member(10870, 'XL'),
    '김태환': member(10946, '3XL'),
    '김현민': member(10868, 'XL'),
    '노신화': member(10487, 'S'),
    '두호균': member(10869, 'XL'),
    '박관우': member(10599, 'M'),
    '박현제': member(10867, 'XL'),
    '백기현': member(10864, 'XL'),
    '서동윤': member(10598, 'M'),
    '서현원': member(10765, 'L'),
    '성수정': member(10597, 'M'),
    '송태현': member(10760, 'L'),
    '신주화': member(10756, 'L'),
    '오정빈': member(10766, 'L'),
    '우대윤': member(10763, 'L'),
    '우영석': member(10758, 'L'),
    '유진영': member(10485, 'S'),
    '유호은': member(10762, 'L'),
    '윤예린': member(10759, 'L'),
    '이다송': member(10488, 'S'),
    '이다은': member(10483, 'S'),
    '이상준': member(10945, '3XL'),
    '이승훈': member(10764, 'L'),
    '이주형': member(10856, 'XL'),
    '임시우': member(10489, 'S'),
    '장소희': member(10872, 'XL'),
    '장지훈': member(10600, 'M'),
    '전재혁': member(10767, 'L'),
    '정가연': member(10871, 'XL'),
    '정무석': member(10859, 'XL'),
    '정세환': member(10863, 'XL'),
    '정승재': member(10861, 'XL'),
    '정준혁': member(10755, 'L'),
    '채서린': member(10593, 'M'),
    '최지윤': member(10594, 'M'),
    '황세진': member(10857, 'XL'),
    '최원': member(10935, '3XL'),
    '최종인': member(10931, 'XXL'),
    "원준식": member(10932, '3XL'),
    "신성구": member(10936, '3XL'),
    "나인호": member(10934, '3XL'),
    "이기호": member(10938, '3XL'),
    "김제현": member(10937, '3XL'),
}

reserved = [
    'ZANZUCCHI Noemie Clara',
    "장지훈",
    "김현민",
    "김가을",
    "김주은",
    "김주성",
    "유진영",
    "서현원",
    "장소희",
    "정가연",
    "이다송"
]

new = {
    "홍민재",
    "김승원"
}

if __name__ == "__main__":
    while True:
        name = input("이름을 입력하세요: ")
        if name in marvelrun:
            print(marvelrun[name])
            break
        print("마블런 신청자 명단에 없습니다.")
        repeat = input("다시 입력하시겠습니까? (y/n) ")
        if repeat == 'n' or repeat == 'N':
            break