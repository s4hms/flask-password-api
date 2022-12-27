from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/")
def documentation():
    return render_template("index.html")


@app.route("/generate")
def generate():
    uc = request.args.get("uc", default=0, type=int)
    lc = request.args.get("lc", default=0, type=int)
    nc = request.args.get("nc", default=0, type=int)
    sc = request.args.get("sc", default="", type=str)

    combine_op = combine(uc, lc, nc, sc)

    diction = {
        "generate count": gen_count(),
        "password length": len(combine_op),
        "password": combine_op,
    }

    return jsonify(diction)


def upperchar(uc):
    uppercase_alphabets = list(string.ascii_uppercase)
    return random.choices(uppercase_alphabets, k=uc)


def lowerchar(lc):
    lowercase_alphabets = list(string.ascii_lowercase)
    return random.choices(lowercase_alphabets, k=lc)


def numericchar(nc):
    numeric_characters = list()
    for _ in range(nc):
        numeric_characters.append(str(random.randint(0, 9)))
    return numeric_characters


def combine(uc: int, lc: int, nc: int, sc: str):
    uppercase_alphabets_gen = upperchar(uc)
    lowercase_alphabets_gen = lowerchar(lc)
    numeric_characters_gen = numericchar(nc)

    combined_list = [
        *uppercase_alphabets_gen,
        *lowercase_alphabets_gen,
        *numeric_characters_gen,
        *[*sc],
    ]

    random.shuffle(combined_list)
    return "".join(combined_list)


def gen_count():
    with open("generate_count.txt", "r") as f:
        cont = f.read()

    with open("generate_count.txt", "w") as f:
        if len(cont) == 0:
            f.write("1")
            return 1
        else:
            f.write(f"{int(cont)+1}")
            return int(cont) + 1


if __name__ == "__main__":
    app.run(port=5000)
# when this line is present, run the script normally like python app.py
