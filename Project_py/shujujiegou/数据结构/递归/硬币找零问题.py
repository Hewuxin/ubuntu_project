import time


def recMC(coinValueList, change):
    """
    递归解决
    :param coinValueList:
    :param change:
    :return:
    """
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def recDC(coinValueList, change, knownResults):
    """
    递归改进 消除重复计算
    :param coinValueList:
    :param change:
    :param knownResults:
    :return:
    """
    mincoins = change
    if change in coinValueList:
        knownResults[change] = 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numcoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numcoins < mincoins:
                mincoins = numcoins
                knownResults[change] = mincoins
    return mincoins


if __name__ == "__main__":
    coin = [1, 5, 10, 25]
    demo = [0]*64
    print(time.clock())
    print(recMC(coin, 63))
    print(time.clock())
    #
    # print(time.clock())
    # print(recDC(coin, 63, demo))
    # print(time.clock())
