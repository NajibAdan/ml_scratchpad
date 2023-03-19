def plot_vectors(vectors, colors):
    plt.figure()
    plt.axvline(x=0,color='lightgray')
    plt.axhline(y=0, color='lightgray')

    for i in range(len(vectors)):
        x = np.concatenate([[0,0],vectors[i]])
        plt.quiver([x[0]],[x[1]],[x[2]], [x[3]], angles='xy',
                   scale_units='xy', scale=1, color= colors[i],)