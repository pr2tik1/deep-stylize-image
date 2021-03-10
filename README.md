# Deep Stylize Image

![](https://github.com/pr2tik1/deep-style-images/blob/main/banner.jpg)

Stylize your image using a web app. The app is built using streamlit and the model is developed using PyTorch. This app uses Style Transfer technique and particualary the "Fast Neural Style". The model and training part is referred from the pytorch examples: https://github.com/pytorch/examples/tree/master/fast_neural_style. 

## Dependencies
```
streamlit==0.78.0
torch==1.7.1
```

## Run

1. Local Hosting

Run following python script in terminal,

```python
streamlit run app.py
```
If the app does not pop up to your default browser, then to view the app follow the localhost link shown in terminal. The link is displayed until you stop by pressing: Ctrl+Z or kill the terminal.


2. Heroku
#TODO

## Usage
Select styles and default images from the sidebar. Then if the user wants to upload his/her own image, select he upload option. Next click on stylize and the output image is shown. To save the image, simply right click -> 'Save Image as'.

## Glimpse of app

![](https://github.com/pr2tik1/deep-stylize-image/blob/main/glimpse.gif)

## Author
[Pratik Kumar](https://pr2tik1.github.io)

## Credits
- PyTorch community
- Streamlit community
