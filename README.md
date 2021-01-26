# spatial_csv_formats Package

This package holds header and format definitions for [CSV-files](https://en.wikipedia.org/wiki/Comma-separated_values) that hold timestamped 3D **spatial** information. 
By **spatial** 
- 3-DoF relative position (), 
- 3-DoF attitude (orientation represented by quaternions), 
- 6-DoF pose (position + attitude)
- 6-DoF pose with uncertainty.

File headers are in the first line of a CSV file starting with a `#`, followed by a sequence of unique comma separated strings/chars. 

It is highly recommended to load the CSV files into a [pandas.DataFrame](). For convenience, there is a package called [csv2dataframe]() that does the conversion using the [CSVFormat](CSVFormat.py) definitions.



## Note
The [CSVFormat.TUM](CSVFormat.py) format, got it's name for file format used in the [TUM RGB-D benchmark tool](ttps://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation). Noticeable, is that the order of quaternion is non-alphabetically (`[q_x,q_y,q_z, q_w]` instead of `[q_w, q_x, q_y, q_z]`), meaning that first comes the imaginary part, then the real part, but this is just a matter of taste and definition! To be backward compatible with older/other tools ([TUM RGB-D benchmark tool](ttps://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation), [rpg_trajectory_evaluation](https://github.com/uzh-rpg/rpg_trajectory_evaluation), etc.), we follow this non-alphabetically order!  


## TODO:

* rename `sTUM_short` to `sPosition`
* rename `sPoseWithCov` to `sTUMWithCov`
* create a `sPose` with quaternions in alphabetic order!
* create a `sPoseWithCov` with quaternions in alphabetic order!
* rename `CSVFormat` to `CSVFormatPose`

## Dependencies

* [enum]()




## License


Software License Agreement (GNU GPLv3  License), refer to the LICENSE file.

*Sharing is caring!* - [Roland Jung](https://github.com/jungr-ait)  
