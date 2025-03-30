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


class PortableappsdotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "portableappsdotcom"

    @property
    def original_file_name(self) -> "str":
        return "portableappsdotcom.svg"

    @property
    def title(self) -> "str":
        return "PortableApps.com"

    @property
    def primary_color(self) -> "str":
        return "#818F95"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PortableApps.com</title>
     <path d="M12 0C7.977 0 4.419 1.984 2.24 5.022c-1.816 4.295.987
 7.619 4.001 7.532 2.925-.084 5.264-1.365
 7.04-3.4l-3.02-3.015h10.635l-.037 10.577-2.788-2.782c-2.739
 2.974-5.493 5.443-9.741 5.208C3.168 18.855.553 14.7.09 10.558.033
 11.032 0 11.512 0 12 0 18.63 5.37 24 12 24s12-5.371 12-12S18.625 0 12
 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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
