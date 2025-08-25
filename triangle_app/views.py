from django.shortcuts import render, redirect
from .forms import TriangleForm
import math
import json

def input_view(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            points = {
                "p1": (form.cleaned_data["x1"], form.cleaned_data["y1"]),
                "p2": (form.cleaned_data["x2"], form.cleaned_data["y2"]),
                "p3": (form.cleaned_data["x3"], form.cleaned_data["y3"]),
            }
            request.session["points"] = points
            return redirect("display")
    else:
        form = TriangleForm()
    return render(request, "triangle_app/input.html", {"form": form})

def angle(a, b, c):
    ab = math.dist(a, b)
    bc = math.dist(b, c)
    ca = math.dist(c, a)
    cos_angle = (ab**2 + bc**2 - ca**2) / (2 * ab * bc)
    return round(math.degrees(math.acos(cos_angle)), 2)

def display_view(request):
    points = request.session.get("points")
    if not points:
        return redirect("input")

    p1, p2, p3 = points["p1"], points["p2"], points["p3"]

    angleA = angle(p2, p1, p3)
    angleB = angle(p1, p2, p3)
    angleC = 180 - angleA - angleB  

    return render(request, "triangle_app/display.html", {
        "points_json": json.dumps(points),
        "angles_json": json.dumps({"A": angleA, "B": angleB, "C": round(angleC, 2)}),
        "angles": {"A": angleA, "B": angleB, "C": round(angleC, 2)}
    })
