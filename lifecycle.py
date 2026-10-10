"""QuantCraft IDE — lifecycle methods (fill in)."""

def on_init(symbols=None):
    # symbols: tickers this run trades. With a screener symbol source this runs again at
    # every rebalance with that interval's universe, so keep it idempotent.
    print("algo init: ", symbols)


def on_tick(bar_index, tick_in_bar, price, bar, fundamentals=None, symbol=None):
    print("algo tick: ", symbol)


def on_bar(bar_index, bar, fundamentals=None, symbol=None):
    print("algo new bar: ", symbol)


def on_timer(bar_index, tick_in_bar, price, bar, fundamentals=None, symbol=None):
    # Runs only when timer_interval_ms is configured in Backtest/Forward parameters (Will not work properly in Backtest).
    pass


def on_finish(bars, symbol=None, bars_by_symbol=None):
    # bars: list of OHLC dicts for the clock symbol, oldest first (execution window).
    print("algo finished: ", symbol)
