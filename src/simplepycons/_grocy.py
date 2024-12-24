#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class GrocyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "grocy"

    @property
    def original_file_name(self) -> "str":
        return "grocy.svg"

    @property
    def title(self) -> "str":
        return "Grocy"

    @property
    def primary_color(self) -> "str":
        return "#337AB7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Grocy</title>
     <path d="M12.621.068C7.527.786 3.608 4.618 2.345 10.082c-.316
 1.35-.392 3.896-.163 5.203.62 3.57 2.96 6.574 6.15 7.913 1.36.577
 2.1.73 3.842.784 1.22.043 1.862.01 2.722-.13 2.688-.447 5.399-1.699
 6.65-3.092l.403-.447-.054-1.872a481.92 481.92 0 0
 1-.12-5.344l-.065-3.473-2.907.087c-1.589.033-3.722.098-4.746.142l-1.85.065-.087
 2.319c-.055 1.284-.076 2.34-.055 2.362.022.022.882.076
 1.916.12l1.872.076v.294c0 .707-.13.98-.555
 1.208-.653.326-1.872.479-2.623.326-2.71-.566-3.777-4.55-1.96-7.369C11.86
 7.48 13.873 6.62 16.562 6.74c.74.043 1.665.163
 2.123.272.446.12.838.174.87.12.098-.142.468-5.726.403-5.9-.087-.24-1.35-.697-2.569-.947-1.252-.25-3.722-.37-4.767-.218z"
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
        return '''https://github.com/grocy/grocy/blob/9e1020b7f'''

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