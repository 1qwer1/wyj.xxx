import dataset
from matplotlib import pyplot as plt
xs,ys=dataset.get_beans(100)
print(xs)
print(ys)

plt.rcParams["font.sans-serif"] = "SimHei"
plt.title("y=wx",fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
#y=0.5x w=0.5
w=0.5
for m in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        y_pre = w * x
        e = y - y_pre
        alpha = 0.05
        w = w + alpha * e * x
y_pre = w * xs
plt.scatter(xs,ys)
plt.plot(xs,y_pre)
plt.show()