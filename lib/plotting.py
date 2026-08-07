import os
import warnings

import matplotlib.pyplot as plt


def apply_thesis_style():
    """Times New Roman look via LaTeX (mathptmx) for all figure text."""
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Times New Roman"],
        "text.latex.preamble": r"\usepackage{mathptmx}",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "legend.fontsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
    })


def save_bundle(fig, output_dir, name, title, assumptions, notes=None):
    """Save fig as a 3-file bundle under output_dir/name/: plot.png, plot.tex, assumptions.md.

    assumptions: dict of {label: value} fixed sweep parameters for this plot.
    notes: optional list of extra assumption strings (not key/value).
    """
    bundle_dir = os.path.join(output_dir, name)
    os.makedirs(bundle_dir, exist_ok=True)

    png_path = os.path.join(bundle_dir, "plot.png")
    fig.savefig(png_path, dpi=150, bbox_inches="tight")

    tex_path = os.path.join(bundle_dir, "plot.tex")
    try:
        import tikzplotlib
        tikzplotlib.save(tex_path, figure=fig)
    except Exception as e:
        warnings.warn(f"tikzplotlib export failed for {name}: {e}")
        with open(tex_path, "w") as f:
            f.write(f"% tikzplotlib export failed: {e}\n% see plot.png for the figure\n")

    md_path = os.path.join(bundle_dir, "assumptions.md")
    with open(md_path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write("Fixed parameters for this plot:\n\n")
        for label, value in assumptions.items():
            f.write(f"- **{label}**: {value}\n")
        if notes:
            f.write("\nOther assumptions:\n\n")
            for note in notes:
                f.write(f"- {note}\n")

    return bundle_dir
