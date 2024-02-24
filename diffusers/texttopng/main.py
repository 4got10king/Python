import torch
from diffusers import StableDiffusionPipeline  
model_id = "dreamlike-art/dreamlike-diffusion-1.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id)

pipe = pipe.to("cpu")

images = pipe(
    prompt="пиксельный вид мягкой игрушки, зеленого динозавра рекса в белой футболке, 8 на 8 пикселей",
    height=240,
    width=240,
    num_inference_steps=100,
    guidance_scale=0.5,
    num_images_per_prompt=1).images


images[0].save("dinosaur.png") 
