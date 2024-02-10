# The Jarvis project
The goal of this project is to create a machine learning model which will be able to read the hand location and gesture from camera feed in real-time. The model will then be paired with a program, which will use the data to control the PC, as if the hand was a mouse.

**In case it's hard for you to imagine, this is what I aim for:**

![](https://media.giphy.com/media/g4sCZhKykg1z2/giphy.gif)

This is also the first step towards developing AR software which is going to imitate Apple Vision Pro, which I was heavily inspired by. Not to mention the titular Jarvis and how Tony Stark interacts with him.

## Todo
- [x] find a way to extract frames from videos
- [x] create a script to help with frame labelling process
- [ ] create the varied dataset
- [ ] develop the machine learning model
- [ ] develop software to translate the data from the model into mouse cursor movements
- [ ] implement clicking
- [ ] implement grabbing/dragging and dropping
- [ ] implement changing the virtual screen through waving
- [ ] support for extracting frames from other video formats, like .mp4

## References
- [Image classifier and processing tutorial](https://medium.com/analytics-vidhya/image-processing-with-python-applications-in-machine-learning-17d7aac6bc97)
- [Transform4Europe ML course by d-tomas from University of Alicante](https://github.com/d-tomas/transform4europe)