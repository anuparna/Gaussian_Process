from pylab import *


def plot_marker(marker_id, frames, x_coordinates, coordinate='x'):
    plot(frames, x_coordinates)
    xlabel('Frames')
    ylabel(coordinate+'-coordinate of marker - '+marker_id)
    title(coordinate+' coordinate movement of marker - '+marker_id+' with time frames')
    grid(True)
    #show()


def define_labels(file, marker_id, coordinate='x'):
    xlabel('Frames')
    ylabel(coordinate + '-coordinate of marker - ' + marker_id)
    title('With filename '+file+' and '+coordinate + ' coordinate movement of marker - '
          + marker_id + ' with time frames')
    legend(loc='upper left')
    grid(True)


def plot_marker_test(frames, x_coordinates, mse, markers, labels, markersize=1):
    plot(frames, x_coordinates, markers,markersize=markersize, label=labels)
    if mse is not None:
        fill(np.concatenate([frames, frames[::-1]]),
             np.concatenate([x_coordinates - 1.9600 * mse,
                             (x_coordinates + 1.9600 * mse)[::-1]]),
             alpha=.5, fc='b', ec='None', label='95% confidence interval')


def plot_show():
    show()
