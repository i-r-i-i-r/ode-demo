# http://www.physics.okayama-u.ac.jp/~otsuki/lecture/CompPhys2/ode/ode.html#id12
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.BDF.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

# 動作確認
# 複数変数、複数パラメータの常微分方程式

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 微分方程式を設定
def derivfun(t, y, a, b): 
    dy1dt = 1
    dy2dt = 2
    return [dy1dt, dy2dt]

# 解析の設定
t_start = 0
t_end = 10
y0 = [5, 0] # [y1, y2]
a = 15
b = -0.1
t_eval=[0, 5.5, 6, 7.5] # サンプリングのタイミングを指定

# 解析実行
sol = solve_ivp(derivfun, (t_start, t_end), y0, args=(a,b), method='BDF')
sol1 = solve_ivp(derivfun, (t_start, t_end), y0, args=(a,b), method='BDF', t_eval=t_eval)

# 結果確認
# sol.y はndarray型
plt.plot(sol.t, sol.y[0], color = "k", marker="*")
plt.plot(sol.t, sol.y[1], color = "orange", marker="*")
plt.plot(sol1.t, sol1.y[0], color = "blue", marker="o", linestyle="none")
plt.plot(sol1.t, sol1.y[1], color = "red", marker="o", linestyle="none")
plt.xlabel('t')
plt.grid()
plt.show()

