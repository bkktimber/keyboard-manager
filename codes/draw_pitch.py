def pitch_drawer():

    fig = plt.figure(figsize=(pitch_width / 10, pitch_height / 10))
    axes = fig.add_subplot(1, 1, 1, facecolor='#78AB46')

    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    plt.xlim([-5, pitch_width + 5])
    plt.ylim([-5, pitch_height + 5])

    box_width = (16.5 / pitch_width) / 1.15
    box_height = (2 * 16.5 * 7.32 / pitch_height) / 1.15

    pitch_line = plt.Rectangle(
        (0.04338, 0.0641), (0.95652 - 0.04338), (0.9359 - 0.0641),
        edgecolor='white',
        facecolor='none',
        alpha=1,
        transform=axes.transAxes)
    halfway_line = plt.Line2D(
        [0.5, 0.5], [0.9359, 0.0641], c='w', transform=axes.transAxes)
    penalty_area = plt.Rectangle(
        (0.04338, (1 - box_height) / 2),
        box_width,
        box_height,
        ec='w',
        fc='none',
        transform=axes.transAxes)
    six_yard_area = plt.Rectangle(
        (0.95652 - box_width, (1 - box_height) / 2),
        box_width,
        box_height,
        ec='w',
        fc='none',
        transform=axes.transAxes)
    middle_circle = Ellipse(
        (0.5, 0.5),
        9.15 * 2 / pitch_width,
        9.15 * 2 / pitch_height,
        ec='w',
        fc='none',
        transform=axes.transAxes)

    fig.lines.extend(
        [pitch_line, halfway_line, penalty_area, six_yard_area, middle_circle])

    return fig, axes