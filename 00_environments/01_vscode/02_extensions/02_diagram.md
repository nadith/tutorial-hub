# 0 Diagramming tools (comparison)
https://youtu.be/tPh9_Cx4yZY


# 1. PlantUML Extension

## PlantUML PicoWeb Server

Many plugins take advantage of the online web server to generate images.
For some reasons (security, performance...) you may need to use your own local server instead. This is possible thanks to the PlantUML Server which is available here.
However, installing and configuring a full webserver may be too complex for some users so we have decided to integrate a tiny webserver inside plantuml.jar.
This means that you only need a Java Runtime Environment and plantuml.jar to run this very simple web server.
Back to topRunning the server
Running the server is pretty simple. You just have to launch:

java -jar plantuml.jar -picoweb
Attention: By default, the server listens on all interfaces on port 8080. To change the default behavior, you can specify a colon separated port (still listening on all interfaces) or, both, a port and a bind address:

https://plantuml.com/picoweb


## Installation under Windows
Starting from 1.2020.21
If you use a recent version (that is at least version 1.2020.21), you don't need to manually install GraphViz anymore !
A minimalistic graphviz dot.exe is packed into PlantUML and will be automagically unzipped in some temporary folder if needed (that is, if no installed GraphViz is available).
This is really the prefered option under Windows.
Caveat: Before 1.2020.25, there was an error message during graph generation, so please use 1.2020.25 or more recent.
Older PlantUML versions
For older version, you have to install GraphViz by yourself. You can either:
Install Win32 version of GraphViz 2.44 (easiest)
Use the minimalistic graphviz dot.exe and unpack it on your c:\ drive (see below)
Install x64 version of GraphViz 2.44 (more complex)
With x64 version, you may have to run dot -c (with with Administrator Right) in a command line to finalize the installation, like in the following example:

https://plantuml.com/graphviz-dot


> GitHub does not support it natively.

> Install Chrome Browser Extension to view PlantUML
Refer to this [link](../../04_git/04_github.md)


## IPython PlantUML
pip install iplantuml

https://pypi.org/project/IPlantUML/
https://stackoverflow.com/questions/20303335/ipython-notebook-plantuml-extension




# 2. Mermaid Diagrams

> GitHub supports it.











