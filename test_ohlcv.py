from quantcraft import Timeframe
import quantcraft.runtime as rt

# Primary timeframe + 3 secondary timeframes.
# Run with chart timeframe = 1Min, and pick 5Min, 15Min, 1Hour under "Additional timeframes".
TIMEFRAMES = [Timeframe.M1, Timeframe.M5, Timeframe.M15, Timeframe.H1]
LOOKBACK = 3  # last 3 completed candles (shift 1..3), newest first


def on_init(symbols=None):
    print(f"[init] logging {[tf.value for tf in TIMEFRAMES]} x last {LOOKBACK} candles on every tick")


def on_tick(bar_index, tick_in_bar, price, bar, symbol=None):
    print(f"--- tick {symbol} price={price:.4f} ---")
    for tf in TIMEFRAMES:
        parts = []
        for shift in range(1, LOOKBACK + 1):
            snap = rt.get_bar(tf, shift=shift)
            parts.append("n/a" if snap is None else f"{snap.t}={snap.close:.4f}")
        print(f"{tf.value:>6}: " + " | ".join(parts))


def on_bar(bar_index, bar, symbol=None):
    pass


def on_finish(bars=None, symbol=None, bars_by_symbol=None):
    pass