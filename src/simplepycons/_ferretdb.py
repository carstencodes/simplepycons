#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class FerretdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ferretdb"

    @property
    def original_file_name(self) -> "str":
        return "ferretdb.svg"

    @property
    def title(self) -> "str":
        return "FerretDB"

    @property
    def primary_color(self) -> "str":
        return "#042133"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FerretDB</title>
     <path d="M12.736.223a7.834 7.834 0 0 0-1.48.12C8.821.744 6.504
 2.14 5.02 4.086c-.817 1.098-1.203 1.737-1.04 1.737.045 0
 .283-.134.52-.312 1.99-1.41 5.6-2.05 8.005-1.41 2.302.608 3.52 1.559
 4.544 3.578.862 1.664 1.04 2.302 1.47
 5.05l.105.579.282-.357c.505-.653 1.128-2.123
 1.38-3.222.847-3.817-.771-6.995-4.44-8.747-1.03-.49-2.048-.742-3.11-.76zm-6.597
 5.76c-.307.018-.637.27-1.12.76-.52.51-1.055 1.007-1.604 1.487C1.975
 9.447.653 11.6.193 13.456c-.43 1.768-.12 4.352.727 6.03 1.292 2.584
 4.738 4.336 8.42 4.291.728 0
 .818-.03.565-.178-.832-.505-2.05-1.856-2.495-2.762-.445-.92-.475-1.07-.475-2.614
 0-1.5.03-1.693.416-2.42.683-1.292 1.396-1.901 2.732-2.287 1.604-.46
 2.406-1.233 2.852-2.733.178-.579.311-1.129.311-1.203
 0-.312-.43-.49-1.559-.653-2.109-.282-3.371-.936-4.574-2.302-.386-.446-.668-.66-.974-.642Zm1.182
 1.93c.186 0 .408.056.653.167.342.149.387.238.298.624-.268 1.233-.268
 1.574 0 1.871.415.46.816.357 1.559-.356.653-.654.861-.728
 1.648-.698.297.015.43.119.49.371.045.208.223.416.386.46.387.12.372.357-.074.98-1.544
 2.11-4.633
 2.095-5.717-.014-.49-.965-.357-2.376.326-3.238.097-.11.245-.167.431-.167Zm14.702
 1.771c-.074 0-.208.342-.297.758-.564 2.613-2.54 5.569-4.678
 6.95-1.663 1.084-2.346 1.262-4.99 1.277-1.262
 0-2.658-.06-3.103-.119l-.802-.119.104.49c.133.713 1.069 1.976 2.004
 2.748 1.708 1.396 3.312 1.9 5.51 1.782 3.906-.208 7.07-2.57
 8.034-5.97.12-.446.209-1.381.194-2.302
 0-1.292-.075-1.767-.401-2.718-.402-1.173-1.322-2.777-1.575-2.777z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/FerretDB/FerretDB/blob/117'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
