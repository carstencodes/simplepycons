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


class DatocmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datocms"

    @property
    def original_file_name(self) -> "str":
        return "datocms.svg"

    @property
    def title(self) -> "str":
        return "DatoCMS"

    @property
    def primary_color(self) -> "str":
        return "#FF7751"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DatoCMS</title>
     <path d="M12 0H.076v24H12c5.964 0 11.924-5.373
 11.924-11.998C23.924 5.376 17.963 0 12 0zm0 17.453a5.453 5.453 0
 115.455-5.451A5.45 5.45 0 0112 17.452z" />
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
