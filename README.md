# Gaussian Process Regression to estimate human movement
This exercise implements <i>Gaussian Process</i> to estimate movement of human subjects using markers placed on human body.
A motion capture suit allows the recording of human movement position data.
<br/>
<p style="text-align:center" align="center">
<img src="https://raw.githubusercontent.com/anuparna/Gaussian_Process/master/doc/images/motionCapture.png" width="250" height="300px" align="center">
</p>
<br/>
When humans contract muscles to move, they can control the stiffness of the movement by co-contracting opposing muscles. 
It could be very informative if this stiffness could be measured.<br/>

One hypothesis is that if a joint controller is stiff, it will produce reliable repeated movements, 
whereas if it is very loose, there will be more variation in repeated movements.

## Datasets
The dataset is composed of CSV files available in the folder: <a href="https://github.com/anuparna/Gaussian_Process/tree/master/data">data</a>.<br/>
The data files have five repeated movements of a subject tracing a square target.<br/>
As the subject does this, the posture changes reflect the fact that different muscles are being used for different tracing segments.
The dataset has 60 separate movement CSV files, for 12 different subjects across 5 traces with each subject.

Each CSV file has a marker position along 3 different dimensions - X, Y and Z. The position of the marker is captured for against time.
The scale is in video frames at 1/60 second per frame.

## Documentation
The code execution begins from main.py.
The extraction of the sample points for marker 1 on X-axis is done in extractData.py.
The experiment was done on these points.

The below plot shows samples from marker 1 on X-axis across all 5 traces of all 12 subjects.
The black dotted line predicts the average predict across all predictions of Gaussian Process.
<br/>
<p style="text-align:center" align="center">
<img src="https://raw.githubusercontent.com/anuparna/Gaussian_Process/master/doc/images/allPoints.png" width="550" height="350px" align="center">
</p>
<br/>


Further documentation of this process could be found 
<a href="https://raw.githubusercontent.com/anuparna/Gaussian_Process/master/doc/Gaussian%20Processes.pdf">here</a>.
