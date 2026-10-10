from quantcraft.backtest.runtime import account
from quantcraft.inputs import params

RSI_PERIOD = params.RSI_PERIOD if hasattr(params, "RSI_PERIOD") else 14
OVERSOLD = params.OVERSOLD if hasattr(params, "OVERSOLD") else 30.0
OVERBOUGHT = params.OVERBOUGHT if hasattr(params, "OVERBOUGHT") else 70.0
ENTRY_MA = params.ENTRY_MA if hasattr(params, "ENTRY_MA") else 20
EXIT_MA = params.EXIT_MA if hasattr(params, "EXIT_MA") else 50
QTY = params.QTY if hasattr(params, "QTY") else 10

_open: dict[str, str] = {}  # symbol -> position_id


def _sma(bar, n):
    vals = [bar.close[i] for i in range(n)]
    return None if None in vals else sum(vals) / n


def _rsi(bar, n):
    closes = [bar.close[i] for i in range(n + 1)]
    if None in closes:
        return None
    gains = losses = 0.0
    for i in range(n):  # closes[0] is the newest
        d = closes[i] - closes[i + 1]
        gains += max(d, 0.0)
        losses += max(-d, 0.0)
    if losses == 0:
        return 100.0
    return 100.0 - 100.0 / (1.0 + gains / losses)


def on_init(symbols=None):
    pass


def on_bar(bar_index, bar, fundamentals=None, symbol=None):
    if account is None:
        return
    sym = (symbol or "AAPL").upper()
    px = float(bar["close"])
    rsi = _rsi(bar, RSI_PERIOD)
    entry_ma = _sma(bar, ENTRY_MA)
    exit_ma = _sma(bar, EXIT_MA)
    if rsi is None or entry_ma is None or exit_ma is None:
        return  # not enough history yet

    if sym not in _open:
        if rsi < OVERSOLD and px < entry_ma and QTY * px <= account.cash:
            snap = account.open_trade(sym, "long", QTY, px)
            _open[sym] = snap["open_positions"][-1]["id"]
    elif rsi > OVERBOUGHT and px > exit_ma:
        account.close_trade(_open.pop(sym), px)


def on_tick(bar_index, tick_in_bar, price, bar, fundamentals=None, symbol=None):
    pass


def on_finish(bars, symbol=None, bars_by_symbol=None):
    if account is None or not bars:
        return
    sym = (symbol or "AAPL").upper()
    account.refresh_metrics({sym: float(bars[-1]["close"])})
