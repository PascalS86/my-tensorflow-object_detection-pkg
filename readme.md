# TF.OBJD

This is my break down to the tensorflow object_detection sample (look at 
https://github.com/tensorflow/models/tree/master/research/object_detection)

It contains all code for building you own object_detection with tensorflow.
It is tested with windows 10, so maybe you need some special handling for unix or other.

You're able to use the mapping, visualization etc. you know from the tensorflow sample, just with the namespace 

```python
import tf.objd.utils as utils
```