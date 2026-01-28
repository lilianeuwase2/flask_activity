from flask import Flask, request, jsonify
import base64

from factorial import (
    bubble_sort,
    linear_search,
    binary_search,
    nested_loops,
    time_complexity_visualizer
)

app = Flask(__name__)


@app.route("/analyze")
def analyze():
    algo = request.args.get("algo")
    n = int(request.args.get("n", 1000))
    steps = int(request.args.get("steps", 100))

    algorithms = {
        "bubble": (bubble_sort, "O(n^2)"),
        "linear": (linear_search, "O(n)"),
        "binary": (binary_search, "O(log n)"),
        "nested": (nested_loops, "O(n^2)")
    }

    if algo not in algorithms:
        return jsonify({"error": "Invalid algorithm"}), 400

    algorithm_func, complexity = algorithms[algo]

    input_sizes, times = time_complexity_visualizer(
        algorithm_func,
        n_min=steps,
        n_max=n,
        n_step=steps
    )

    with open("graph.png", "rb") as img:
        graph_base64 = base64.b64encode(img.read()).decode("utf-8")

    return jsonify({
        "algorithm": algo,
        "time_complexity": complexity,
        "input_sizes": input_sizes,
        "execution_times": times,
        "graph_base64": graph_base64
    })


if __name__ == "__main__":
    app.run(port=3000, debug=True)
