
df = pd.DataFrame(data=np.random.randn(200, 2),
                  columns=['A', 'B'])
df['data_size'] = np.random.randint(1, 100, 200)
fig = plt.figure()
ax = fig.add_subplot(111)
ax_cmap = ax.scatter(df['A'], df['B'], s=df['data_size']*10, c=df['data_size'], cmap='viridis', alpha=0.5)
fig.colorbar(ax_cmap)
ax.set_xlabel('$x_0$', fontsize=10)
ax.set_ylabel('$x_1$', fontsize=10)
ax.set_title('title')
plt.show()
