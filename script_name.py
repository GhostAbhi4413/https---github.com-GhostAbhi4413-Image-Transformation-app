import cv2
import numpy as np
import streamlit as st

def apply_affine_transformation(image, transformation_type, **kwargs):
    rows, cols = image.shape[:2]

    if transformation_type == 'Translation':
        tx, ty = kwargs['tx'], kwargs['ty']
        matrix = np.float32([[1, 0, tx], [0, 1, ty]])

    elif transformation_type == 'Rotation':
        angle = kwargs['angle']
        matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

    elif transformation_type == 'Scaling':
        scale_x, scale_y = kwargs['scale_x'], kwargs['scale_y']
        matrix = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])

    elif transformation_type == 'Shearing':
        shear_x, shear_y = kwargs['shear_x'], kwargs['shear_y']
        matrix = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])

    transformed_image = cv2.warpAffine(image, matrix, (cols, rows))
    return transformed_image

def main():
    st.title('Image Transformations with OpenCV and Streamlit')

    uploaded_file = st.file_uploader("Choose an image...", type=[ "png"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        transformation_type = st.selectbox("Select Transformation", ['Translation', 'Rotation', 'Scaling', 'Shearing'])

        if transformation_type == 'Translation':
            tx = st.slider("Horizontal Shift (pixels)", -100, 100, 0)
            ty = st.slider("Vertical Shift (pixels)", -100, 100, 0)
            transformed_image = apply_affine_transformation(image, transformation_type, tx=tx, ty=ty)

        elif transformation_type == 'Rotation':
            angle = st.slider("Rotation Angle (degrees)", -180, 180, 0)
            transformed_image = apply_affine_transformation(image, transformation_type, angle=angle)

        elif transformation_type == 'Scaling':
            scale_x = st.slider("Horizontal Scaling Factor", 0.1, 2.0, 1.0, step=0.1)
            scale_y = st.slider("Vertical Scaling Factor", 0.1, 2.0, 1.0, step=0.1)
            transformed_image = apply_affine_transformation(image, transformation_type, scale_x=scale_x, scale_y=scale_y)

        elif transformation_type == 'Shearing':
            shear_x = st.slider("Horizontal Shear Factor", -1.0, 1.0, 0.0, step=0.1)
            shear_y = st.slider("Vertical Shear Factor", -1.0, 1.0, 0.0, step=0.1)
            transformed_image = apply_affine_transformation(image, transformation_type, shear_x=shear_x, shear_y=shear_y)

        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

if __name__ == '__main__':
    main()
