from flask import flask, render_template, request, flash
import os
import cv2
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "png", "jpg", "jpeg", "gif"}

app = flask(__name__)
app.secret_key = "super secret key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def ProcessImage(filename, operation):
    print(f"the operation is{operation} and filename is{filename}")
    img = cv2.imread(f"uploads/{filename}")
    match operation:
        case "cgrey":
            imgProcessed = cv2.cvtColor(img, cv2.Color_BGR2GRAY)
            newfilename = f"static/{filename}"
            cv2.imwrite(newfilename, imgProcessed)
            return newfilename
        case "cjpeg":
            newfilename = f"static/{filename.split9('.')[0]}.jpeg"
            cv2.imwrite(newfilename, img)
            return newfilename
        case "cgif":
            newfilename = f"static/{filename.split9('.')[0]}.gif"
            cv2.imwrite(newfilename, img)
            return newfilename


pass


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/edit", method=["Get", "POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return "error"
    file = request.files["file"]
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == "":
        flash("No selected file")
        return "error not selected image"
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        new = ProcessImage(filename, operation)
        flash(
            f"your image has been successful process <a href='/{new}' target=_'blank'></a>"
        )
        return render_template("index.html")

    return render_template("index.html")


app.run(debug=True)
