# Stable Diffusion : Gaussian Noise - Color Distribution

Stable Diffusion is an artificial intelligence model that can generate images from
descriptive text inputs.

## The Diffusion Process 
To generate a unique desired image, the model starts with a random Gaussian Noise 
image information, and from here undergoes multiple steps to reach our desired image.
Each step the model changes the information in a way that more resembles the input
text but also in a way that resembles the visual information the model picked up from all
images it has been trained on.

### Training Diffusion Models
Noise Predictor: 
We get an image, generate some random gaussian noise, and then let the model predict
this noise. After that the model compares its prediction to the actual noise (calculate
loss), then updates itself to be better next time.

Reverse Diffusion (Denoising)
The trained noise predictor takes a noisy image, the amount of noise, and is able to
predict some of the noise by each step. The noise is predicted so that if we subtract it
from the noisy image we get an image close to the images the model has been trained
on, not the exact images but fits the distribution of those images. Though until now we
have no control over the generated images, here is where we incorporate the text input
and generate what we want.

## Generating an image that fits the data it trained on 
This data has certain distributions for everything : colors, objects, mood, style, details,
and much more. So what the model does is generate an image that belongs to these
distributions in the way needed.
We will now consider images of Van Gogh as our data, we will study their color
distributions namely Histograms. By doing that we will know how this artist uses color
and what are the most likely colors used. A model like Stable Diffusion uses that
information to generate new images that look like it's drawn by this artist.

# What is this project
 It is focused from a probability aspect on two parts, Gaussian Noise and color distribuion.
 
 ### Gaussian Noise
 Adding random Gaussian noise to an image. How does variance and mean affect the noise.
 > GaussianNoise.py : Takes an image,also mean and variance of the gaussian noise. Outputs noisy image and representing the gaussian distribution with its PMF and CDF.

### Color Distribution
Generating color histogram for red, green, blue in pixels we get their frequencies or count. Normalizing this histogram we obtain the probabilty for each color intensity or PMF.
> colorDistribution.py : Takes an image, outputs PMF and CDF of the each color channel.

> conditionalProbability.py : Generates a joint histogram between two color channels to see dependant probabilities of a color given that the other color has acertain intensity.

## Documentation
For more details and results please visit the [documentation](https://github.com/shahdelrefai/stable_diffusion/blob/main/Stable%20Diffusion.pdf).
