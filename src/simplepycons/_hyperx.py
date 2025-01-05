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


class HyperxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hyperx"

    @property
    def original_file_name(self) -> "str":
        return "hyperx.svg"

    @property
    def title(self) -> "str":
        return "HyperX"

    @property
    def primary_color(self) -> "str":
        return "#E21836"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HyperX</title>
     <path d="M22.428 5.234c-.036-.005-.055.05-.055.05-.935
 2.297-2.446 4.096-4.25
 5.503-2.157-1.445-4.476-2.16-6.477-2.5l.508-1.695H10.56l-.445
 1.496c-2.12-.194-3.61.004-3.664.008-.085.007-.108.027-.106.056.004.042.084.043.084.043
 4.228.324 7.684 1.789 10.367 3.528C9.926 16.098.15 15.826.15
 15.826c-.123-.002-.149.019-.15.065-.004.07.113.07.113.07 12.395 1.527
 17.776-2.796 18.238-3.143 3.685 2.82 5.513 5.867 5.513
 5.867.034.05.069.092.105.079.056-.02.02-.106.02-.106-1.062-3.053-2.666-5.243-4.475-6.808
 2.846-2.757 2.926-6.242 2.945-6.499.01-.113-.01-.115-.03-.117zM4.939
 6.592l-1.313 4.384h1.582l1.314-4.384Zm1.39
 2.023-.222.748h3.625c-.09.297-.483 1.613-.483
 1.613h1.594l.422-1.414a21.95 21.949 0 0 0-4.936-.947z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://ca.hyperx.com/cdn/shop/files/image_pl'''

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
