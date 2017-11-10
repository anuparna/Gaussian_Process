# Gaussian Process Regression to estimate human movement
This exercise implements <i>Gaussian Process</i> to estimate movement of human subjects using markers placed on human body.
A motion capture suit allows the recording of human movement position data.
<br/>
<p style="text-align:center" align="center">
<img src="https://github.com/anuparna/Gaussian_Process/blob/master/doc/images/motion_capture.PNG" width="250" height="300px" align="center">
</p>
<br/>
When humans contract muscles to move, they can control the stiffness of the movement by co-contracting opposing muscles. 
It could be very informative if this stiffness could be measured.<br/>

One hypothesis is that if a joint controller is stiff, it will produce reliable repeated movements, 
whereas if it is very loose, there will be more variation in repeated movements.

## Datasets
The dataset is composed of CSV files available in the folder: <a href="https://github.com/anuparna/Gaussian_Process/tree/master/data">data</a>.
The data files have five repeated movements of a subject tracing a square target.<br/>
As the subject does this, the posture changes reflect the fact that different muscles are being used for different tracing segments.
The dataset has 60 separate movement files, for 12 different subjects across 5 traces with each subject.

## Documentation
Further documentation of this process could be found <a href="https://github.com/anuparna/Gaussian_Process/blob/master/doc/Gaussian%20Processes.pdf">here</a>.
