from flask import Flask, request, jsonify, render_template
from database import init_db, db_session
from models import Image
from s3_utils import upload_to_s3
import os
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    images = db_session.query(Image).order_by(Image.upload_time.desc()).all()
    return render_template('index.html', images=images)


@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image uploaded'}), 400

    filename = file.filename

    # Read the content once
    file_bytes = file.read()
    size = len(file_bytes)

    # Upload to S3 (pass BytesIO object)
    from io import BytesIO
    s3_url = upload_to_s3(BytesIO(file_bytes), filename)

    image = Image(
        filename=filename,
        size=size,
        s3_url=s3_url,
        upload_time=datetime.now()
    )
    db_session.add(image)
    db_session.commit()

    return jsonify({'message': 'Image uploaded', 'url': s3_url})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
