from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

                # <horizontal_fov>0.2</horizontal_fov>
                # <image>
                #     <width>640</width>
                #     <height>480</height>

w = 640
h = 480

# x = np.linspace(-w/2,w/2,w)
# zx = x**2*0.01

y = np.linspace(-h/2, h/2,h)
zy = (y**2)*(1/((h/2)*(h/2)))

# plt.plot(x,zx)
plt.plot(y,zy)
plt.show()

# ax = plt.figure().add_subplot(projection='3d')
# # X, Y, Z = axes3d

# # Plot the 3D surface
# ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8,
#                 alpha=0.3)

# # Plot projections of the contours for each dimension.  By choosing offsets
# # that match the appropriate axes limits, the projected contours will sit on
# # the 'walls' of the graph
# ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
# ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
# ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')

# ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100),
#        xlabel='X', ylabel='Y', zlabel='Z')

# plt.show()