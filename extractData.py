import pandas as pd
import os


train_file_names = []
test_file_names = []


def all_subjects_all_extract_data(marker_id, is_training=True, coordinate='x', sample_points=40):
    frame_list = []
    coordinates_list = []
    if is_training:
        for file in train_file_names:
            df = pd.read_csv(file)
            df = df[['frame', str(marker_id - 1) + "_" + coordinate]][(df[str(marker_id - 1) + "_c"] >= 0)]
            frames, coordinates = extract_data_points(df, sample_points)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
    else:
        for file in train_file_names:
            df = pd.read_csv(file)
            df = df[['frame', str(marker_id - 1) + "_" + coordinate]][(df[str(marker_id - 1) + "_c"] >= 0)]
            frames, coordinates = extract_data_points(df, start_index=2, sample_points=50)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
            break
    return frame_list, coordinates_list


def file_wise_extract_data(file, marker_id, is_training=True, coordinate='x', sample_points=40):
    frame_list = []
    coordinates_list = []
    if is_training:
        df = pd.read_csv(file)
        df = df[['frame', str(marker_id - 1) + "_" + coordinate]][(df[str(marker_id - 1) + "_c"] >= 0)]
        frames, coordinates = extract_data_points(df, sample_points)
        frame_list.append(frames)
        coordinates_list.append(coordinates)
        frames, coordinates = extract_data_points(df, start_index=3, sample_points=30)
        frame_list.append(frames)
        coordinates_list.append(coordinates)
        frames, coordinates = extract_data_points(df, start_index=10, sample_points=40)
        frame_list.append(frames)
        coordinates_list.append(coordinates)
        frames, coordinates = extract_data_points(df, start_index=14, sample_points=10)
        frame_list.append(frames)
        coordinates_list.append(coordinates)
        # frames, coordinates = extract_data_points(df, start_index=20, sample_points=5)
        # frame_list.append(frames)
        # coordinates_list.append(coordinates)
    else:
        df = pd.read_csv(file)
        df = df[['frame', str(marker_id - 1) + "_" + coordinate]][(df[str(marker_id - 1) + "_c"] >= 0)]
        frames, coordinates = extract_data_points(df, start_index=1, sample_points=50)
        frame_list.append(frames)
        coordinates_list.append(coordinates)
    return frame_list, coordinates_list


def extract_data(marker_id, is_training=True, coordinate='x', sample_points=40):
    frame_list = []
    coordinates_list = []
    if is_training:
        for file in train_file_names:
            df = pd.read_csv(file)
            df = df[['frame', str(marker_id-1)+"_"+coordinate]][(df[str(marker_id-1)+"_c"] >= 0)]
            frames, coordinates = extract_data_points(df, sample_points)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
            frames, coordinates = extract_data_points(df, start_index=3, sample_points=30)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
            frames, coordinates = extract_data_points(df, start_index=10, sample_points=40)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
            frames, coordinates = extract_data_points(df, start_index=14, sample_points=10)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
            #frames, coordinates = extract_data_points(df, start_index=20, sample_points=5)
            #frame_list.append(frames)
            #coordinates_list.append(coordinates)
    else:
        for file in test_file_names:
            df = pd.read_csv(file)
            df = df[['frame', str(marker_id-1)+"_"+coordinate]][(df[str(marker_id-1)+"_c"] >= 0)]
            frames, coordinates = extract_data_points(df, start_index=1, sample_points=50)
            frame_list.append(frames)
            coordinates_list.append(coordinates)
    return frame_list, coordinates_list


def extract_data_points(df, start_index=0, sample_points=40):
    #print(len(df))
    avg = len(df)/sample_points
    #print(int(avg/2))
    #print(df.iloc[int(avg/2)]['0_x'])
    step_size = int(avg/2)
    # take the data-points and check what you can do
    count = start_index
    frames = []
    x_coordinates = []
    while (len(df) - count) >= step_size*2:
        #print(count)
        x_coordinates.append(df.iloc[count+step_size]['0_x'])
        frames.append(df.iloc[count+step_size]['frame'])
        count += step_size*2
    print((x_coordinates))
    print((frames))
    return frames, x_coordinates


def extract_data_files(no_subjects, is_training=True, start=0, root_dir='data'):
    subjects_dir = [os.listdir(root_dir)[i] for i in range(start, no_subjects)]

    for subject_dir in subjects_dir:
        for root, sub_dir, files in os.walk(root_dir+"/"+subject_dir):
            if 'block' in root:
                for file in files:
                    if '.csv' in file:
                        if is_training:
                            train_file_names.append(os.path.join(root, file))
                        else:
                            test_file_names.append(os.path.join(root, file))

                #break
