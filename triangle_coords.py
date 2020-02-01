
import numpy as np
import matplotlib.pyplot as plt
import math


def draw_triangles(ax,n,w):
     if n > 0:
      ax.plot(p[:,0],p[:,1],linewidth = 0.5, color = 'k')
      p1 = [[(p[0,0] + p[1,0])/2],[(p[0,1] + p[1,1])/2]]
      p2 = [[(p[1,0] + p[2,0])/2],[(p[1,1] + p[2,1])/2]]
      p3 =[[(p[2,0] + p[3,0])/2,[(p[2,1] + p[3,1])/2]]]
      p4 = [[(p[3,0] + p[0,0])/2,[(p[3,1] + p[0,1])/2]]]
      # q = p.copy() *p1*p2*p3
      # triangle(ax,n-1,q,w)

# def draw_triangles(ax,n,q,w):
#      if n > 0:
#       ax.plot(p[:,0],p[:,1],linewidth = 0.5, color = 'k')
#       p1 = [[(p[0,0] + p[1,0])/2],[(p[0,1] + p[1,1])/2]]
#       p2 = [[(p[1,0] + p[2,0])/2],[(p[1,1] + p[2,1])/2]]
#       p3 =[[(p[2,0] + p[3,0])/2,[(p[2,1] + p[3,1])/2]]]
#       p4 = [[(p[3,0] + p[0,0])/2,[(p[3,1] + p[0,1])/2]]]
#       # q = p.copy() *p1*p2*p3
#       triangle(ax,n-1,q,w)



if __name__ == "__main__":

    plt.close("all") # Close all figures

    w=1
    fig, ax = plt.subplots()
    draw_triangles(ax,2,w)
    ax.set_aspect(1.0)
    plt.show()
    fig.savefig('triangel.png')
