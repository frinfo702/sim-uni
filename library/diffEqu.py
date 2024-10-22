import numpy as np

def solve_system(a, b, c, d, X0, Y0, t, dXdt, dYdt):
    # 時間ステップの計算
    dt = t[1] - t[0]
    
    # 結果を格納するリストの初期化
    X = [X0]
    Y = [Y0]
    
    # オイラー法のループ
    for i in range(1, len(t)):
        X_new = X[-1] + dt * dXdt(X[-1], Y[-1], a, b)
        Y_new = Y[-1] + dt * dYdt(X[-1], Y[-1], c, d)
        X.append(X_new)
        Y.append(Y_new)
    
    return np.array(X), np.array(Y)




