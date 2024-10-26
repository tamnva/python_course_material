#-----------------------------------------------------------------------------#
#         The link to this code is in the video description                   # 
# For Sypder users: You could change the way your plot appears in Spyder by   #
# Tools => Preferences => IPython Console => Graphics => Inline Backend       #
# => (Resolution = 600, Width = 7, Height = 3)                                #
#-----------------------------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.arange(100)
y = x + np.random.rand(100) * 20
z = np.random.normal(50, 10, 1000)

# Set font size
plt.rcParams['font.size'] = 15

# Explicit vs. implicit https://matplotlib.org/stable/api/index.html
# Implicit approach - Define Figures and Subfigures/Axes directly using pyplot

# Line plot
plt.plot(x, y, marker='*', alpha=0.5, c="blue", label='my line')
plt.plot(x, y*3, linestyle='solid', linewidth=2, alpha=0.5, label="other line")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("my first plot")
plt.legend()
plt.show()

# Scatter plot
plt.scatter(x, y, alpha=0.5, c=y, s=40)
plt.show()

# Fill between two lines
plt.fill_between(x, y-20, y+20, color="blue", alpha=0.2, label="uncertainty band")
plt.plot(x, y, c="blue", label="best prediction")
plt.legend()
plt.show()

# Histogram plot
plt.hist(z, bins=15, rwidth=0.8, alpha=0.5)
plt.show()

# Stack plot
plt.stackplot(x, y, y*2, y*3, labels=["solar", "wind", "nuclear power"])
plt.legend(loc="upper left")
plt.show()

# Pie plot
plt.pie(y[0:4], labels=["a", "b", "c", "d"])
plt.show()

# Heat map plot
plt.pcolormesh(x[0:10], x[0:10], np.random.random((10, 10)), cmap="autumn")
plt.colorbar()
plt.show()



# Explicit approach------------------------------------------------------------
fig, ((axs1, axs2), (axs3, axs4))= plt.subplots(nrows=2, ncols=2, figsize=(6, 4))
axs1.stackplot(x, y, y*2, y*3, labels=["solar", "wind", "nuclear power"])
axs2.scatter(x, y, alpha=0.5, c=y, s=40)
axs3.fill_between(x, y-20, y+20, color="blue", alpha=0.2, label="uncertainty band")
axs4.plot(x, y, c='blue')
plt.show()


plt.rcParams['font.size'] = 10
# Explicit approach using subplot_mosaic
fig, axs = plt.subplot_mosaic([['axs1', 'axs1'],
                               ['axs2', 'axs3']],
                              figsize=(6, 4))
axs['axs1'].stackplot(x, y, y*2, y*3, labels=["solar", "wind", "nuclear power"])
axs['axs2'].scatter(x, y, alpha=0.5, c=y, s=40)
axs['axs3'].fill_between(x, y-20, y+20, color="blue", alpha=0.2, label="uncertainty band")
#plt.savefig("C:/examples/myplot.png", dpi=600)
plt.show()


# More examples with code: https://matplotlib.org/stable/gallery/index.html 
# Save figure https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html
