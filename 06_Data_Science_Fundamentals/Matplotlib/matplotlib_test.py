import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2* np.pi, 200)
y = np.sin(x)


fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# -------------------------------------------------------------- #

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

# -------------------------------------------------------------- #
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
print(type(b))
print(type(b_asarray))

# -------------------------------------------------------------- #
np.random.seed(19680801)
data = {
    "a" : np.arange(50),
    "c" : np.random.randint(0, 50, 50),
    "d" : np.random.randn(50)
}
data["b"] = data["a"] + 10 * np.random.randn(50)
data["d"] = np.abs(data["d"]) * 100

fig, ax = plt.subplots(figsize =(5, 2.7), layout="constrained")
ax.scatter("a", "b", c="c", s="d", data=data)
ax.set_xlabel("entry a")
ax.set_ylabel("entry b")

plt.show()

# ------------- OO style ------------- #
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
ax.plot(x, x, label="linear")
ax.plot(x, x**2, label="quadratic")
ax.plot(x, x**3, label="cubic")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_title("Simple Plot")
ax.legend()
plt.show()

# ------------- pyplot-style ------------- #
x = np.linspace(0, 2, 100)
plt.figure(figsize=(5, 2.7), layout="constrained")
plt.plot(x, x, label="linear")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Simple Plot")
plt.legend()
plt.show()

# ------------- හHelper functions ------------- #
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# ------------- Example of using the helper function ------------- #
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {"marker" : "x"})
my_plotter(ax2, data3, data4, {"marker" : "o"})

plt.show()

# ------------- Styling with matplotlib ------------- #
fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color="blue", linewidth=3, linestyle="--")
l, = ax.plot(x, np.cumsum(data2), color="orange", linewidth=2)
l.set_linestyle(":")
plt.show()

# ------------- Color ------------- #
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(data1, data2, s=50, facecolor="C0", edgecolor="k")
plt.show()

# ------------- ළLinewidths, linestyles, and markersizes ------------- #
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, "o", label="data1")
ax.plot(data2, "d", label="data2")
ax.plot(data3, "v", label="data3")
ax.plot(data4, "s", label="data4")
ax.legend()
plt.show()

# ------------- Labelling plots ------------- #
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
n, bins, patches = ax.hist(x, 50, density=True, facecolor="C0", alpha=0.75)

ax.set_xlabel("Lenght [cm]")
ax.set_ylabel("Probability")
ax.set_title("Aardvark lengths\n (not really)")
ax.text(75, .025, r"$\mu=115,\sigma=15$")
ax.axis([55, 175, 0, 0.03])
ax.grid(True)
plt.show()

