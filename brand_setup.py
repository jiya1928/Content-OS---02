from PIL import Image
import base64, io, os

def to_b64(pil_img):
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

def load_default_photo():
    paths = ["wa_image_2143544513346209280", "./wa_image_2143544513346209280.jpg", "/mnt/data/wa_image_2143544513346209280"]
    for p in paths:
        if os.path.exists(p):
            try:
                return to_b64(Image.open(p))
            except:
                pass
    return None