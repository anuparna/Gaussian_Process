from extractData import *
from plot_data import *
import Kernel
import train

if __name__ == '__main__':
    # Work on multiple traces of the same subject
    extract_data_files(1)  # 1 - indicates that consider only the first subject
    #print(train_file_names)
    for file in train_file_names:
        frames_list, x_coordinates_list = file_wise_extract_data(file, 1, is_training=True)
        test_frames_list, test_x_coordinates_list = file_wise_extract_data(file, 1, is_training=False)

        gp = None
        kernel = Kernel.Kernel(1.0, 1.0)
        for frames, coordinates in zip(frames_list, x_coordinates_list):
            #plot_marker('1', np.reshape(frames, (-1, 1)), coordinates)
            #plot_show()
            if gp:
                gp = train.train(gp, kernel, frames, coordinates, sigma2=1.0)
            else:
                gp = train.train(None, kernel, frames, coordinates, sigma2=1.0)

            define_labels(file, '1')
            plot_marker_test(np.reshape(test_frames_list, (-1, 1)), np.reshape(test_x_coordinates_list, (-1, 1)),
                         None, 'bo', labels='Observations')
            for test_frames, test_coordinates in zip(test_frames_list, test_x_coordinates_list):
                y_pred, mse = train.test(gp, test_frames)
                plot_marker_test(np.reshape(test_frames, (-1, 1)), y_pred, mse, 'k-', labels='Prediction')
                plot_show()


    # Test for all subjects
    extract_data_files(12)
    frames_list, x_coordinates_list = all_subjects_all_extract_data(1, is_training=True)
    test_frames_list, test_x_coordinates_list = all_subjects_all_extract_data(1, is_training=False)

    gp = None
    kernel = Kernel.Kernel(1.0, 1.0)
    all_predictions = []
    for frames, coordinates in zip(frames_list, x_coordinates_list):
        plot_marker('1', np.reshape(frames, (-1, 1)), coordinates)
        #plot_show()
        if gp:
            gp = train.train(gp, kernel, frames, coordinates, sigma2=1.0)
        else:
            gp = train.train(None, kernel, frames, coordinates, sigma2=1.0)

        define_labels(file, '1')
        #plot_marker_test(np.reshape(test_frames_list, (-1, 1)), np.reshape(test_x_coordinates_list, (-1, 1)),
        #                 None, 'bo', labels='Observations')

        for test_frames, test_coordinates in zip(test_frames_list, test_x_coordinates_list):
            y_pred, mse = train.test(gp, test_frames)
            all_predictions.append(y_pred)
            #print(y_pred.shape)
    all_predictions = np.array(all_predictions)
    #print("check",all_predictions.shape)

    plot_marker_test(np.reshape(test_frames, (-1, 1)), np.mean(all_predictions, axis=0),
                     None, 'ko', labels='Prediction', markersize=5)
    plot_show()
