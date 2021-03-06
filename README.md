# cnspy_spatial_csv_formats Package

This package holds header and format definitions for [CSV-files](https://en.wikipedia.org/wiki/Comma-separated_values) that hold timestamped 3D **spatial** information. 
By **spatial** 
- 3-DoF relative position (), 
- 3-DoF attitude (orientation represented by quaternions), 
- 6-DoF pose (position + attitude)
- 6-DoF pose with uncertainty.

File headers are in the first line of a CSV file starting with a `#`, followed by a sequence of unique comma separated strings/chars. 

It is highly recommended to load the CSV files into a [pandas.DataFrame](https://pypi.org/project/pandas/). For convenience, there is a package called [cnspy_csv2dataframe](https://github.com/aau-cns/cnspy_csv2dataframe) that does the conversion using the [CSVFormatPose](CSVFormatPose.py) definitions.


## Note

The [CSVFormatPose.TUM](./cnspy_spatial_csv_formats/CSVFormatPose.py) format, got it's name for file format used in the [TUM RGB-D benchmark tool](https://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation). Noticeable, is that the order of quaternion is non-alphabetically (`[q_x,q_y,q_z, q_w]` instead of `[q_w, q_x, q_y, q_z]`), meaning that first comes the imaginary part, then the real part, but this is just a matter of taste and definition! To be backward compatible with older/other tools ([TUM RGB-D benchmark tool](ttps://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation), [rpg_trajectory_evaluation](https://github.com/uzh-rpg/rpg_trajectory_evaluation), etc.), we follow this non-alphabetically order!


## Installation

Install the current code base from GitHub and pip install a link to that cloned copy
```
git clone https://github.com/aau-cns/spatial_csv_formats.git
cd spatial_csv_formats
pip install -e .
```
or the [official package](https://pypi.org/project/cnspy-spatial-csv-formats/) via
```commandline
pip install cnspy-spatial-csv-formats
```


## Dependencies

It is part of the [cnspy eco-system](hhttps://github.com/aau-cns/cnspy_eco_system_test) of the [cns-github](https://github.com/aau-cns) group.  

* [enum]()

## License


Software License Agreement (GNU GPLv3  License), refer to the LICENSE file.

*Sharing is caring!* - [Roland Jung](https://github.com/jungr-ait)
