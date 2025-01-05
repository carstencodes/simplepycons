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


class TheAlgorithmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thealgorithms"

    @property
    def original_file_name(self) -> "str":
        return "thealgorithms.svg"

    @property
    def title(self) -> "str":
        return "The Algorithms"

    @property
    def primary_color(self) -> "str":
        return "#00BCB4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Algorithms</title>
     <path
 d="M8.226,19.857H1.353l1.79-4.225h4.812L13.308,3.21H7.564l-4.226,9.82h2.587c.18.3.511.51.887.51a1.04,1.04,0,0,0,1.038-1.037c0-.572-.467-1.023-1.038-1.023-.421,0-.767.24-.932.602H4.647l3.503-7.94h3.76L7.383,14.684l-4.766.03L0,20.79h8.842L10,18.263h3.835l1.278,2.526H24L15.985,3.211Zm2.27-2.586,1.384-3.023,1.503,3.023zm5.218,2.691-.872-1.759h2.737c.18.33.526.556.917.556a1.04,1.04,0,0,0,1.038-1.037,1.04,1.04,0,0,0-1.038-1.038c-.42,0-.782.256-.947.617H14.42l-2.09-4.06,1.534-3.369,1.729,3.519h.812c.165.346.526.601.932.601a1.04,1.04,0,0,0,1.038-1.037,1.04,1.04,0,0,0-1.038-1.038c-.436,0-.812.271-.962.662h-.3l-1.79-3.64,1.699-3.728,6.677,14.751Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/TheAlgorithms/website/blob'''

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
