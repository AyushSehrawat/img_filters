# Img-Filters

A module to help you with image manipulation.

## Installation
```bash
pip install img-filters==0.0.2
```

## Usage

Every class takes 1 arguement which is the path to image , it can be either relative or absolute

```bash
from img_filters.color import Color
from img_filters.color import Filter
from img_filters.tools import Tools
```


Color - Class
```bash
from img_filters.color import Color
color = Color('image_name.jpg') # Any image format & Any type of path
color.gray() # Example to convert image to gray
color.hsv() # Example to convert image to hsv
color.rgba() # Example to convert image to rgba
```

Filter-Calss
```bash
from img_filters.color import Filter
filter = Filter('image_name.jpg') # Any image format & Any type of path
filter.blur(val1,val2) # It takes 2 arguements , it is pixel by pixel
filter.edge() # Shows the edges of the image
filter.contrast(val) # Increase or decrease the contrast depending upon val given
filter.imgcolor(val) # Increase or decrease image color depending upon val given
filter.bright(val) # Increase or decrease image brighness depending upon val given
```

Tools - Class
```bash
from img_filters.tools import Tools
tools = Tools('image_name.jpg')  # Any image format & Any type of path
tools.rotate(angle) # Rotate the image by given angle
tools.flip() # Flips the image
```