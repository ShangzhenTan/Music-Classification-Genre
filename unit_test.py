import numpy as np
import unittest

from audio_preprocessor import audio_preprocessor
from feature_extractor import feature_extractor
from feature_extractor import feature_type
from feature_extractor import echonest_feature_type
from feature_extractor import statistic_type

USE_ECHONEST_DATASET = False
extractor = feature_extractor(USE_ECHONEST_DATASET)
processor = audio_preprocessor()

class TestExtractor(unittest.TestCase):
    ''' Test feature extractor class '''
    ''' Make sure to download the metadata folder '''
    ''' using setup_env.sh before running unit tests '''

    def test_get_training_dataset_info(self):
        ''' Get training dataset '''
        training_set_song_ids = extractor.get_training_dataset_song_ids()
        print('---------------------------------------------------------')
        print('Training dataset (total size: ' + str(len(training_set_song_ids)) + ')')
        print('---------------------------------------------------------\n')
        TestExtractor.print_dataset_info(training_set_song_ids, True)

    def test_get_validation_dataset_info(self):
        ''' Get validation dataset '''
        validation_set_song_ids = extractor.get_validation_dataset_song_ids()
        print('---------------------------------------------------------')
        print('Validation dataset (total size: ' + str(len(validation_set_song_ids)) + ')')
        print('---------------------------------------------------------\n')
        TestExtractor.print_dataset_info(validation_set_song_ids)

    def test_get_test_dataset_info(self):
        ''' Get test dataset '''
        test_set_song_ids = extractor.get_test_dataset_song_ids()
        print('---------------------------------------------------------')
        print('Test dataset (totalsize: ' + str(len(test_set_song_ids)) + ')')
        print('---------------------------------------------------------\n')
        TestExtractor.print_dataset_info(test_set_song_ids)

    def test_get_all_genres(self):
        ''' Get all genres '''
        genre_list = extractor.get_all_genres()
        print('---------------------------------------------------------')
        print('Genre List (totalsize: ' + str(len(genre_list)) + ')')
        print('---------------------------------------------------------\n')
        print(genre_list)
        print('\n')

    def print_dataset_info(dataset, training_data=False):
        ''' Print dataset info'''
        SAMPLE_SIZE = 1

        print('Printing sample data...\n')

        # Get features
        for i in dataset[:SAMPLE_SIZE]:
            print('Song: #' + str(i))
            print('Title: ' + str(extractor.get_title(i)))
            print('Artist: ' + str(extractor.get_artist(i)))
            print('Genre: ' + str(extractor.get_genre(i)))
            print('Median MFCC:\n' + str(extractor.get_feature(i, feature_type.MFCC, statistic_type.MEDIAN)) + '\n')
            print('Median Chroma STFT:\n' + str(extractor.get_feature(i, feature_type.CHROMA_STFT, statistic_type.MEDIAN)) + '\n')
            print('Median Spectral Contrast:\n' + str(extractor.get_feature(i, feature_type.SPEC_CONTRAST, statistic_type.MEDIAN)) + '\n')

            # Get echonest features
            if USE_ECHONEST_DATASET == True:
                for ef in echonest_feature_type:
                    print(extractor.echonest_feature_types_str[ef].title() + ':\n' + str(extractor.get_echonest_feature(i, ef)) + '\n')

class TestProcessor(unittest.TestCase):
    ''' Test audio preprocessor class '''
    ''' Make sure to download the audio folder '''
    ''' using setup_env.sh before running unit tests '''

    def test_display_spectrogram(self):
        ''' Get training dataset '''
        training_set_song_ids = extractor.get_training_dataset_song_ids()

        size = len(processor.list_of_all_audio_files)

        if size > 0:
            print('---------------------------------------------------------')
            print('Audio data files (total size: ' + str(len(processor.list_of_all_audio_files)) + ')')
            print('---------------------------------------------------------\n')

            file_path = processor.find_song_filepath(training_set_song_ids[0])
            print ('Song ID: ' + str(training_set_song_ids[0]))
            print ('Plotting spectrogram for song: ' + str(file_path))

            processor.plot_mel_spectrogram(file_path)


if __name__ == '__main__':
    unittest.main()






