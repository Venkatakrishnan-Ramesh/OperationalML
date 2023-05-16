import unittest
import streamlit as st
import os
import pandas as pd
from streamlit.testing import StreamlitTestClient

class TestApp(unittest.TestCase):
    def test_upload_functionality(self):
        # Simulate the Upload functionality by providing a sample file
        with open('test_dataset.csv', 'w') as f:
            f.write('col1,col2,col3\n')
            f.write('1,2,3\n')
        
        # Create a Streamlit test client
        client = self.get_test_client()
        
        # Simulate selecting the "Upload" option
        response = client.selectbox('Navigation', ['Upload', 'Profiling', 'Modelling', 'Download'], index=0)
        self.assertEqual(response, 'Upload')
        
        # Simulate uploading the sample file
        uploaded_file = client.file_uploader('Upload Your Dataset', type=['csv'])
        self.assertIsNotNone(uploaded_file)
        
        # Read the uploaded file and compare it with the expected data
        uploaded_df = pd.read_csv(uploaded_file)
        expected_df = pd.DataFrame({'col1': [1], 'col2': [2], 'col3': [3]})
        pd.testing.assert_frame_equal(uploaded_df, expected_df)
        
        # Clean up the test file
        os.remove('test_dataset.csv')
    
    def get_test_client(self):
        # Create a Streamlit test client
        client = StreamlitTestClient(st)
        client.set_option('browser.gatherUsageStats', False)
        return client

if __name__ == '__main__':
    unittest.main()
