
from MultiPage import MultiPage
from pages import data_upload, new_dataset_uploaded_pipeline, new_analysis_method_committed_pipeline

#create an instance of the multipage class
app = MultiPage()

#add pages to the app using the add_page method from the Multipage class
app.add_page("Upload file", data_upload.app)
app.add_page("New dataset uploaded pipeline", new_dataset_uploaded_pipeline.app)
app.add_page("New analysis method committed pipeline", new_analysis_method_committed_pipeline.app)

#start the application by calling the run method from the MultiPage class
app.run()
