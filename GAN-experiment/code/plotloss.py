import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

with open(filename,'r') as file:
	iters = []
	d_loss, g_loss = [], []
	for line in file:
		line = line.split(' ')
		if line[0] == 'Iter:':
			iters.append(int(line[1]))
		elif line[0] == 'D':
			d_loss.append(float(line[2]))
		elif line[0] == 'G_loss:':
			g_loss.append(float(line[1]))

plt.plot(iters, d_loss, label='D loss', linewidth=3)
plt.plot(iters, g_loss, label='G loss', linewidth=3)
plt.title('generator & discriminator loss')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()