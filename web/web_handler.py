from pathlib import Path

resource_path = Path(__file__).parent.joinpath('resources/')
page_html_name = 'index.html'


def generate_page(grid_size: int) -> Path:
    """
    Generate the HTML page of the game.
    Loads the template from resources then populates is with
    an NxN interactive table.

    :param grid_size: row and column number for the playing table
    :return: Path to the newly generated HTML file
    """
    with open(resource_path.joinpath('page_template.txt'), "r") as tf:
        table = '\n'.join(f"<tr>{
            ''.join(f'<td></td>' for _ in range(grid_size))
        }</tr>" for _ in range(grid_size))

        page_template = tf.read()
        page_txt = page_template.format(table_html=table)
        tf.close()

        page_html_path = resource_path.joinpath(page_html_name)
        with open(page_html_path, 'w') as o:
            o.write(page_txt)
            o.close()

        return page_html_path
