"""QuantCraft IDE — lifecycle methods (fill in)."""
import quantcraft.process.runtime as rt

from rsi_ma_algo.charting.plot import plot_line
from rsi_ma_algo.indicators.technical import moving_average, rsi

MA_PERIOD, RSI_PERIOD = 50, 14
RSI_BUY_BELOW, RSI_SELL_ABOVE = 30, 70

DOLLARS_PER_TRADE = 10_000

indicator_history = {}
SYMBOL = "AAPL"


holding = set()

def on_init(symbols=None):
    # symbols: tickers this run trades. With a screener symbol source this runs again at
    # every rebalance with that interval's universe, so keep it idempotent.
    pass


def on_tick(bar_index, tick_in_bar, price, bar, fundamentals=None, symbol=None):
    pass


def on_bar(bar_index, bar, fundamentals=None, symbol=None):
    symbol = (symbol or SYMBOL).upper()
    ma_value = moving_average(bar, MA_PERIOD, shift=1)
    rsi_value = rsi(bar, RSI_PERIOD, shift=1)
    prev_time = bar.t[1]
    indicator_history.setdefault(symbol, []).append((prev_time, ma_value, rsi_value))

    # EnTRY/ExIt logic
    price = float(bar["close"])
    prev_close = bar.close[1]

    if prev_close is None or ma_value is None or rsi_value is None:
        return

    uptrend = prev_close > ma_value
    if symbol not in holding and uptrend and rsi_value < RSI_BUY_BELOW:
        shares = int(min(DOLLARS_PER_TRADE, rt.account.cash * 0.95) // price)
        if shares:
            rt.account.open_trade(symbol, "long", shares, price)
            rt.qc_ohlcv_by_symbol
            holding.add(symbol)
            print(
                f"{bar['t']} BUY {symbol} x{shares} @ {price:.2f} RSI={rsi_value:.0f} MA={ma_value:.4f}"
            )
    elif symbol in holding and (rsi_value > RSI_SELL_ABOVE or not uptrend):
        rt.account.close_all_longs(price, symbol=symbol)
        holding.discard(symbol)
        print(
            f"{bar['t']} SELL {symbol} @ {price:.2f} RSI={rsi_value:.0f} MA={ma_value:.4f}"
        )


def on_timer(bar_index, tick_in_bar, price, bar, fundamentals=None, symbol=None):
    # Runs only when timer_interval_ms is configured in Backtest/Forward parameters (Will not work properly in Backtest).
    pass


def on_finish(bars, symbol=None, bars_by_symbol=None):
    # bars: list of OHLC dicts for the clock symbol, oldest first (execution window).
    for symbol, rows in indicator_history.items():
        rsi_pane = f"rsi_{symbol}"
        plot_line(symbol, f"SMA({MA_PERIOD})", [(t, ma) for t, ma, _ in rows])
        plot_line(symbol, f"RSI({RSI_PERIOD})", [(t, rsi) for t, _, rsi in rows], pane=rsi_pane)

        for level, label in ((RSI_SELL_ABOVE, "overbought"), (RSI_BUY_BELOW, "oversold")):
            plot_line(symbol, f"{label} ({level})", [(t, level) for t, _, _ in rows], pane=rsi_pane, style="dotted")
















