import SnakeAndLadder


def test_position():
    test1 = SnakeAndLadder.SnakeAndLadder()
    assert test1.position==1
    assert test1.money_available==500
    
def test_movecheck():
    test1 = SnakeAndLadder.SnakeAndLadder()
    test1.play_onemove(1)
    assert test1.position==2
    test1.play_onemove(2)
    assert test1.position == 4

def test_laddercheck():
    test2 = SnakeAndLadder.SnakeAndLadder()
    test2.play_onemove(4)
    assert test2.position==10
    assert test2.money_available == 600
    test2.play_onemove(2)
    assert test2.position==26
    assert test2.money_available == 700
    test2.play_onemove(6)
    test2.play_onemove(3)
    assert test2.position==36
    assert test2.money_available == 800
    test2.play_onemove(4)
    assert test2.position==45
    assert test2.money_available == 900
    test3 = SnakeAndLadder.SnakeAndLadder()
    test3.play_onemove(4)
    test3.play_onemove(6)
    assert test3.position==29
    assert test3.money_available == 700

def test_snakecheck():
    test4=SnakeAndLadder.SnakeAndLadder()
    test4.play_onemove(4)
    test4.play_onemove(4)
    assert test4.position==2
    assert test4.money_available == 500
    test4.play_onemove(3)
    assert test4.position==10
    assert test4.money_available == 600
    test4.play_onemove(5)
    assert test4.position==15
    assert test4.money_available == 600
    test4.play_onemove(6)
    test4.play_onemove(2)
    assert test4.position==8
    assert test4.money_available == 500
    test4.play_onemove(4)
    test4.play_onemove(6)
    test4.play_onemove(6)
    test4.play_onemove(5)
    assert test4.position==41
    assert test4.money_available == 500
    test4.play_onemove(6)
    assert test4.position==37
    assert test4.money_available == 400






