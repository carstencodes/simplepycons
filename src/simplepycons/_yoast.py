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


class YoastIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yoast"

    @property
    def original_file_name(self) -> "str":
        return "yoast.svg"

    @property
    def title(self) -> "str":
        return "Yoast"

    @property
    def primary_color(self) -> "str":
        return "#A61E69"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yoast</title>
     <path d="M16.61 0 11.4 14.477 8.806 6.36H5.941l3.804 9.77a4.017
 4.017 0 0 1 0 2.925c-.387.993-1.073 2.158-2.96 2.505V24c1.512-.06
 2.692-.562 3.694-1.57 1.032-1.036 1.919-2.655 2.79-5.091L19.739
 0ZM5.357 3.274a3.706 3.706 0 0 0-3.695 3.695v10.358a3.706 3.706 0 0 0
 3.695 3.694h.817l.26-.034c1.76-.237 2.37-1.224 2.733-2.158a3.4 3.4 0
 0 0 0-2.475L5.035 5.738H9.26l2.174 6.81 3.339-9.274Zm13.792.08L13.853
 17.55c-.502 1.403-1.015 2.54-1.559 3.47h10.044V6.97a3.706 3.706 0 0
 0-3.19-3.616Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
