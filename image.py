{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'input_image.jpg'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32md:\\computerVision_assignments\\image.ipynb Cell 1\u001b[0m line \u001b[0;36m2\n\u001b[0;32m     <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=22'>23</a>\u001b[0m input_image_path \u001b[39m=\u001b[39m \u001b[39m\"\u001b[39m\u001b[39minput_image.jpg\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m     <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=24'>25</a>\u001b[0m \u001b[39m# Rotate image by 45 degrees\u001b[39;00m\n\u001b[1;32m---> <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=25'>26</a>\u001b[0m rotate_image(input_image_path, \u001b[39m\"\u001b[39;49m\u001b[39moutput_rotated.jpg\u001b[39;49m\u001b[39m\"\u001b[39;49m, \u001b[39m45\u001b[39;49m)\n\u001b[0;32m     <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=27'>28</a>\u001b[0m \u001b[39m# Flip image horizontally\u001b[39;00m\n\u001b[0;32m     <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=28'>29</a>\u001b[0m flip_image(input_image_path, \u001b[39m\"\u001b[39m\u001b[39moutput_flipped.jpg\u001b[39m\u001b[39m\"\u001b[39m)\n",
      "\u001b[1;32md:\\computerVision_assignments\\image.ipynb Cell 1\u001b[0m line \u001b[0;36m4\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mrotate_image\u001b[39m(input_path, output_path, angle):\n\u001b[1;32m----> <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m     image \u001b[39m=\u001b[39m Image\u001b[39m.\u001b[39;49mopen(input_path)\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m     rotated_image \u001b[39m=\u001b[39m image\u001b[39m.\u001b[39mrotate(angle)\n\u001b[0;32m      <a href='vscode-notebook-cell:/d%3A/computerVision_assignments/image.ipynb#W0sZmlsZQ%3D%3D?line=5'>6</a>\u001b[0m     rotated_image\u001b[39m.\u001b[39msave(output_path)\n",
      "File \u001b[1;32mc:\\Users\\Nightcoderz\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\PIL\\Image.py:3243\u001b[0m, in \u001b[0;36mopen\u001b[1;34m(fp, mode, formats)\u001b[0m\n\u001b[0;32m   3240\u001b[0m     filename \u001b[39m=\u001b[39m fp\n\u001b[0;32m   3242\u001b[0m \u001b[39mif\u001b[39;00m filename:\n\u001b[1;32m-> 3243\u001b[0m     fp \u001b[39m=\u001b[39m builtins\u001b[39m.\u001b[39;49mopen(filename, \u001b[39m\"\u001b[39;49m\u001b[39mrb\u001b[39;49m\u001b[39m\"\u001b[39;49m)\n\u001b[0;32m   3244\u001b[0m     exclusive_fp \u001b[39m=\u001b[39m \u001b[39mTrue\u001b[39;00m\n\u001b[0;32m   3246\u001b[0m \u001b[39mtry\u001b[39;00m:\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'input_image.jpg'"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "\n",
    "def rotate_image(input_path, output_path, angle):\n",
    "    image = Image.open(input_path)\n",
    "    rotated_image = image.rotate(angle)\n",
    "    rotated_image.save(output_path)\n",
    "\n",
    "def flip_image(input_path, output_path):\n",
    "    image = Image.open(input_path)\n",
    "    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)\n",
    "    flipped_image.save(output_path)\n",
    "\n",
    "def resize_image(input_path, output_path, size):\n",
    "    image = Image.open(input_path)\n",
    "    resized_image = image.resize(size)\n",
    "    resized_image.save(output_path)\n",
    "\n",
    "def grayscale_image(input_path, output_path):\n",
    "    image = Image.open(input_path).convert(\"L\")\n",
    "    image.save(output_path)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    input_image_path = \"input_image.jpg\"\n",
    "    \n",
    "    # Rotate image by 45 degrees\n",
    "    rotate_image(input_image_path, \"output_rotated.jpg\", 45)\n",
    "    \n",
    "    # Flip image horizontally\n",
    "    flip_image(input_image_path, \"output_flipped.jpg\")\n",
    "    \n",
    "    # Resize image to 200x200 pixels\n",
    "    resize_image(input_image_path, \"output_resized.jpg\", (200, 200))\n",
    "    \n",
    "    # Convert image to grayscale\n",
    "    grayscale_image(input_image_path, \"output_grayscale.jpg\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
