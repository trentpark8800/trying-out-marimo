import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    x = 6
    return (x,)


@app.cell
def _(x):
    y = 10
    print(x+y)
    return


if __name__ == "__main__":
    app.run()
