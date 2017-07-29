#utf-8
from pytdx.log import DEBUG, log


class TdxHqPool_API:
    """
    实现一个连接池的机制
    包含：

    1 1个正在进行数据通信的主连接
    2 1～n个备选连接，备选连接也连接到服务器，通过心跳包维持连接，当主连接通讯出现问题时，备选连接立刻转化为主连接
    3 m个ip构成的ip池，可以通过某个方法获取列表，列表可以进行排序，如果备选连接缺少的时候，我们根据排序的优先级顺序将其追加到备选连接
    """
