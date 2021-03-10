# Deep Stylize Image

![](https://github.com/pr2tik1/deep-style-images/blob/main/banner.jpg)

Stylize your image using a web app. The app is built using streamlit and the model is developed using PyTorch. This app uses Style Transfer technique and particualary the "Fast Neural Style". The model and training part is referred from the pytorch examples: https://github.com/pytorch/examples/tree/master/fast_neural_style. 

## Dependencies
```
streamlit==0.78.0
pillow
https://download.pytorch.org/whl/cpu/torchvision-0.7.0%2Bcpu-cp36-cp36m-linux_x86_64.whl
https://download.pytorch.org/whl/cpu/torch-1.6.0%2Bcpu-cp36-cp36m-linux_x86_64.whl
```

## Run

1. Local Hosting

Run following python script in terminal,

```python
streamlit run app.py
```
If the app does not pop up to your default browser, then to view the app follow the localhost link shown in terminal. The link is displayed until you stop by pressing: Ctrl+Z or kill the terminal.


2. Heroku
The app is deployed(as of 11.03.2021) with Heroku, please follow the link :   https://deep-style-images.herokuapp.com 

## Usage
Select styles and default images from the sidebar. Then if the user wants to upload his/her own image, select he upload option. Next click on stylize and the output image is shown. To save the image, simply right click -> 'Save Image as'.


## Author
[Pratik Kumar](https://pr2tik1.github.io)

## Credits
- PyTorch community
- Streamlit community
