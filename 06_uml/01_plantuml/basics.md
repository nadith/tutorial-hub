# Generate huge diagrams!
https://plantuml.com/faq

PlantUML limits image width and height to 4096. There is an environment variable that you can set to override this limit: PLANTUML_LIMIT_SIZE. You have to define this variable before launching PlantUML, something like:

set PLANTUML_LIMIT_SIZE=8192
or

setenv PLANTUML_LIMIT_SIZE 8192
Another way is an option in the command line:

java -DPLANTUML_LIMIT_SIZE=8192 -jar /path/to/plantuml.jar ...
Note that if you generate very big diagrams, (for example, something like 20 000 x 10 000 pixels), you can have some memory issues. The solution is to add this parameter to the java vm : -Xmx1024m.