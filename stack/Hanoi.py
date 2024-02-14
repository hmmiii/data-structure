
def hanoi_tower(n, fr, tmp, to):
    """
    하노이 탑 문제를 해결하는 함수

    Parameters:
    - n (int): 원판의 수
    - fr (str): 시작 막대
    - tmp (str): 임시 막대
    - to (str): 목표 막대
    """
    
    if(n==1):
        print("원판 1: %s --> %s" % (fr,to)) # 순환 호출을 멈추는 부분. 원판이 하나라면 바로 이동.
    else:
        hanoi_tower(n-1, fr, to, tmp) # 1단계 : fr막대에 있는 n-1개의 원판을 to 막대를 이용해 tmp로 옮김
        print("원판 %d: %s --> %s" % (n,fr,to)) # 2단계 : fr에 있는 하나의 원판을 바로 to로 옮김.
        hanoi_tower(n-1, tmp, fr, to) # 3단계 : 마지막으로 tmp에 있는 n-1개의 원판을 fr을 이용해 to로 옮김

hanoi_tower(4, 'A', 'B', 'C')