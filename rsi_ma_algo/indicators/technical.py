def moving_average(bar, period, shift):
    closes = [bar.close[shift + i] for i in range(period)]
    return None if None in closes else sum(closes) / period

def rsi(bar, period, shift):
    closes = [bar.close[shift + i] for i in range(period + 1)]
    if None in closes:
        return None

    moves = [closes[i] - closes[i + 1] for i in range(period)]
    gains, losses = sum(m for m in moves if m > 0), -sum(m for m in moves if m < 0)

    return 100.0 if losses == 0 else 100 - 100 / (1 + gains / losses)
    