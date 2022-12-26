# http://www.physics.okayama-u.ac.jp/~otsuki/lecture/CompPhys2/ode/ode.html#id12
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.BDF.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

# https://qiita.com/termoshtt/items/48788da8ee0994bbfaa0

# 動作確認
# 硬い方程式

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 微分方程式を設定
def derivfun(t, y, a, b): # 導関数は共通
    dydt = -a * y + b
    return dydt

# 解析の設定
t_start = 0
t_end = 1
y0 = [10, 20, -10] # 初期値いろいろ
a = 15
b = 0.1

# 解析実行
sol = solve_ivp(derivfun, (t_start, t_end), y0, args=(a,b), method='BDF')

# 結果確認
plt.plot(sol.t, sol.y[0], color = "k", marker="o")
plt.plot(sol.t, sol.y[1], color = "orange", marker="o")
plt.plot(sol.t, sol.y[2], color = "blue", marker="o")
plt.xlabel('t')
plt.grid()
plt.show()

