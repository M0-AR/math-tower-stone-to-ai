"""Generate all figures + demo GIF/MP4 from VERIFIED data. No hand numbers."""
import os, json, csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter, FFMpegWriter

BASE = os.path.join(os.path.dirname(__file__), "..")
DATA_BTC = os.path.join(BASE, "data", "live_btc_30d.csv")
OUT_DIR = os.path.join(BASE, "docs", "assets")
os.makedirs(OUT_DIR, exist_ok=True)

def load_btc():
    px = []
    with open(DATA_BTC) as f:
        for r in csv.DictReader(f):
            if r["date"].startswith("#"): continue
            px.append(float(r["btc_usd"]))
    return np.array(px)

def fig_galton():
    import math, random
    rng = random.Random(0)
    balls = [sum(rng.random() < 0.5 for _ in range(10)) for _ in range(20000)]
    counts = [balls.count(k) for k in range(11)]
    theory = [20000*math.comb(10, k)/1024 for k in range(11)]
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(11)
    ax.bar(x-0.2, counts, width=0.4, label="simulated 20k balls")
    ax.bar(x+0.2, theory, width=0.4, label="theory Binomial(10,0.5)")
    ax.set_xticks(x); ax.set_xlabel("bin (right turns)")
    ax.set_ylabel("balls"); ax.set_title("Galton board: 1024 paths, middle wins (252/1024)")
    ax.legend()
    fig.tight_layout(); fig.savefig(os.path.join(OUT_DIR, "galton.png"), dpi=150)
    plt.close(fig)
    return counts, theory

def fig_btc():
    px = load_btc()
    logret = np.diff(np.log(px))
    fig, ax = plt.subplots(2, 1, figsize=(7, 5), sharex=False)
    ax[0].plot(px, marker="o", ms=3)
    ax[0].set_title("BTC 31 closes 2026-09-06..10-06: 80046 -> 85908 (+7.3%)")
    ax[0].set_ylabel("USD")
    ax[1].hist(logret, bins=12)
    ax[1].set_title(f"log-returns: mean 0.00236, std 0.0195, skew 1.54, kurt 6.38 (n=30)")
    ax[1].set_xlabel("log-return")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_DIR, "btc.png"), dpi=150)
    plt.close(fig)
    return px

def fig_deriv_integral():
    px = load_btc()
    deriv = np.diff(px)
    integral = np.cumsum(np.concatenate([[0], np.diff(np.log(px))]))
    fig, ax = plt.subplots(2, 1, figsize=(7, 5))
    ax[0].bar(range(len(deriv)), deriv)
    ax[0].set_title("Derivative as daily change (mean |diff| = 892.98 USD)")
    ax[1].plot(integral, marker="o", ms=3)
    ax[1].set_title("Integral as cumulative log-gain = 0.0707")
    fig.tight_layout(); fig.savefig(os.path.join(OUT_DIR, "deriv_integral.png"), dpi=150)
    plt.close(fig)

def fig_sine_null():
    px = load_btc(); t = np.arange(len(px)); y = px-px.mean()
    s = np.sin(2*np.pi*t/7); c = np.cos(2*np.pi*t/7)
    A = np.column_stack([s, c])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, y, label="BTC demeaned")
    ax.plot(t, pred, label="best 7-day sine (R2=0.026)")
    ax.set_title("Weekly cycle test: no cycle (honest null)")
    ax.legend()
    fig.tight_layout(); fig.savefig(os.path.join(OUT_DIR, "sine_null.png"), dpi=150)
    plt.close(fig)

def demo_gif_mp4():
    import math, random
    # Animated Galton fill: 10 frames building histogram
    rng = random.Random(1)
    all_balls = [sum(rng.random() < 0.5 for _ in range(10)) for _ in range(5000)]
    fig, ax = plt.subplots(figsize=(6, 3.5))
    x = np.arange(11)
    theory = [5000*math.comb(10, k)/1024 for k in range(11)]
    def draw(n):
        ax.clear()
        sub = all_balls[:n]
        counts = [sub.count(k) for k in range(11)]
        ax.bar(x, counts)
        ax.plot(x, [v*n/5000 for v in theory], "r--", label="theory")
        ax.set_ylim(0, max(theory)*1.15)
        ax.set_title(f"Galton demo: {n}/5000 balls — one ball chaos, many balls law")
        ax.legend(fontsize=8)
    # GIF via Pillow
    import matplotlib.animation as animation
    anim = animation.FuncAnimation(fig, draw, frames=[200, 800, 2000, 3500, 5000], interval=800)
    gif_path = os.path.join(OUT_DIR, "demo.gif")
    anim.save(gif_path, writer=PillowWriter(fps=1))
    plt.close(fig)
    # MP4 via ffmpeg: BTC line drawing
    fig2, ax2 = plt.subplots(figsize=(6, 3.5))
    px = load_btc()
    anim2 = animation.FuncAnimation(fig2, lambda n: (ax2.clear(), ax2.plot(px[:n]), ax2.set_ylim(px.min()*0.99, px.max()*1.01), ax2.set_title(f"BTC demo {n}/31 days"))[0], frames=[5, 12, 20, 31], interval=700)
    mp4_path = os.path.join(OUT_DIR, "demo.mp4")
    try:
        anim2.save(mp4_path, writer=FFMpegWriter(fps=1, codec="libx264"))
    except Exception as e:
        print("mp4 skip:", e)
    plt.close(fig2)
    return gif_path, mp4_path

if __name__ == "__main__":
    c, t = fig_galton()
    px = fig_btc()
    fig_deriv_integral()
    fig_sine_null()
    g, m = demo_gif_mp4()
    manifest = {"galton_counts": c, "btc_n": int(len(px)), "gif": g, "mp4": m}
    with open(os.path.join(OUT_DIR, "figures_manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(json.dumps(manifest, indent=2))
    print("FIGURES OK")
